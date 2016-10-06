from Tests.plan import Plan
from flask import Flask, render_template, request, url_for
from abc import ABCMeta, abstractmethod
from collections import defaultdict

import re

app = Flask(__name__)
test_list = []
test_state = []
test_time = []
pattern = '(\d)(-)(\w+)'

class TestPlan(object):
    def __init__(self):
        print 'creating the tests'
        self.test_steps = []

    def register_test(self, test):
        self.test_steps.append(test)

    def start(self):
        pass

    def run(self):
        pass

    def cleanup(self):
        pass


class Test(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


class Voltage(Test):
    def __init__(self, parent_test):
        self.parent_test = parent_test
        self.parent_test.register_test(self)

    def start(self):
        print 'setup voltage'

    def run(self):
        print 'running voltage test'

    def cleanup(self):
        print 'close voltage test'


class RunTests(object):
    def __init__(self, all_tests):
        steps = defaultdict()
        print 'initialize objects here'
        plan = TestPlan()
        for test in all_tests:
            set = re.search(pattern, test)
            test_name = set.groups()[2]

            steps[test_name] = eval(test_name)
            steps[test_name](plan)

    def run_all(self):
        print 'start running each test'
        

    def end(self):
        print 'close instruments'

# Using place holders to pass items to html
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        if request.form['start'] == 'start test':
            # Create the tests
            start = RunTests(test_list)
    print 'rendering page {}'.format(test_list)
    return render_template('home.html',
                           steps=test_list,
                           status=test_state,
                           elapse=test_time)

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
    print test_list
    app.run(debug=True, host='0.0.0.0')
