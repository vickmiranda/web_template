from Tests.plan import Plan
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
test_step = []
test_state = []
test_time = []

# Using place holders to pass items to html
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        if request.form['start'] == 'start test':

            print 'starting tests'
    print 'rendering page {}'.format(test_step)
    return render_template('home.html',
                           steps=test_step,
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
    test_step = my_plan.plan
    print test_step
    app.run(debug=True)
