from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard')
def dashboard():
    img_files=["head.png", "k-means-clust.png", "random-forest-regression.png"]
    return render_template('dashboard/dashboard.html', img_files=img_files)