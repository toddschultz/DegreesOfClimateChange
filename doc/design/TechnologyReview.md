<<<<<<< HEAD
The main task for this project is to retrieve climate data, in particular average global temperatures, from various sources. The data are offered typically using a RESTful webservice and thus make choosing an interface layer critical to the project.
=======
# Web Service Data Access Technology
The main task for this project is to retrieve climate data, in particular average global temperatures, from various sources. The data are offered typically using a RESTful webservice and thus make choosing an interface layer critical to the project.
>>>>>>> e5b02eb10e1838f039ac7865ac92adf8f19bc6b5

Requirements
To meet the needs of the intended audience for the project, the following requirements are specified.
* OS agnostic
* Available via FOSS license
* Simple commands for retrieving data
* Allows for a token or password to be transmitted in the header

# Available Technology
Python package to interface with RESTful APIs
## Requests http://docs.python-requests.org/en/master/
### Pros
* In Anaconda distribution
* Allows for username and passwords
* Designed for simple data retrieval
### Cons

## Pandas (pandas.read_csv)
### Pros
* Can read json formatted data
* Can read straight from URL
### Cons
* Doesn't appear to allow metadata in the header for URL calls


## Flask-RESTful https://pypi.python.org/pypi/Flask-RESTful
### Pros
### Cons
* Complex module designed as a full web development framework

## Simple REST Client https://pypi.python.org/pypi/simple-rest-client
### Pros
### Cons
* Not included in the Anaconda distribution

## EVE http://python-eve.org/
### Pros
### Cons
* Not included in the Anaconda distribution

## curl bash command
### Pros
* Readily availabe on Linus systems without installation
### Cons
* nix specific
* Requires calling system commands from Python


## wbpy
### Pros
* Single method calls to do the equivalent of multiple API requests, makes for much more readable and repeatable code
* Supports both ISO 1366 alpha-2 and alpha-3 country codes. Most standard API wrapper libraries only support alpha-3 ISO codes. i.e. wbpy supports 'legacy format' regarding the ISO-3166 standard (https://www.iso.org/iso/home/standards/country_codes.htm)
* Defines multiple subclasses i.e. GetClimateAPI(), GetModelAPI() each interfacing with the respective indicator dataset in the World Bank dataset (indicator list: https://data.worldbank.org/indicator)

# Visualization Technology
The project also needs to be able to generate a plot of the estimated average global temperatures from the various angencies. The requirements and user personas are assuming that the intended user has only basic computer programming experience and thus would favor simplier solutions. However, the plot must be able to be zoomed and panned and easily expendable to additional new data sources. 

## Matplotlib


## ?
