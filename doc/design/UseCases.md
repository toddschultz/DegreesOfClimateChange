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

Example

dataframe = grab_noaa()


### Question 2
How does the estimates from various agencies compare?

### Question 3
What other quantities correlate to the average global temperature?

### Question 4
How do I add another agency’s estimate?

### Question 5
How do I add another quantity?
