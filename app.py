from flask import Flask, render_template, redirect, url_for, flash, session
from forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        # Here you would typically save to a database
        flash(f'Account created successfully!', 'success')
        return redirect(url_for('alumni_login'))  # Redirect to alumni login after registration
    return render_template('register.html', form=form)

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        # Admin login logic
        if email == 'admin@sju.edu' and password == 'adminpassword':
            session['user_type'] = 'admin'
            session['email'] = email
            flash('Welcome to Admin Dashboard!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid admin credentials!', 'danger')
    return render_template('admin_login.html', form=form)

@app.route('/alumni_login', methods=['GET', 'POST'])
def alumni_login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        # Alumni login logic
        if email.endswith('@alumni.sju.edu') and password == 'alumnipass':
            session['user_type'] = 'alumni'
            session['email'] = email
            flash('Welcome back to Alumni Portal!', 'success')
            return redirect(url_for('alumni_dashboard'))
        else:
            flash('Invalid alumni credentials!', 'danger')
    return render_template('alumni_login.html', form=form)

@app.route('/admin-dashboard')
def admin_dashboard():
    if not session.get('user_type') == 'admin':
        flash('Please login as an admin to access this page.', 'danger')
        return redirect(url_for('admin_login'))
    return render_template('admin_dashboard.html')

@app.route('/alumni-dashboard')
def alumni_dashboard():
    if not session.get('user_type') == 'alumni':
        flash('Please login as an alumni to access this page.', 'danger')
        return redirect(url_for('alumni_login'))
    return render_template('alumni_dashboard.html')

@app.route('/alumni-directory')
def alumni_directory():
    return render_template('alumni_directory.html')

@app.route('/alumni-events')
def alumni_events():
    return render_template('alumni_events.html')

@app.route('/manage-users')
def manage_users():
    if not session.get('user_type') == 'admin':
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('admin_login'))
    return render_template('manage_users.html')

@app.route('/manage-events')
def manage_events():
    if not session.get('user_type') == 'admin':
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('admin_login'))
    return render_template('manage_events.html')

@app.route('/profile')
def profile():
    if not session.get('user_type'):
        flash('Please login to access your profile.', 'danger')
        return redirect(url_for('alumni_login'))
    return render_template('profile.html')

@app.route('/events')
def events():
    if not session.get('user_type'):
        flash('Please login to view events.', 'danger')
        return redirect(url_for('alumni_login'))
    return render_template('events.html')

@app.route('/alumni-network')
def alumni_network():
    if not session.get('user_type') == 'alumni':
        flash('Please login as an alumni to access the network.', 'danger')
        return redirect(url_for('alumni_login'))
    return render_template('alumni_network.html')

@app.route('/job-board')
def job_board():
    if not session.get('user_type') == 'alumni':
        flash('Please login as an alumni to access the job board.', 'danger')
        return redirect(url_for('alumni_login'))
    return render_template('job_board.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully!', 'success')
    return redirect(url_for('alumni_login'))

if __name__ == '__main__':
    app.run(debug=True)
