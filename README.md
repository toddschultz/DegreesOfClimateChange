## Degrees of (Climate) Change

[![Build Status](https://travis-ci.org/toddschultz/DegreesOfClimateChange.svg?branch=master)](https://travis-ci.org/toddschultz/DegreesOfClimateChange)

The climate of the planet has been in continual flux throughout the ages. We know of ice ages that created glaciers miles thick, we know of tropical periods that allowed the dinosaur to flurish. Recent times have seen the industrial age create unseen wealth, prosparity, opportunity, and pollution. The evidence indicates that our pollution in disrupting the natural climate of the planet and causing a shift in the global temperatures. However, the people  of the world are divided on the interupation of the evidence not from differences in data or methods but because of political reasons and self-interest. The goal of this work is to create a simple comparison of various estimates of the average global temperature. 
Although, ultimately all estimates of the average global temperature are based on the same pool of global temperature observations, the comparison is insightful to verify the processing applied by each source such as selection of observations and computational processing. 

### Organization of the  project

The project has the following structure:

```
.
├── DegreesOfClimateChange
│   ├── NOAAURL.txt
│   ├── NOAAtoken.txt
│   ├── NOAAtokenTemplate.txt
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
│   └── design
│       ├── Components.md
│       ├── DataSources.txt
│       ├── GithubStarCount.png
│       ├── Ideas.md
│       ├── TechnologyReview.md
│       ├── TechnologyReview.pptx
│       ├── UseCases.md
│       ├── UserPersonas.md
│       ├── Web-scraping\ Comparison\ Example.ipynb
│       └── designworkflow.md
└── examples
    ├── README.txt
    ├── berkeleyearth.ipynb
    ├── co2_data_retrieval.ipynb
    ├── grab_WorldBank_Module.ipynb
    └── noaa_co2_data.ipynb

5 directories, 29 files

```
### Module code

Describe the modules

### Project Data

Add description and citation for all data sources completed

### Installation

Update with installation instructions. 



### Git Configuration

Currently there is one file in the repository which help working
with this repository, and which you could extend further:

- `.gitignore` -- specifies intentionally untracked files (such as
  compiled `*.pyc` files), which should not typically be committed to
  git (see `man gitignore`)


