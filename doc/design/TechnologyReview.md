# Technology Review for Degrees of Climate Changes

# Web Service Data Access Technology
The main task for this project is to retrieve climate data, in particular average global temperatures, from various sources. The data are offered typically using either plain text files or a RESTful webservice API and thus making the choice of an interface layer critical to the project.

### Requirements
To meet the needs of the intended audience for the project, the following requirements are specified.
* OS agnostic
* Available via FOSS license
* Simple commands for retrieving data
* Allows for a token or password to be transmitted in the header

## Available Technology
Python package to interface with RESTful APIs

## Requests http://docs.python-requests.org/en/master/
r = requests.get(data_url, headers={'token’: api_key})

### Pros
* In Anaconda distribution
* Allows for username and passwords or tokens
* Designed for simple data retrieval
### Cons
* Doesn't return a DataFrame
* Better suited for JSON formated urls

## Pandas (pandas.read_csv)
df = pandas.read_csv(data_url, skiprows=header_skip)

### Pros
* Can read CSV or JSON formatted data
* Can read straight from URL
* Returns Pandas DataFrame
* Option to easily skip header lines in the file
### Cons
* Doesn't allow metadata in the header for URL calls
* Web scraping for arbitrary websites where data may be stored deep inside an HTML DOM tree is not easily done nor viable (i.e. libraries designed for web-scraping such as BeautifulSoup, Requests, Selenium, would be a better choice for this artbitrary situation)


## Example Case: Pandas vs. Selenium
* Suppose we search webpage: http://www.fdic.gov/bank/individual/failed/banklist.html
* Web page is already 'like' a table.
* Pandas read_html code to parse:
```python
    #PANDAS
    url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'
    dfs = pd.read_html(url)
    dfs

    #SELENIUM
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Firefox()
    driver.get('http://www.fdic.gov/bank/individual/failed/banklist.html')
    elem = driver.find_element_by_name('....insert HTML selector here....')
```
* So seems pandas is better, but....suppose we take an **arbitrary page**: i.e. 'www.python.org'
* Using pandas.read_html()...unclear how to proceed
* Using selenium: just change the driver.get() url to 'www.python.org' and now we have more *granular* access to the webpage elements

## BeautifulSoup
* A happy medium between direct web-scraping tools and the ease and simplicity of pandas
* Can easily interface with pandas functions i.e.
* Example: 'www.cnbc.com'...see jupyter notebook example and add to poiwerpoint 



## Flask-RESTful https://pypi.python.org/pypi/Flask-RESTful
### Pros
### Cons
* Complex module designed as a full web development framework

## Simple REST Client https://pypi.python.org/pypi/simple-rest-client
### Pros
### Cons
* Not included in the Anaconda distribution

## curl bash command
curl "https://www.dataurlgoeshere.com"

### Pros
* Readily availabe on Linux systems without installation
### Cons
* *nix specific
* Requires calling system commands from Python


## wbpy https://pypi.org/project/wbpy/
### Pros
* Single method calls to do the equivalent of multiple API requests, makes for much more readable and repeatable code
* Supports both ISO 1366 alpha-2 and alpha-3 country codes. Most standard API wrapper libraries only support alpha-3 ISO codes. i.e. wbpy supports 'legacy format' regarding the ISO-3166 standard (https://www.iso.org/iso/home/standards/country_codes.htm)
* Defines multiple .get(foo) functions, where foo is a query on a/many indicator(s) from the World Bank dataset (indicator list: https://data.worldbank.org/indicator). I.e. simply can do:
* ```python
     population_indicators = api.get_indicators(search="population")
     ```
* Automatically fills in missing dates within a queried time interval (if necessary)
### Cons
* Not included in the Anaconda distribution
* Restricted to WorldBank data only

# Visualization Technology
The project also needs to be able to generate a plot of the estimated average global temperatures from the various angencies. The requirements and user personas are assuming that the intended user has only basic computer programming experience and thus would favor simplier solutions. However, the plot must be able to be zoomed and panned and easily expendable to additional new data sources.

## Matplotlib


## ?
