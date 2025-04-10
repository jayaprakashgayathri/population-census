from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "censalyze_secret"

# ---------- Routes ----------
@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'user123' and request.form['password'] == 'population':
            session['user'] = request.form['username']
            return redirect(url_for('homepage'))
        else:
            return "Invalid credentials"
    return render_template("login.html")

@app.route('/birthrate')
def birthrate():
    return render_template("birthrate.html")

@app.route('/mortality')
def mortality():
    return render_template("mortality.html")

@app.route('/income')
def income():
    return render_template("income.html")

@app.route('/sexratio')
def sexratio():
    return render_template("sexratio.html")

@app.route('/add-edit-data', methods=['GET', 'POST'])
def add_edit():
    if request.method == 'POST':
        data = request.form['data']
        module = request.form['module']
        conn = sqlite3.connect('census.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO population (Module, Data) VALUES (?, ?)", (module, data))
        conn.commit()
        conn.close()
        return redirect(url_for('homepage'))
    return render_template("add-edit-data.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ---------- Run App ----------
if __name__ == '__main__':
    app.run(debug=True, port=8000)
