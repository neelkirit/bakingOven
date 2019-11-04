import requests
from flask import (
    Blueprint,
    request)

bp = Blueprint('data_storage', __name__)


@bp.route('/store', methods=["GET", "POST"])
def store():
    if request.method == 'POST':
        angle = request.json['angle']
        user = request.json['user']
        product = request.json['product']
        url = 'http://localhost:8086/write?db=ineck'
        payload = 'angle,user=' + user + ',product=' + product + ' value=' + angle
        headers = {}
        res = requests.post(url, data=payload, headers=headers)
        print(res)

    return "Return Data points here"
