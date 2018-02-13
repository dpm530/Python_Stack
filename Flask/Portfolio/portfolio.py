from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('page1.html')

@app.route('/projects')
def projects():
    return render_template('page2.html')

@app.route('/about')
def about():
    return render_template('page3.html')

app.run(debug=True)
