import csv
import requests
from itertools import chain
from time import sleep

def is_image(file):
  return file['hasMimeType'] == 'image/jp2'

def get_filename(file):
  return file['filename']

def get_images(fileset):
  return list(map(get_filename, filter(is_image, fileset['structural']['contains'])))


def get_files(func, druid):
  max_retries = 3
  retry_count = 0
  backoff_factor = 2  # Multiplier for increasing wait time between retries

  while retry_count < max_retries:
    try:
        url = f'https://purl.stanford.edu/{druid}.json'
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad status codes (e.g., 4xx, 5xx)
        json_data = response.json()
        images = list(chain.from_iterable(map(get_images, json_data['structural']['contains'])))
        for image in images:
          func(image)
        break # exit loop on success
    except requests.exceptions.Timeout:
        retry_count += 1
        print(f"Timeout occurred. Attempt {retry_count} of {max_retries}.")

        if retry_count == max_retries:
            print("Max retries reached. Unable to complete the request due to repeated timeouts.")
            break

        # Wait before retrying again (with exponential backoff)
        sleep(backoff_factor ** retry_count)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred for {druid} {err}")
        break # exit loop
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {druid} {e}")
        break # exit loop

def harvest_files(start_at=0):
  with open('report2.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    # next(csv_reader) # skip headers

    with open('out.csv', mode='a') as outfile:
      csv_writer = csv.writer(outfile)
      # if start_at == 0:
        # csv_writer.writerow(['Druid', 'Filename'])
      for row_index, row in enumerate(csv_reader):
        if row_index >= start_at:
          druid = row[0]
          print(row_index)
          get_files(lambda image: csv_writer.writerow([druid, image]),  druid)

harvest_files(start_at=0)

# get_files('bb001nx1648')
