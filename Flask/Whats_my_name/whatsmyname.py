from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('page1.html')

@app.route('/page2', methods=['POST'])
def create_user():
    name1=request.form['name']

    return render_template('page2.html',name=name1)

app.run(debug=True)
