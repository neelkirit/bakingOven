import requests
from flask import (
    Blueprint,
    request)

bp = Blueprint('data_storage', __name__)


@bp.route('/store', methods=["GET", "POST"])
def store():
    if request.method == 'POST':
        url = 'http://localhost:8086/write?db=mydb'
        payload = 'cpu_load_short,host=server01,region=us-west value=0.690'
        headers = {}
        res = requests.post(url, data=payload, headers=headers)
        print(res)

    return "Return Data points here"
