from flask import Blueprint, redirect, abort, request

from application import db
from reftrak_app.models import RedirectList, RedirectLog

reftrak_app = Blueprint('reftrak_app', __name__)

@reftrak_app.route('/<code>')
def init(code):
    redirect_obj = RedirectList.query.filter_by(code=code).first()

    # log the redirect
    ip = request.access_route[0]
    referrer = request.referrer
    redirect_log = RedirectLog(
        ip=ip,
        referrer=referrer,
        code=code
    )
    db.session.add(redirect_log)
    db.session.commit()

    if redirect_obj:
        return redirect(redirect_obj.url, code=302)
    else:
        abort(404)
