import os
from flask import Flask, render_template, request, redirect, url_for, flash, session

from password_checker import check_password_strength, get_feedback

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Needed for flash and session

# Ensure users.txt exists
if not os.path.exists('users.txt'):
    open('users.txt', 'w').close()

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Read users
        with open('users.txt', 'r') as f:
            users = [line.strip().split(',') for line in f if ',' in line]

        # Check if username exists
        if any(user[0] == username for user in users):
            session['form_data'] = {'username': username}
            session['error'] = "❌ Username already exists."
            return redirect(url_for('register'))

        # Check password strength
        result = check_password_strength(password)
        if result != "Very Strong":
            feedback_list, strength = get_feedback(password)
            session['form_data'] = {'username': username}
            session['feedback'] = feedback_list
            session['strength'] = strength
            return redirect(url_for('register'))

        # Save user
        with open('users.txt', 'a') as f:
            f.write(f"{username},{password}\n")

        flash(" Registration successful!")
        return redirect(url_for('register'))

    # GET request
    username = ''
    error = feedback = strength = None

    if 'form_data' in session:
        username = session['form_data'].get('username', '')
        session.pop('form_data')

    if 'error' in session:
        error = session['error']
        session.pop('error')

    if 'feedback' in session:
        feedback = session['feedback']
        session.pop('feedback')

    if 'strength' in session:
        strength = session['strength']
        session.pop('strength')

    return render_template(
        'register.html',
        submitted=bool(error or feedback),
        username=username,
        error=error,
        feedback=feedback,
        strength=strength
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with open('users.txt', 'r') as f:
            users = [line.strip().split(',') for line in f if ',' in line]

        # Check credentials
        if any(user[0] == username and user[1] == password for user in users):
            flash(" Login successful!")
            return redirect(url_for('dashboard'))
        else:
            error = "❌ Invalid username or password."

    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    return "<h2> Welcome to your dashboard!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
