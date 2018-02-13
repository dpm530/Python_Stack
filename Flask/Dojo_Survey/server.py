from flask import Flask,render_template, request,session,flash,redirect
app=Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def main():
    return render_template('page1.html')


@app.route('/page2', methods=["POST"])
def validation():

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    validation_failed = False

    if len(session['name']) < 1:
        flash("Name cannot be blank!")
        validation_failed = True
    if len(session['comment']) < 1:
        flash("Comment cannot be blank")
        validation_failed = True
    if len(session['comment']) > 120:
        flash("Comment cannot be longer than 120 characters!")
        validation_failed = True


    if validation_failed == True:
        return redirect('/')
    else:
        return render_template('page2.html')





app.run(debug=True)
