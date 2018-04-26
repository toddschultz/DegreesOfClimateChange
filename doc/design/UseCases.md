## Use cases 

This document provides the use cases this project considered in its design. The use cases are presented as research questions as this project is focused on research and analysis tasks, not general computer interactions. 

## Question 1
What is the average global temperature from a certain agency?

Sally the scientist would like to call a simple, well-documented command to pull the estimated averaged global temperatures by specified agency. The data should be returned structured in a table format and should not include ancillary data or information that might be a destraction. However, the orignal sources of the data should be well-documented as Sally, as a trained scientist, will want to know where to find the complete description and reference for the data. Success for Sally is simple commands that can be called easily in an interactive environment such as a Jupyter notebook or interactive Python terminal. 

#### Inputs
Sally selects the appropriate command/function for the specified source
Sally calls the command/function with no required inputs

#### Outputs
Table of estimated averaged global temperatures with the corresponding date

#### Design
Set of Python functions with the following signature

dataframe = grab_<agency>()

#### Example

dataframe = grab_noaa()


### Question 2
How does the estimates from various agencies compare?

Sally the scientist would like to see a graph of the estimated average global temperatures from various agencies. The graph should start with the full time scale available and all agencies available. The should allow for easy zooming and panning to allow Sally to easily explore and interrogate the graph. The average global temperature estimates should be provided as a temperature with units of degrees Celsius as it will be the most meaningful quantity to Sally. 

#### Inputs
None.

#### Outputs
Graph readily available in an interactive forum with all available data and for the full time scale available.

#### Design
Line graph available in the final notebook product that has a line for each data source/agency. The x-axis should be the time axis presented with the full time scale available from all the data sources. The y-axis should be the average global temperature with units of degrees Celsius. Controls for zooming and panning should be accessible. 


### Question 4
How do I add another agency’s estimate?

Sally, being a scientist, will likely want to add additional data sources and agency estimates to expand and improve the analysis. The data sources already provided in the notebook should provide examples of how to build functions to retrieve, process, and organize the data from various agencies. Sally would also like simple, well-written instructions to help guide her through process of contructing the data access functions and integrating the new data set into the exiting notebook and graph. 

#### Inputs
New data source.

#### Outputs
A new data access function similar to the existing ones and a new line on the comparison graph. 

#### Design
Provide a read me file with plain english language instructions for creating a new data access function from a new data source. The instructions should be complete but concise and visually appealing such as in a list format. The existing data access functions should be well-documented to explain all the steps performed and why. They will serve as a set of examples for the construction of new functions. 

### Question 3
What other quantities correlate to the average global temperature?

### Question 5
How do I add another quantity?
