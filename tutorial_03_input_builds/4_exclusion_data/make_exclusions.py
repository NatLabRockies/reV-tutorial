"""Upload existing geotiffs into a new or existing reV-compatible HDF5 file."""
import os

import json
import pathlib

import h5py
import rasterio as rio

from reVX.handlers.layered_h5 import LayeredH5


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


# Sample Attributes
LAYER_ATTRS = {
    "ri_reeds_regions": {
        "some_key": "Anything else you would like to include.",
    }
}


# To convert from GeoTiffs to the HDF5 file.
def geotiffs_to_h5():
    """Upload geotiff to a new or existing h5 file."""
    if EXCL_FPATH.exists():
        os.remove(EXCL_FPATH)
    lh5 = LayeredH5(EXCL_FPATH)
    lh5.layers_to_h5(
        layers=LAYER_FPATHS,
        descriptions=LAYER_DESCS,
        attrs=LAYER_ATTRS,
        replace=False,
        check_tiff=True,
        transform_atol=0.01,
        scale_factors=None,
    )


# To convert HDF5 datasets back to GeoTiffs with h5py
def back_to_tif_h5py():
    """Convert HDF5 datasets back to geotiff with h5py."""
    hdf = h5py.File(EXCL_FPATH)
    out_dir = HOME.joinpath("export_1")
    out_dir.mkdir(exist_ok=True)
    for dataset in list(hdf):
        if not dataset.startswith(("lat", "lon")):
            array = hdf[dataset][0]
            profile = json.loads(hdf[dataset].attrs["profile"])
            dst = out_dir.joinpath(f"{dataset}.tif")
            with rio.open(dst, "w", **profile) as file:
                file.write(array, 1)


# To convert HDF5 datasets back to GeoTiffs with rex
def back_to_tif_revx():
    """Convert HDF5 datasets back to geotiff with rex."""
    lh5 = LayeredH5(EXCL_FPATH)
    lh5.extract_all_layers(out_dir="./export_2", extract_lat_lon=False)


if __name__ == "__main__":
    geotiffs_to_h5()
