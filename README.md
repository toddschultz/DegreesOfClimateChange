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
│   ├── __pycache__
│   │   ├── grab_berkeley.cpython-36.pyc
│   │   ├── grab_co2_scripps.cpython-36.pyc
│   │   ├── grab_noaa.cpython-36.pyc
│   │   └── grab_worldbank.cpython-36.pyc
│   ├── country_iso_codes.csv
│   ├── doe.json
│   ├── grab_berkeley.py
│   ├── grab_co2_scripps.py
│   ├── grab_noaa.py
│   ├── grab_worldbank.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_grab_berkeley.py
│   │   ├── test_grab_co2_scripps.py
│   │   ├── test_grab_noaa.py
│   │   └── test_grab_worldbank.py
│   └── version.py
├── LICENSE
├── README.md
├── doc
│   ├── Components.md
│   ├── DataSources.txt
│   ├── DegreesOfClimateChangeSummary.pptx
│   ├── GithubStarCount.png
│   ├── Ideas.md
│   ├── TechnologyReview.md
│   ├── TechnologyReview.pptx
│   ├── UseCases.md
│   ├── UserPersonas.md
│   ├── Web-scraping\ Comparison\ Example.ipynb
│   ├── design
│   └── designworkflow.md
├── examples
│   ├── GlobalTemperatureComparison-Final.ipynb
│   ├── __init__.py
│   ├── berkeleyearth.ipynb
│   ├── co2_data_retrieval.ipynb
│   ├── grab_WorldBank_Module.ipynb
│   └── noaa_co2_data.ipynb
├── requirements.txt
└── setup.py

6 directories, 44 files
```
### Module code

- `grab_noaa` retrieves global average temperatures (in anomaly units) from National Oceanic and Atmospheric Administration (NOAA)
- `grab_worldbank` retreives global average temperatures across all countries on earth between 1901 and 2012, in units degrees   Celsius, from the WorldBank dataset 
- `grab_berkeley` retrieves global average temperatures (in anomaly units) using data from BerkeleyEarth
- `grab_co2_scripps` retrieves _CO2_ data in units parts-per-million from various sampling stations across the globe, as part of the Scripps Institute for Oceanography at UCSD

### Project Data

1. Zhang, H.-M., B. Huang, J. Lawrimore, M. Menne, Thomas M. Smith, NOAA Global Surface Temperature Dataset (NOAAGlobalTemp), Version 4.0 NOAA Global Surface Temperature Data. NOAA National Centers for Environmental Information. doi:10.7289/V5FN144H.

Required Citations For Scripps Data:

2. Macfarling Meure, C. et al., 2006: Law Dome CO2, CH4 and N2O ice core records extended to 2000 years BP. Geophysical Research Letters, 33.
3. C. D. Keeling, S. C. Piper, R. B. Bacastow, M. Wahlen, T. P. Whorf, M. Heimann, and H. A. Meijer, Exchanges of atmospheric CO2 and 13CO2 with the terrestrial biosphere and oceans from 1978 to 2000. I. Global aspects, SIO Reference Series, No. 01-06, Scripps Institution of Oceanography, San Diego, 88 pages, 2001

### Installation

Update with installation instructions. 



### Git Configuration

Currently there is one file in the repository which help working
with this repository, and which you could extend further:

- `.gitignore` -- specifies intentionally untracked files (such as
  compiled `*.pyc` files), which should not typically be committed to
  git (see `man gitignore`)


