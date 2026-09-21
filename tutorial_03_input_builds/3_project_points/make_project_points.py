"""How to build a project points file."""
from pathlib import Path

from rex import Resource

from rev_tutorial import DATA


HOME = Path(__file__).parent

# Path to the HDF5 resource file
RES_FILE = DATA.joinpath("resource/ri_100_nsrdb_2012.h5")


def main():
    """Read, format, and write a project points file."""
    # Use rex's Resource class to pull out a formatted resource meta dataframe
    with Resource(RES_FILE) as res:
        meta = res.meta

    # The "gid" column is the original index and tell reV where to run
    meta.loc[:, "gid"] = meta.index

    # The config column tell reV which SAM config to run
    # Here we are assuming a single 'default' config will be run every where
    meta.loc[:, "config"] = "default"

    # Now you can subset, as long as the gid refers to the original index
    meta = meta[meta["population"] < 10_000]

    # All reV needs is config and gid, but you can include other fields
    project_points = meta[["latitude", "longitude", "gid", "config"]]

    # Save this to a project points file
    dst = HOME.joinpath("project_points.csv")
    project_points.to_csv(dst, index=False)


if __name__ == "__main__":
    main()
