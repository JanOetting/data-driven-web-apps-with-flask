from flask import app
import flask
from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services.package_service import get_latest_packages

blueprint=flask.Blueprint("home",__name__,template_folder="templates")

@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = get_latest_packages()
    return {'packages': test_packages}
    # return flask.render_template('home/index.html', packages=test_packages)


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}