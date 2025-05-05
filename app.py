from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')  # Ensure index.html exists in your templates folder

# Route for the login page
@app.route('/login')
def login():
    return render_template('login.html')  # Ensure login.html exists

# Route for the dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # Ensure dashboard.html exists

# Route for the attendance page
@app.route('/attendance')
def attendance():
    return render_template('attendance.html')  # Ensure attendance.html exists

# Route for the grades page
@app.route('/grades')
def grades():
    return render_template('grades.html')  # Ensure grades.html exists

# Route for the schedule page
@app.route('/schedule')
def schedule():
    return render_template('schedule.html')  # Ensure schedule.html exists

# Route for the notice page
@app.route('/notice')
def notice():
    return render_template('notice.html')  # Ensure notice.html exists

# Route for the messaging page
@app.route('/messaging')
def messaging():
    return render_template('messaging.html')  # Ensure messaging.html exists

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Ensure contact.html exists

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')  # Ensure about.html exists

if __name__ == '__main__':
    app.run(debug=True)
