"""
Updated Cell tracking example
==============================

This example demonstrates how the tracking layer is used
for displaying 2D + time dataset of cells with colored properties for track-id.

Thanks to Dr. Alessia Ruggieri and Philipp Klein, Centre for Integrative Infectious
Disease Research (CIID), University Hospital Heidelberg, Germany for the data.
You can find the data on: https://doi.org/10.5281/zenodo.15597019

"""
import os

import pooch

###############################################################################
# Download the data
# ------------------
download = pooch.DOIDownloader(progressbar=True)
doi = '10.5281/zenodo.15597019'
tmp_dir = pooch.os_cache('napari-cell-tracking-example')
os.makedirs(tmp_dir, exist_ok=True)

data_files = "01.zip"

data_path = tmp_dir/data_files

if not data_path.exists():
    print(f"downloading archive {data_files}")
    download(f"doi: {doi}/{data_files}", output_file=data_path, pooch=None)
else:
    print(f"using cached {data_path}")
