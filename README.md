# Webservice Fetch Rewards
Web service that accepts HTTP requests and returns responses based on the conditions outlined in PDF.
Close repository on local device.
## Installation of python 
If you dont have python on your machine, you can install it from here and add pip and python to environment variables.
https://www.python.org/downloads/


## Dependencies installation
To install all dependencies please run the following command
Command:
```pip install -r requirements.txt```

## Files
1. webservice.py (webservice)
2. requirements.txt (contains requirements for program)
3. db_functions.py (contains functions used to perform calculations and db operations)
4. test.py (Test file to test and show how the webserice can be used)
5. configfile.ini (contains API URL's for test.py)

## Main Webservice
To run the webserice use the command : ```python webservice.py```

### Endpoints
**The server runs on localhost:5000 or 127.0.0.1:5000 by default.**
#### ADD Transaction
Send a ```POST``` request to ```http://127.0.0.1:5000/api/addTransaction``` where ```/api/addTransaction``` is the endpoint.
*Input:* Json with "payer","points" and "timestamp" field. 
    example= { "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }
*Output:* Message from server indicating succesfull addition of transaction

#### Spend Points
Send a ```POST``` request to ```http://127.0.0.1:5000/api/spendPoints``` where ```/api/spendPoints``` is the endpoint.
*Input:* Json with "points"
    example= { "points": 1000 }
*Output:* list of payers and points deducted from them

#### Player point balance
Send a ```GET``` request to ```http://127.0.0.1:5000/api/totalPoints``` where ```/api/totalPoints``` is the endpoint.
*Input:* No Input
*Output:* list of payers and their total balance points


## test.py
**By default config file uses 127.0.0.1 to run test.py** it can be changed in the configfile.ini to test accordingly.
To run test.py use the command : ```python test.py```
