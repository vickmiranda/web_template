from Tests.plan import Plan
from flask import Flask, render_template, request, url_for, redirect
from Tests.tests import RunTests


app = Flask(__name__)
test_list = []
test_state = []
test_time = []


# Using place holders to pass items to html
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        if request.form['start'] == 'start test':
            # Create the tests
            start = RunTests(test_list)
    print 'all test objects created successfully {}'.format(test_list)
    return render_template('home.html',
                           steps=test_list,
                           status=test_state,
                           elapse=test_time,
                           name=station_name)
@app.route('/station/<name>')
def station_name(name):
    print station_name
    print 'station route successful!'
    return redirect(url_for('home', name=station_name))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contributions')
def contributions():
    return render_template('contributions.html')

if __name__ == '__main__':
    # Load test plan
    my_plan = Plan()
    my_plan.read()
    test_list = my_plan.plan
    station_name = my_plan.station_name
    print test_list, station_name
    app.run(debug=True, host='0.0.0.0')
