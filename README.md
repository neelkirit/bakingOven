## Architecture of the application
* MySQL for storing User Info *[DONE]*
    * Schema defined in `flaskr\schema.sql`
* Angle Data stored in InfluxDB *[TBD]*
* Kafka acts as real-time mq to store angle from Flask to InfluxDB *[TBD]*
* Flask app listens from client by exposed APIs
* Flask app acts as producer to Kafka topic
* A new topic is created for each product
* InfluxDB acts as consumer to Kafka topic


## Development Environment
* Set following to the `environment` by running in Terminal - 
    *  `export FLASK_APP=flaskr`
    *  `export FLASK_ENV=development`
* Run the app -
    *   `flask run`
* After changes update the `requirements.txt` -
    *   `pip freeze > requirements.txt`

## Prepare for Deployment

## Production Environment
* Build Docker Image -
* Run Docker Image -