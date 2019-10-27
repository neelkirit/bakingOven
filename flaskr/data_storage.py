from flask import (
    Blueprint
)

bp = Blueprint('data_storage', __name__)


@bp.route('/')
def index():
    return "Return Data points here"
