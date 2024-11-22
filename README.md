# Extracting descriptions for images

Starting with https://argo.stanford.edu/report?f%5Bcontent_type_ssim%5D%5B%5D=image&f%5Bis_member_of_collection_ssim%5D%5B%5D=info%3Afedora%2Fdruid%3Agh795jd5965&f%5Brights_descriptions_ssim%5D%5B%5D=world download this report and save it as report.csv

Install venv:
```
$ python -mvenv .venv
$ source .venv/bin/activate
```

Then run `python3 find_files.py` to get the file list from SDR.
