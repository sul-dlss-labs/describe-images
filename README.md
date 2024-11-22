# Extracting descriptions for images

Starting with https://argo.stanford.edu/report?f%5Bcontent_type_ssim%5D%5B%5D=image&f%5Bis_member_of_collection_ssim%5D%5B%5D=info%3Afedora%2Fdruid%3Agh795jd5965&f%5Brights_descriptions_ssim%5D%5B%5D=world download this report and save it as report.csv

Install venv:
```
$ python -mvenv .venv
$ source .venv/bin/activate
```

Then run `python3 find_files.py` to get the file list from SDR. This produces `out.csv`

Next take out.csv and put it on Google Cloud Storage.

Then run `band_photos_from_stacks.ipynb` to collect a represenative image for each object from the IIIF server.

Finally run `band photos - Describe images.ipynb` to generate a description of the photos.
