import os
import sys
import flask
from pathlib import Path

from pypi_org.db import db_session

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)


app = flask.Flask(__name__)


def setup_db():
    dbfile=Path("data/pypi.sqlite")
    db_session.global_init(dbfile)



def main():
    register_blueprints()
    setup_db()
    app.run(debug=True)


def register_blueprints():
    from pypi_org.views import home_views
    from pypi_org.views import package_views
    from pypi_org.views import cms_views

    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(cms_views.blueprint)


if __name__ == '__main__':
    main()
