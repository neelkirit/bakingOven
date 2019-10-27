## Architecture of the application
* MySQL for storing User Info __*[DONE]*__
    * Schema defined in `flaskr\schema.sql`
* Angle Data stored in InfluxDB __*[TBD]*__
* Kafka acts as real-time mq to store angle from Flask to InfluxDB __*[TBD]*__
* Flask app listens from client by exposed APIs
* Flask app acts as producer to Kafka topic
* A new topic is created for each product
* InfluxDB acts as consumer to Kafka topic


## Setup Development Environment
* Clone the repository
    *   `git clone https://github.com/neelkirit/bakingOven.git`
* Navigate to project directory
    *   `cd bakingOven`
* Setup virtual environment
    *   `python3 -m virtualenv venv`
    *   `source venv/bin/activate`
* Install the dependencies in `venv`
    *   `pip install -e .`
* Verify the dependencies -
    *   `pip list`
* Set following to the `environment` by running in Terminal - 
    *   `export FLASK_APP=flaskr`
    *   `export FLASK_ENV=development`
* Run the app -
    *   `flask run`
* After changes update the `requirements.txt` -
    *   `pip freeze > requirements.txt`

## Prepare for Production Deployment
*When you want to deploy your application elsewhere, you build a distribution file. The current standard for Python distribution is the wheel format, with the `.whl` extension.
 Running `setup.py` with Python gives you a command line tool to issue build-related commands. The `bdist_wheel` command will build a wheel distribution file.*
* Install Wheel
    *   `pip install wheel`
* Build wheel distribution file -
    *   `python setup.py bdist_wheel`
* Locate the deployment binary at - 
    *   `dist/flaskr-1.0.0-py3-none-any.whl`

## Production Environment
#### Configure the Secret Key
* `SECRET_KEY` should be changed to some random bytes in production. Otherwise, attackers could use the public 'dev' key to modify the session cookie, or anything else that uses the secret key.*

* Copy the binary to deployment location - 
    *   `cp ~/bakingOven/dist/flaskr-1.0.0-py3-none-any.whl .`
* Generate Secret Key -
    *   `python3 -c 'import os; print(os.urandom(16))'`
* Create `config.py`
    *   `vi venv/var/flaskr-instance/config.py`
* Add `SECRET_KEY` -
    *   `SECRET_KEY = <GENERATED_DECRET_KEY>`
* Install Waitress -
    *   `pip install waitress`
* Run server -
    *   `waitress-serve --call 'flaskr:create_app'`

* Build Docker Image in local-
* Run Docker Image -