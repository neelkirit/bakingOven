from flask import Flask, request

import utils.db_util

app = Flask(__name__)


@app.route('/fetch')
def fetch():
    return utils.db_util.fetch()


@app.route('/register', methods=['POST'])
def register():
    print(request.json)
    return utils.db_util.register(request.json)


@app.route('/record_measurement', methods=['POST'])
def measurement():
    # Send to Influx DB
    return None


if __name__ == '__main__':
    app.run()

    # 23280725910672
