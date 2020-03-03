from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


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


@app.route('/image-princess', methods=['GET', 'POST'])
def image_princess():
    if request.method == 'POST':
        selected_value = request.form['options']
        if selected_value == "option1":
            return redirect(url_for('start', selected_value=selected_value))
        if selected_value == "option2":
            return redirect(url_for('nein', selected_value=selected_value))

    return render_template('image-princess.html')


@app.route('/nein')
def nein():
    return render_template('nein.html')


@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        selected_value = request.form['options']
        if selected_value == "option1":
            pass
        if selected_value == "option2":
            pass
        if selected_value == "option3":
            pass
    return render_template('start.html')


if __name__ == '__main__':
    app.run(debug=True)
