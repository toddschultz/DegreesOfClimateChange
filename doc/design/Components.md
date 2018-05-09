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

# Comparison visualization
This component should create a clear and intuitive graph that compares the temperature estimates from the various data sources. The graph should eloquently handle data that could be in absolute units and deviation units.

## Design
graph with time (dates) on the x-axis and two y-axes, one for absolute temperature estimates and another for deviation temperature estimates

## Inputs
dataframes with two columns (Dates,Tabsolute_C or Tanomaly_C) for each data source (at least two)

## Outputs
graph with one line for each data source
