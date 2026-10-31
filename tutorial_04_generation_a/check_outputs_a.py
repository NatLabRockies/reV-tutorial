# -*- coding: utf-8 -*-
"""Some quick routines for checking reV generation outputs."""
from pathlib import Path

import matplotlib.pyplot as plt
import h5py
import pandas as pd
import reV

from rex import Resource

plt.ion()
plt.close("all")


HOME = Path(__file__).parent
GEN_FPATHS = list(HOME.glob("*generation*h5"))
RES_FPATHS = list(HOME.glob("*nsrdb*h5"))


def plotit(scf, stime):
    _, ax = plt.subplots(figsize=(3, 8))
    im = ax.imshow(scf, cmap="viridis")
    cbar = plt.colorbar(im, ax=ax, shrink=0.5)
    cbar.set_label("Capacity Factor", rotation=270, labelpad=20)
    ax.set_yticks(range(0, 1_000, 100))
    ax.set_yticklabels(stime[::100], rotation=45, fontsize=8)
    ax.set_title(
        r"$\bf{Sample\ reV\ Generation}$"
        "\nRhode Island, 2012\n2035 PV Tech",
        pad=20
    )
    plt.tight_layout()


def main():
    """Read in some reV generation outputs, check values, visualize."""
    # The outputs are HDF5 files in the format introduction in tutorial 3.2
    gen_fpath = GEN_FPATHS[0]
    ds = h5py.File(gen_fpath)

    # This is basically a dict object, list datasets like keys
    datasets = list(ds)
    datasets = ds.keys()

    # The biggest output is the capacity factor profile
    scale = ds["cf_profile_ac"].attrs["scale_factor"]
    cf = ds["cf_profile_ac"][:] / scale

    # Little trick for summary stats
    df = pd.DataFrame(cf.flatten())
    df.describe()

    # Everything else is site specific (x-axis of the profile)
    lcoe = ds["lcoe_fcr"][:]
    cf_mean = ds["cf_mean_ac"][:]

    # This is the time index, values are bytes objects
    # Also, these are in UTC, or Coordinated Universal Time
    time = ds["time_index"][:]
    time = [t.decode()[:-9] for t in time]

    # This is the meta "table", but it's stored as a structured array
    # And strings and other Python objects are stored as bytes
    meta = ds["meta"][:]
    meta = pd.DataFrame(meta)

    # Visualize the capacity factor profile
    # First, let's take a sample, it's too long to see it well (8,760 rows)
    scf = cf[:1_000]
    stime = time[:1_000]

    # Plot it
    plotit(scf, stime)


def show_other_items():
    """Show the audience some other items from the gen docs."""
    # Technology options
    options = reV.Gen.OPTIONS
    print(list(options))

    # Find the reV-SAM object
    windpower = reV.SAM.generation.Windpower

    # Find the original SAM object
    from PySAM import Pvwattsv8 as pv8
    pv = pv8.Pvwattsv8


if __name__ == "__main__":
    main()
