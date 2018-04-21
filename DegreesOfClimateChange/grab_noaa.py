# -*- coding: utf-8 -*-
"""grab_noaa retrieves global average temperatures from NOAA.

This python module contains a single function, grab_temperatures_NOAA, that
retrieves the global average temperature estimets from NOAA. This is the
climate data that is used to evaluate global climate change.

An overview of the data access available from NOAA is at:
https://www.ncdc.noaa.gov/data-access

The documentation for the NOAA RESTful Web Services v2 API is at:
https://www.ncdc.noaa.gov/cdo-web/webservices/v2

Reference documents from NOAA can be found at:
ftp://ftp.ncdc.noaa.gov/pub/data/noaa/

Instructions for obtaining an API key:
1. Go to <https://www.ncdc.noaa.gov/cdo-web/token> and
   submit a token request.
2. Open the "NOAAtokenTemplate.txt" file and enter the email
   address used to obtain the NOAA API token and the token
   itself into the second line of the file.
3. Save the file as "NOAAtoken.txt" in the same directory with
   the template file and the python module.

Written by Todd Schultz
2018
"""

import requests


def grab_temperatures_noaa():
    """Retrieves global average temperatures from NOAA."""
    
    # Read in API key
    with open("NOAAtoken.txt") as file:
        noaa_key = file.read()
    
    # example work for connecting to NOAA RESTful API
    base_url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/"
    end_point = "datasets"
    
    r = requests.get(base_url + end_point, headers={'token': noaa_key})
    
    
"""
r = requests.get('http://api.football-data.org/v1/competitions/398/teams')
x = r.json()
df = pd.DataFrame(x['teams'])
print df

r = requests.get('http://api.football-data.org/v1/competitions/398/teams')
df = pd.read_json(x.text)
"""
