# reV Tutorial
A tutorial for the Renewable Energy Potential Model ([reV](https://github.com/natlabrockies/reV)).

This is a repository for learning to run reV through its Command-Line Interface (CLI). It contains the sample input data found in the reV repository and sample run directories set up to create outputs for a study area in Rhode Island. Detailed instructions, example runs, and tests can be found in the official reV repository, but this repository will supplement that material with various Python scripts and preconfigured run folders specifically tailored for learning the basics of retrieving or building the input datasets, configuring the settings, running the model, and troubleshooting common problems.

# What is reV?

reV is a platform for the detailed assessment of renewable energy resources and their geospatial intersection with grid infrastructure and land use characteristics. It is centered on the concept of technical potential which will be covered in the first tutorial ([`tutorial_01_concepts`](https://github.com/NatLabRockies/reV-tutorial/tree/master/tutorial_01_concepts)) and is part of a network of interacting energy system models at the National Laboratory of the Rockies, but it is made fully open-source in the form of a Python package for public use. In addition, the lab has developed a suite of support packages. These serve both as direct dependencies for reV or as tools for building inputs and formatting outputs and which will be introduced in this series. 

As we move forward in this tutorial series, we will continue to elaborate on what reV is, what it does, and how it fits into energy systems analysis.

# Brief description of the reV modeling pipeline

reV is split into four main components: 
1) Simulating renewable energy generation and cost potential across a landscape. 
2) Creating model generation plants within spatial constraints.
3) Connecting plants to a transmission grid.
4) Reaggregating generation profiles (timeseries) into representative profiles for each model generation plant.

<p align="center">
  <img src="https://github.com/natlabrockies/reV-tutorial/blob/master/tutorial_05_pipeline/images/rev_standard_pipeline.png" alt="" height=400>
  <p align="center"> <i>reV is modular, outputs from one module serve as inputs to the next. Depending on the outputs needed, part or all of the reV pipeline can be used.</i></p>
</p>


At its foundation reV serves a spatial coordinator for the [Systems Advisor Model](https://sam.nlr.gov/). It runs any number of simulated generators at any number of points for which resource data is availabe. The resource datasets most typically used with reV (at least thus far) include the [National Solar Radiation Database](https://nsrdb.nlr.gov/) (NSRDB) and the [Wind Integration National Dataset Toolkit](https://www.nlr.gov/grid/wind-toolkit.html) (WTK), however any resource dataset can be used if it is formatted correctly.

reV is designed as a set of Python modules, each of which take as inputs the outputs of previous modules. The basic work flow is to take input "resource" datasets, a specifically formatted gridded timeseries of wind or solar irradiance, pass them through module generators (**in reV-Generation**) (wind turbines or photovoltaic panels) to create gridded timeseries of energy outputs and production costs, pass that into an aggregation module (**reV-Supply-Curve-Aggregation**) which combines the resource scale generation values into model plants with plant-level costs and energy production, and finally pass that into a transmission module (**reV-Supply-Curve**) which connects these plants to transmission and updates costs: 


 <h5 align="center"> Resource &rarr; Generation &rarr; Aggregation &rarr; Transmission &rarr; Potential Energy and Costs </h5>

 
Land use constraints can be added into the aggregation step to exclude development in parts of the study area, resulting in a range of plant sizes. It is also possible to create time series of plant-level power generation, or "representative profiles" as the final step, resulting in a modeling pipeline that looks like this:

  <h5 align="center"> Resource &rarr; Generation &rarr; Exclusions &rarr; Aggregation &rarr; Transmission &rarr; Potential Energy and Costs &rarr; Representative Profiles </h5>


# Tutorials on reV CLI methods

The quickest and easiest way to get started with reV is to use the **JSON-CLI** workflow. This involves building a JSON configuration file for a module you want to run and running that module with the corresponding CLI command. You can also configure several modules in the input-output pipeline described above and run each sequentially with a single command. The configurations will tell reV which SAM generator configurations to run and where, what variables to generate, which land-use assumptions to use, etc. It will also tell reV how to work with your system to most efficiently build these outputs (e.g. how to split the work across CPUs, how to split work across nodes for distributed systems, what memory utilization limits to use, etc.). This method is convenient in that you don't need to build Python scripts to actually run the model, it is relatively straightforward to set up and run directly from your terminal, and it leaves a tidy trail of run instructions which is useful for recreating or reviewing a reV run.

To learn about how to work with the reV JSON-CLI workflow, go into each `tutorial_##_module` folder sequentially and follow the instructions in each. 

# reV Documentation
Use this documentation in tandem with the tutorial series: [https://natlabrockies.github.io/reV/_cli/cli.html](https://natlabrockies.github.io/reV/_cli/cli.html).

# Getting started with the tutorial
Tutorial #1 ([`tutorial_01_concepts`](https://github.com/NatLabRockies/reV-tutorial/tree/master/tutorial_01_concepts)) will introduce key concepts needed to understand what the outputs of the reV model represent (particularly that of "technical potential"). It is recommended to start here, but if you understand that material and want to start running the model, you may skip to [`tutorial_02_setting_up`](https://github.com/NatLabRockies/reV-tutorial/tree/master/tutorial_02_setting_up). Each subsequent tutorial folder contains reV configuration files and a README describing how to use them to run reV and generate outputs. The READMEs will also describe what each configuration parameter means. These tutorials are ordered by increasing complexity. Early tutorials should be setup such that you may simply run the model without editing configuration files, though later tutorials will require user input in order to work.
