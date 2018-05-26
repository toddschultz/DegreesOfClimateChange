# Component Design
This document details the components needed for the project as identified by the other design documents such the use case document, the user persona document, and work flow document. 

## Jupyter Notebook
Jupyter notebook that contains the contextual documentation describing the purpose of the notebook, the orgin of the data sources, how to access the data sources, and a visualization of all of the average global temperature estimates. The components should be exposed such that users can see the calls and even change the inputs to explore data. 

### Design
Jupyter notebook with report sections such as Introduction, Data Sources, Analysis, and Conclusions. All calls to data access functions and visualization functions should be easily seen and described in detail. The visualization should provide an intuitive graph of the various average global temperature estimates The visualization should support comparison of the data even if the some sources are in absolute temperature values verus sources that are anomaly or deviation from a long term average temperature. 

### Inputs
None required

### Outputs
Complete, self documenting Jupyter notebook.

## Data access functions
Python functions that access, retrieve, clean, and store the data from the data sources. There should be one function per a data source with no required inputs. The outputs of all the functions should be similarly formatted Pandas dataframe. Most data sources provide average global temperature estimates on a monthly basis. 

### Design
temperature_df = grab_agency()

* 'agency'  should be replaced by the data source agency such as noaa for NOAA, wb for World Bank, etc

### Inputs
no required inputs

### Outputs
clean dataframe with two columns, Date and Tanomaly_C or Tabsolute_C
Date - date string with a minimum of the month and year for the average global temperature estimates
Tabsolute_C or Tanomaly_C - estimated average global temperature as an absolute or deviation, respectively, in units of degrees Celsius

# Comparison visualizations
This component should create a set clear and intuitive graphs that compares the temperature estimates from the various data sources. The graphs should eloquently handle data that could be in absolute units and deviation units. Note, after working with the data it was determined that a single graph would be inefficient and incomplete demonstrate the comparison. Thus this component was modified to include multiple graphs. 

## Design 
1. Graph with a subplot for each data source provided. The subplots should have time (dates) on the x-axis and temperature on the y-axes. The ranges for all of the x-axis should be the same, the maximum date range. The ranges for the y-axes should be the same for any subplots that are absolute temperature estimates and the same for any subplots that are for anomaly or deviation temperature estimates. This provide quick understanding of each data source individually and any overview or gross tends between the data sources. 

2. Graph with a subplotsfor overlaying the anomaly temperature estimate and a subplot for overlaying the absolute temperature estimates, so long as there are at least two data sources. This will provide quicker comparison of the tends and numeric values. 

## Inputs
Dataframes with two columns (Dates,Tabsolute_C or Tanomaly_C) for each data source(at least two)

## Outputs
Graph with one line for each data source
