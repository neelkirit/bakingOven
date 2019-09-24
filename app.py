from flask import Flask

import utils.db_util

app = Flask(__name__)


@app.route('/fetch_all')
def fetch_all():
    return utils.db_util.fetch_all()


@app.route('/record_measurement', methods=['POST'])
def measurement():
    # Send to Influx DB
    return None


if __name__ == '__main__':
    app.run()
