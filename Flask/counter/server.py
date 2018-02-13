from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def counter():
    if 'number' not in session:
        session['number']=0
    session['number']+=1

    return render_template('index.html', counter=session['number'])

@app.route('/reset', methods=["POST"])
def reset_click():

    session['number'] = 0
    return redirect('/')

app.run(debug=True)
