Project Points
===
Project points serve two main functions by telling reV 1) which locations to run and 2) what SAM configuration to run at each site. They may hold additional information to help either the user or contribute to site-specific functionality described later in the tutorial, but for a basic generation run they simply hold resource grid IDs and SAM configuration labels.

These points must be taken from the meta data of the resource data for the technology that is being run (e.g., NSRDB for PV, WTK for wind). This meta data will track the coordinate information for each grid ID, but reV only needs that grid ID. The example code in this folder is using a subset of the wind toolkit points and subsetting them to contain points that are only found in Rhode Island.

The project points file must have two columns, anything else is optional:
  1) "**gid**": The index position of the x-axis of the resource array, or the row index of the resource meta data table.
  2) "**config**": The key associated with a SAM config in the `config_gen.json` file. For solar it is '*default*' and wind it is '*onshore*'.

These points are then used as example inputs to the tutorial_4 and tutorial_5. 

