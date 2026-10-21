"""Upload existing geotiffs into a new or existing reV-compatible HDF5 file."""
import json
import pathlib

import h5py
import rasterio as rio

from reVX.handlers.layered_h5 import LayeredH5

from rev_tutorial import DATA


HOME = pathlib.Path(__file__).parent


# Target HDF5 file
EXCL_FPATH = HOME.joinpath("./RI_Exclusions.h5")

# Paths to datasets for upload to HDF5 file
LAYER_FPATHS = {
 "ri_padus": HOME.joinpath("ri_padus.tif"),
 "ri_reeds_regions": HOME.joinpath("ri_reeds_regions.tif"),
 "ri_smod": HOME.joinpath("ri_smod.tif"),
 "ri_srtm_slope": HOME.joinpath("ri_srtm_slope.tif")
}

# Dataset descriptions
LAYER_DESCS = {
 "ri_padus": "Protected Lands Dataset US.",
 "ri_reeds_regions": "ReEDS Regions.",
 "ri_smod": "Global Human Settlement Layer - Settlement Model",
 "ri_srtm_slope": "SRTM-derived slope."
}

# 


# To convert from GeoTiffs to the HDF5 file.
def geotiffs_to_h5():
    """Upload geotiff to a new or existing h5 file."""
    lh5 = LayeredH5(EXCL_FPATH)
    lh5.layers_to_h5(
        layers=LAYER_FPATHS,
        descriptions=LAYER_DESCS
    )


# To convert HDF5 datasets back to GeoTiffs with h5py
def back_to_tif_h5py():
    """Convert HDF5 datasets back to geotiff with h5py."""


# To convert HDF5 datasets back to GeoTiffs with rex
def back_to_tif_rex():
    """Convert HDF5 datasets back to geotiff with rex."""

