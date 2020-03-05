from flask import Flask, render_template, request, redirect, url_for
from textadventure import statusfeature

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
    return render_template("index.html", values=statusfeature.statusbar())


# Bild der Prinzessin
@app.route('/image-princess', methods=['GET', 'POST'])
def image_princess():
    if request.method == 'POST':
        selected_value = request.form['options']
        if selected_value == "option1":
            return redirect(url_for('start', selected_value=selected_value))
        if selected_value == "option2":
            return redirect(url_for('nein', selected_value=selected_value))
    return render_template('image-princess.html', values=statusfeature.statusbar())


# Dead End
@app.route('/nein')
def nein():
    return render_template('nein.html', values=statusfeature.statusbar())


""" QUEST ANFANG 
/ Erste richtige Entscheidung 
/ Hauptnummer 1 
"""

# begin story / Hauptnummer 1
@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        selected_value = request.form['options']
        if selected_value == "option1":
            return redirect(url_for('leave_tavern', selected_value=selected_value))
        if selected_value == "option2":
            return redirect(url_for('ask_barkeeper', selected_value=selected_value))
        if selected_value == "option3":
            return redirect(url_for('ask_tavern_person', selected_value=selected_value))
    return render_template('start.html', values=statusfeature.statusbar())

# Möglichkeit 1.1 Taverne verlassen
@app.route('/1.1_leave_tavern', methods=['GET', 'POST'])
def leave_tavern():
    if request.method == 'POST':
        selected_value = request.form['options']
        if selected_value == "option1":
            return redirect(url_for('leave_town', selected_value=selected_value))
        if selected_value == "option2":
            return redirect(url_for('town_square', selected_value=selected_value))
        if selected_value == "option3":
            pass
    return render_template('1.1_leave_tavern.html', values=statusfeature.statusbar())

# Möglichkeit 1.2 Wirt fragen
@app.route('/1.2_ask_barkeeper', methods=['GET', 'POST'])
def ask_barkeeper():
    if request.method == 'POST':
        selected_value = request.form['options']
        if selected_value == "option1":
            pass
        if selected_value == "option2":
            pass
        if selected_value == "option3":
            pass
    return render_template('1.2_ask_barkeeper.html', values=statusfeature.statusbar())

# Möglichkeit 1.3 Zwielichtige Person in Taverne befragen, keine Auswahlmöglichkeit
@app.route('/1.3_ask_tavern_person', methods=['GET', 'POST'])
def ask_tavern_person():
    return render_template('1.3_ask_tavern_person.html', values=statusfeature.statusbar())


""" DORF VERLASSEN
Hauptnummer 2
"""

# Möglichkeit 2 - Haupt , Dorf verlassen
@app.route('/2_leave_town', methods=['GET', 'POST'])
def leave_town():
    if request.method == 'POST':
        selected_value = request.form['options']
        if selected_value == "option1":
            pass
        if selected_value == "option2":
            pass
        if selected_value == "option3":
            pass
    return render_template('2_leave_town.html', values=statusfeature.statusbar())


""" ZUM DORFPLATZ
Hauptnummer 3
"""

# Möglichkeit 3 - Haupt, zum Dorfplatz
@app.route('/3_town_square', methods=['GET', 'POST'])
def town_square():
    if request.method == 'POST':
        selected_value = request.form['options']
        if selected_value == "option1":
            pass
        if selected_value == "option2":
            pass
        if selected_value == "option3":
            pass
    return render_template('3_town_square.html', values=statusfeature.statusbar())


if __name__ == '__main__':
    app.run(debug=True)
