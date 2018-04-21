# -*- coding: utf-8 -*-
""" grab_temperatures_NOAA retrieves global average temperatures from NOAA.

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

def grab_temperatures_NOAA():
    """Retrieves global average temperatures from NOAA."""
    
    # Read in API key
    