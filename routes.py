from Tests.plan import Plan
from flask import Flask, render_template, request, url_for, redirect, flash
from Tests.tests import RunTests
from flask_moment import Moment, datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy

import os

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                        os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

test_list = []
test_state = []
test_time = []
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'


# Using place holders to pass items to html
@app.route('/', methods=['GET', 'POST'])
def home():

    print 'all test objects created successfully {}'.format(test_list)
    return render_template('home.html',
                           steps=test_list,
                           status=test_state,
                           elapse=test_time,
                           name=station_name)


@app.route('/start', methods=['GET', 'POST'])
def start():
    print 'test starting'
    if request.method == "POST":
        if request.form['begin'] == 'starting':
            # Create the tests
            start = RunTests(test_list)
            start.run_tests()
            start.end()

    return redirect(url_for('home'))


@app.route('/about')
def about():
    form = Form()
    return render_template('about.html', form=form)


@app.route('/contributions')
def contributions():
    return render_template('contributions.html')


@app.errorhandler(404)
def handler_error_404(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    # Load test plan
    my_plan = Plan()
    my_plan.read()
    test_list = my_plan.plan
    station_name = my_plan.station_name
    print test_list, station_name
    print datetime.now()
    app.run(debug=True, host='0.0.0.0')
