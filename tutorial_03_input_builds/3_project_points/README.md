Project Points
===
Project points serve two main functions by telling reV 1) which locations to run and 2) what SAM configuration to run at each site. They may hold additional information to help either the user or contribute to site-specific functionality described later in the tutorial, but for a basic generation run they simply hold resource grid IDs and SAM configuration labels.

These points must be taken from the meta data of the resource data for the technology that is being run (e.g., NSRDB for PV, WTK for wind). This meta data will track the coordinate information for each grid ID, but reV only needs that grid ID. The example code in this folder is using a subset of the wind toolkit points and subsetting them to contain points that are only found in Rhode Island.

The project points file must have two columns, anything else is optional:
  1) "**gid**": The index position of the x-axis of the resource array, or the row index of the resource meta data table.
  2) "**config**": The key associated with a SAM config in the `config_gen.json` file. For solar it is '*default*' and wind it is '*onshore*'.

The script uses the reV package resource helper `rex` and its `Resource` class to facilitate formatting from the HDF5 format, which cannot store Python objects such as strings or Pandas dataframes. To pull the meta data out as as a Pandas dataframe, we simply run

```python
from rex import Resource

with Resource("path/to/resource.h5") as res:
    meta = res.meta
```

Because reV uses the grid ID of the 2D resource array to pull the data that it feeds into SAM, we associate each row in the meta data table with its original index position

```python
meta.loc[:, "gid"] = meta.index
```

We may use labels to tell reV to tell SAM which configuration file to run at each site. Here we are telling the model to run configuration file `1` in Providence County and configuration file `2` in Kent County.


```python
meta.loc[meta["county"] == "Providence", "config"] = "sam_one"
meta.loc[meta["county"] == "Kent", "config"] = "sam_two"
```

Later, in the generation module in the next tutorial, you will see that we may associate any number of SAM configuration files with labels. For a preview of what that looks like, here is a snippet from the generation configuration file that associates these labels with the actual SAM configuration files.

```json
...
"sam_files": {
  "sam_one": "path/to/sam_configuration_1.json5",
  "sam_two": "path/to/sam_configuration_2.json5"
},
...
```

You may then filter this dataframe down to just the target sites (here we are only running these in locations below a certain elevation) and needed fields. Though you only need `gid` and `config`, it can be useful to include at least the coordinates.

```python
meta = meta[meta["elevation"] < 150]
project_points = meta[["latitude", "longitude", "gid", "config"]]
```

Then save these files to a CSV. The path to this CSV will be used later in the same generation config mentioned above.

```python
project_points.to_csv("path/to/project_points.csv", index=False)
```
