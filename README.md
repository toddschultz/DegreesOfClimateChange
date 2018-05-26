## Degrees of (Climate) Change

[![Build Status](https://travis-ci.org/toddschultz/DegreesOfClimateChange.svg?branch=master)](https://travis-ci.org/toddschultz/DegreesOfClimateChange)
[![Coverage Status](https://coveralls.io/repos/github/toddschultz/DegreesOfClimateChange/badge.svg?branch=master)](https://coveralls.io/github/toddschultz/DegreesOfClimateChange?branch=master)

The climate of the planet has been in continual flux throughout the ages. We know of ice ages that created glaciers miles thick, we know of tropical periods that allowed the dinosaur to flurish. Recent times have seen the industrial age create unseen wealth, prosparity, opportunity, and pollution. The evidence indicates that our pollution in disrupting the natural climate of the planet and causing a shift in the global temperatures. However, the people  of the world are divided on the interupation of the evidence not from differences in data or methods but because of political reasons and self-interest. The goal of this work is to create a simple comparison of various estimates of the average global temperature. 
Although, ultimately all estimates of the average global temperature are based on the same pool of global temperature observations, the comparison is insightful to verify the processing applied by each source such as selection of observations and computational processing. 

### Organization of the  project

The project has the following structure:

```
.
├── DegreesOfClimateChange
│   ├── __init__.py
│   ├── country_iso_codes.csv
│   ├── doe.json
│   ├── grab_berkely.py
│   ├── grab_noaa.py
│   ├── grab_worldbank.py
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_grab_noaa.py
│   └── version.py
├── LICENSE
├── README.md
├── doc
│   ├── Components.md
│   ├── DataSources.txt
│   ├── GithubStarCount.png
│   ├── Ideas.md
│   ├── TechnologyReview.md
│   ├── TechnologyReview.pptx
│   ├── UseCases.md
│   ├── UserPersonas.md
│   ├── Web-scraping\ Comparison\ Example.ipynb
│   └── designworkflow.md
└── examples
    ├── README.txt
    ├── berkeleyearth.ipynb
    ├── co2_data_retrieval.ipynb
    ├── grab_WorldBank_Module.ipynb
    └── noaa_co2_data.ipynb

5

```
### Module code

grab_noaa retrieves global average temperatures from National Oceanic and Atmospheric Administration (NOAA)

### Project Data

Zhang, H.-M., B. Huang, J. Lawrimore, M. Menne, Thomas M. Smith, NOAA Global Surface Temperature Dataset (NOAAGlobalTemp), Version 4.0 NOAA Global Surface Temperature Data. NOAA National Centers for Environmental Information. doi:10.7289/V5FN144H.

Required Citations For Scripps Data:

II. Macfarling Meure, C. et al., 2006: Law Dome CO2, CH4 and N2O ice core records extended to 2000 years BP. Geophysical Research Letters, 33.
III. C. D. Keeling, S. C. Piper, R. B. Bacastow, M. Wahlen, T. P. Whorf, M. Heimann, and H. A. Meijer, Exchanges of atmospheric CO2 and 13CO2 with the terrestrial biosphere and oceans from 1978 to 2000. I. Global aspects, SIO Reference Series, No. 01-06, Scripps Institution of Oceanography, San Diego, 88 pages, 2001"

### Installation

Update with installation instructions. 



### Git Configuration

Currently there is one file in the repository which help working
with this repository, and which you could extend further:

- `.gitignore` -- specifies intentionally untracked files (such as
  compiled `*.pyc` files), which should not typically be committed to
  git (see `man gitignore`)


