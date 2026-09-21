# -*- coding: utf-8 -*-
"""Convert files to exclusion datasets.

Author: twillia2
Date: Wed Sep 16 14:26:05 MDT 2026
"""
import json

from pathlib import Path

import h5py


HOME = Path(__file__).parent
DATA = HOME.parent.joinpath("data")
DST = DATA.joinpath("exclusions/Natural_Gas_Exclusions.h5")
SAMPLE = ("/kfs2/projects/rev/data/exclusions/north_america/conus/"
          "standard_exclusions_and_characterizations_fy25.h5")
SOURCES = {
    "non_attainment_co2": {
        "src": DATA.joinpath("vectors/CO_1971std_naa.shp"),
        "attrs": {
            "description": "Dah dah dah",
            "original_file": "path/path.shp",
            "lookup": "if categorical",
            "date": "whenever either you got it or it was made.",
            "source": "Preferrably a URL."
        }
    }
}


def main():
    """Convert all layers to and HDF5 file."""
    # Creat target folder
    DATA.mkdir(exist_ok=True)

    # Open new file
    ds = h5py.File(DST, "w")

    # Open old file
    ods = h5py.File(SAMPLE)

    # Write top-level attributes
    for key, attr in ods.attrs.items():
        if "reVX" not in key:
            ds.attrs[key] = attr

    # Pull out your profile
    profile = json.loads(ds.attrs["profile"])

    # Upload each file
    for key, info in SOURCES.items():

        fpath = info["src"]
        attributes = info["attrs"]

        # Rasterize to the exact shape in profile above
        array = None   # The resulting array
        dtype = None

        # Add the dataset to the HDF5 file
        ds.create_dataset(name=key, data=array, dtype=dtype)

        # Add attributes
        for akey, attrs in attributes.items():
            ds.attrs[akey] = attrs


if __name__ == "__main__":
    pass
