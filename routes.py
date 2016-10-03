from flask import Flask, render_template, request

app = Flask(__name__)
test_step = ["Voltage Test", "Running", "10:10"]
test_state =["Running", "Waiting"]

# Using place holders to pass items to html
@app.route('/')
def home():
    if request == "post":
        print 'test running'
    return render_template('home.html', steps=test_step, status=test_state)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contributions')
def contributions():
    return render_template('contributions.html')

if __name__ == '__main__':
    app.run(debug=True)