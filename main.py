from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# index page / main page / home page if you click on "Starte dein Abenteuer neu"
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_value = request.form['options']
        if selected_value == "option1":
            return redirect(url_for('start', selected_value=selected_value))
        if selected_value == "option2":
            return redirect(url_for('nein', selected_value=selected_value))
        if selected_value == "option3":
            return redirect(url_for('image_princess', selected_value=selected_value))

    return render_template("index.html")


# Bild der Prinzessin
@app.route('/image-princess', methods=['GET', 'POST'])
def image_princess():
    if request.method == 'POST':
        selected_value = request.form['options']
        if selected_value == "option1":
            return redirect(url_for('start', selected_value=selected_value))
        if selected_value == "option2":
            return redirect(url_for('nein', selected_value=selected_value))

    return render_template('image-princess.html')

# Dead End
@app.route('/nein')
def nein():
    return render_template('nein.html')


""" QUEST ANFANG 
/ Erste richtige Entscheidung 
/ Hauptnummer 1 
"""


@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        selected_value = request.form['options']
        if selected_value == "option1":
            return redirect(url_for('leave_tavern', selected_value=selected_value))
        if selected_value == "option2":
            pass
        if selected_value == "option3":
            pass
    return render_template('start.html')

# Möglichkeit 1.1 Taverne verlassen
@app.route('/1.1_leave_tavern', methods=['GET', 'POST'])
def leave_tavern():
    if request.method == 'POST':
        selected_value = request.form['options']
        if selected_value == "option1":
            pass
        if selected_value == "option2":
            pass
        if selected_value == "option3":
            pass
    return render_template('1.1_leave_tavern.html')


if __name__ == '__main__':
    app.run(debug=True)
