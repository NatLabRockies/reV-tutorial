# -*- coding: utf-8 -*-
"""Some quick routines for the outputs."""
from pathlib import Path

import matplotlib.pyplot as plt

import h5py
import pandas as pd
import reV

from rex import Resource


HOME = Path(__file__).parent
MY_FPATH = list(HOME.glob("*multi-year*h5"))[0]


def main():
    """Read in some reV generation outputs, check values, visualize."""
    # Let's use rex this time
    res = Resource(MY_FPATH)

    # Want to see it in a GIS?
    # You need the meta object, which is a bit messy without rex
    meta = res.meta


def show_other_stuff():
    """Show the audience some other items from the gen docs."""


if __name__ == "__main__":
    pass
