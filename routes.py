from flask import Flask, render_template, request, url_for

app = Flask(__name__)
test_step = ["Voltage Test", "Current Test", "Frequency Test"]
test_state =["Running", "Waiting", "Waiting"]
test_time = ["10.10", "2:20", "0:00"]



# Using place holders to pass items to html
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        if request.form['start'] == 'start test':

            print 'starting tests'
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
    app.run(debug=True)