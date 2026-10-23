# Technical Potential

> *"It is a truism that everything affects everything else. More specific to the subject at hand are the observations that the evolution of energy demand depends on the supply options available, while the availability of different supply options is itself influenced by the level of energy demand. **Moreover, both depend on environmental constraints, resource constraints, and the like**."* <br><br> -Alan McDonald, *Energy in a Finite World (1981)*

We can estimate the amount of oil in the Earth or the amount of physical energy embedded in the sunlight hitting its surface, but how much of that can be converted to useable energy? That initial amount of resource will be reduced by how much of it we can realistically access and how much of that we can convert into a useable form (e.g., electricity). This amount is referred to as *"technical potential"*, the estimation of which  is the central purpose of the reV modeling platform. This technical potential may be further reduced by economically viable production cost thresholds, which we refer to as *"techno-economic potential"*. Finally, this third amount can be filtered to an even smaller value that considers the interplay between supply and demand and other social, political, and market variables to represent a realistically deployable amount of generation potential. The reV model is focused only on the technical and techno-economic potential tiers of this assessment model, but is designed to facilitate the later steps (see Figure 1). Resource assessment serve as an input to reV while its outputs serve as inputs to downstream models. This techno-economic potential will vary widely between generation technologies and geographies, as well as technological and economic assumptions of the future.

<p align="center">
  <img src="./images/tech_potential_re.png" alt="Renewable Energy Technical Potential Levels" width="1200">
  <br>
  <em><b>Figure 1.</b> Conceptual diagram of potential energy levels for renewable energy. The bottom bar represents NLR models and relative certainty associated with each level.</a>.</em>
</p>



## The Renewable Energy Potential Model

The Renewable Energy Potential model (reV) is designed to provide large scale and detailed estimates of techno-economic potential for use in energy resource assessments. In general, the outputs of reV represent the top-level capacity and generation potential for a given technology in a given place as well as the costs associated with these amounts. The output data comes in two basic varieties: 1) summary tables describing site-specific techno-economic characteristics across a field of potential sites and 2) the potential energy generation timeseries (or profiles) associated with each site. It is designed to be as flexible as possible and these outputs may be provided at any spatial and temporal resolution the reV analyst has input data for. 

Users may be interested in the direct outputs of reV, to the degree that a theoretical maximum potential estimate is, or they may wish to use these as inputs in downstream models. One of the more common uses of reV is to develop the field of possible plants for capacity expansion models such as the Regional Energy Deployment System (ReEDS). 

## Renewables Vs. Non-renewables
We’ll try to understand how energy assessments happen across the energy spectrum – renewables vs. oil & gas. Therefore, how to define resource potential is important. The energy generator has to be in the same place where there is resource availability. Therefore, understanding where the resource is available and how much is available brings us to the starting point to any kind of energy analysis.

### What is a resource?
- Resource is the input utilized for energy generation (electricity) by a generator (Wind Turbine, Solar Panel, Steam Turbine etc.)
Renewable energy is a site-specific resource and cannot be transported elsewhere for energy generation. Non-renewables like Crude oil, Natural gas, Coal are not site-specific resources, and they can be transported to a generation site.

![re_potential_cirlces_diagram](https://github.com/user-attachments/assets/ae2aff1c-6117-4977-8f7f-a686a147b6a7)
*Renewable Energy Assessments - Levels of Potential.*
*Source: Geospatial Data Science Group - National Renewable Energy Laboratory (2024).* 
 <!-- [Reference or URL](https://example.com) -->

## Resource Potential
The resource potential is the theoretical availability of renewable energy across an area is resource potential. It quantifies the energy content of a resource at specific location. There are two resource datasets developed at NREL for understanding solar resource potential and wind resource potential:
- National Solar Radiation Database (NSRDB) for solar (Sengupta et al. 2018)
- Wind Integrated National Dataset Toolkit (WTK) for wind (Draxl et al. 2015)

![nsrdb_coverage_map_042024](https://github.com/user-attachments/assets/a3b7778d-b126-46ef-91d1-73a2447aa216)
*Source: Geospatial Data Science Group - National Renewable Energy Laboratory (2024).* 

![wtk_coverage_map_042024](https://github.com/user-attachments/assets/302cf3e2-aaf4-407d-8172-a175ec0e6c60)
*Source: Geospatial Data Science Group - National Renewable Energy Laboratory (2024).* 


## Technical Potential
### Define technical potential
- Technical potential refers to the maximum amount of capacity and generation possible in an area, given physical, technological and regulatory constraints (refer to reV 2019 & reV 2023 reports)
- Technical potential is a measure of resource potential that could be developed based on assumptions of the developable area defined by the user
    - For example, the user can limit development by land ownership, terrain, land use/cover, and urban areas, as well as other custom inputs
- The benefit of assessing technical potential is that it establishes an upper boundary estimate of development potential (Lopez et al. 2012)

- Contextualize in terms of broader energy availability assessment (e.g., geological surveys in the Oil and Gas industry; see figure below)
    - Geological surveys are conducted in the oil and gas industries to assess the available total resources underground, which is referred to the in-place resources. The tech pot in renewable energy has a similar definition to the in-place resources in the oil and gas industry, where we are measuring the maximum available energy or resources after applying exclusions and contraints. 

*Oil and Gas Energy Assessments - Levels of Potential*

<p align="center">
  <img src="https://github.com/user-attachments/assets/8c1592e6-5a45-4c3e-a254-e6e59e01ab71" width="1000">
</p>

<!-- ![oil_gas_potential_cirlces_diagram](https://github.com/user-attachments/assets/8c1592e6-5a45-4c3e-a254-e6e59e01ab71) -->
<p align="center">Source: U.S. Energy Information Administration ([2014](https://www.eia.gov/todayinenergy/detail.php?id=17151))</p>


Ideally, we'll convince Galen or Donna or Anthony to make a guest appearance and describe their thought process when they developed the technical potential analysis approach...this could also lead directly into the Model


## Introducing the reV Model 
One of the main responsibility of GDS is the renewable energy potential a.k.a. reV model. What is it? 

- Background info about reV
    - Why it's called reV? It's a short for The Renewable Energy Potential (reV)
    - reV is an open-source geospatial platform for assessing system performance, available capacity, distance to transmission, and total costs for potential solar and wind energy deployment at regional to continental scales.
    - Potential and intended users of reV model outputs include utility planners, regional and national agencies, project and land developers, internal NREL modelers, and external researchers. 

The reV model supports broadly three components:
- Simulating renewable energy generation and cost potential across a landscape.
- Simulating discrete generation plants with spatial constraints.
- reV serves a spatial coordinator for the Systems Advisor Model (SAM). It can help connect renewable energy plants to a transmission. 

Overview of the input-output pipeline of reV: 
![rev_flow](https://github.com/user-attachments/assets/e5ab2d7c-e7fd-4201-801a-a55ec6156136)

- How speciifcally does the model represent technical potential (e.g., what are the outputs.)
    - The LCOE output can serve as the end point of a reV analysis, providing insight into economic competitiveness, relative performance competitiveness, and regional differences driven by cost assumptions. LCOE estimates can also be used downstream in the supply curves. 
    - The tech pot is represented as a function of the available land area after applying exclusions, the net capacity factor estimated by the generation module, and a user-defined power density appropriate for the specific technology. The power density value represents the maximum potential capacity for a given unit of area (e.g., MW/km2). 

- How does this model fit into the broader energy modeling ecosystem at NREL.

- Describe the open-source nature of reV...anyone can use it, though challenges exists in acquiring and/or building input datasets, which we'll cover in Episode #3.
- Describe who all is using it.

### Here need to add info to introduce the NREL Modeling Ecosystem
![seac_ecosystem](https://github.com/user-attachments/assets/74ceb6cc-9b2f-463a-84cf-873abe6f673e)

## Renewable energy glossary
This section includes abbreviations, concepts, knowledge gaps that might not be familiar to the audiences; we can expand this glossary along the tutorial making process. 
- SAM = Systems Advisor Model. SAM is an open-source techno-economic software model that simulates estimating power generation and financial viability for renewable energy technologies...(https://sam.nrel.gov).
- LCOE = Levelized Cost of Energy. LCOE represents the average revenue per unit of electricity generated that would be required to recover the costs of building and operating a generating plant during an assumed financial life. 
- Supply curves = represent the cost and amount of energy at all reV-modeled potential sites at a snapshot in time. 

## Images to be assimilated
Put any candidates images here.


