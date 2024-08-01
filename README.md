<h1 align=center><strong>Analytics Master Service</strong></h1>

## Overview
The Analytics Master Service powers a data analytics dashboard designed to provide accurate business insights for better decision-making. This service leverages Python and FastAPI to deliver robust API endpoints, facilitating data retrieval and analysis from a PostgresSQL database.

## Tech Stack

* 🐍 [FastAPI](https://fastapi.tiangolo.com/)
* 🐘 [PostgreSQL](https://www.postgresql.org/docs/current/libpq-async.html)
* 🐳 [Dockerized](https://www.docker.com/)


## Project Structure

https://excalidraw.com/#json=XDaDU3WIf3NGatw0L6UYj,2_NfKKC_VxJpcCalijr1Tg

When the `Docker` is started, the base URL address:

* Backend Application $\rightarrow$ `http://127.0.0.1:5000/api`

# API Endpoints

   Detailed API documentation is available at :- https://drive.google.com/file/d/1reQidBjWVKuxEyBA14QY0kRtcPaMQlmQ/view?usp=drivesdk
   
# CURL
1- Endpoint: /totalSale

`curl --location
'http://127.0.0.1:5000/api/totalSale?start_date=2024-01-07&end_date=2024-04-07'`

2- Endpoint: /sales-by-dimensions

    curl --location 'http://127.0.0.1:5000/api/sales-by-dimensions?group_by=category'

3- Endpoint: /market-share-changes

    curl --location
    'http://127.0.0.1:5000/api/market-share-changes?start_date=2024-01-07&end_date=20
    24-05-07'

4- Endpoint: /sale/brand/{brand_id}

    curl --location 'http://127.0.0.1:5000/api/sale/brand/1001'
