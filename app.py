from flask import Flask, render_template, redirect, url_for, flash, session
from forms import RegistrationForm, LoginForm
from forms import UserForm, EventForm, EmailForm, ProfileForm, JobPostingForm, MentorshipForm, DonationForm, SettingsForm
from flask import request
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
        flash('Account created successfully!', 'success')
        return redirect(url_for('alumni_login'))  # Redirect to alumni login after successful registration
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

@app.route('/manage-users', methods=['GET', 'POST'])
def manage_users():
    if not session.get('user_type') == 'admin':
        flash('Please login as an admin to access this page.', 'danger')
        return redirect(url_for('admin_login'))
    
    form = UserForm()
    if form.validate_on_submit():
        # Logic to add or update user
        flash('User updated successfully!', 'success')
        return redirect(url_for('manage_users'))
        
    # Mock user data - in a real app, you'd fetch from database
    users = [
        {'id': 1, 'name': 'John Doe', 'email': 'john@alumni.sju.edu', 'graduation_year': 2020, 'status': 'Active'},
        {'id': 2, 'name': 'Jane Smith', 'email': 'jane@alumni.sju.edu', 'graduation_year': 2019, 'status': 'Pending'},
        {'id': 3, 'name': 'Bob Johnson', 'email': 'bob@alumni.sju.edu', 'graduation_year': 2021, 'status': 'Active'}
    ]
    
    return render_template('admin_d_manageusers.html', users=users, form=form)

@app.route('/manage-events', methods=['GET', 'POST'])
def manage_events():
    if not session.get('user_type') == 'admin':
        flash('Please login as an admin to access this page.', 'danger')
        return redirect(url_for('admin_login'))
    
    form = EventForm()
    if form.validate_on_submit():
        # Logic to add or update event
        flash('Event added successfully!', 'success')
        return redirect(url_for('manage_events'))
    
    # Mock event data
    events = [
        {'id': 1, 'title': 'Annual Alumni Meet 2025', 'date': '2025-05-15', 'location': 'Main Campus', 'attendees': 120},
        {'id': 2, 'title': 'Career Fair', 'date': '2025-03-10', 'location': 'Student Center', 'attendees': 250},
        {'id': 3, 'title': 'Networking Dinner', 'date': '2025-04-22', 'location': 'Downtown Hotel', 'attendees': 85}
    ]
    
    return render_template('admin_d_manageevents.html', events=events, form=form)

@app.route('/reports-analytics')
def reports_analytics():
    if not session.get('user_type') == 'admin':
        flash('Please login as an admin to access this page.', 'danger')
        return redirect(url_for('admin_login'))
    
    # Mock analytics data
    analytics = {
        'total_alumni': 1234,
        'active_users': 892,
        'events_this_year': 15,
        'total_event_attendees': 3450,
        'new_registrations_month': 42,
        'graduation_years': {
            '2020-2025': 450,
            '2015-2019': 380,
            '2010-2014': 215,
            'Before 2010': 189
        },
        'engagement_rate': 72
    }
    
    return render_template('admin_d_reports&analytics.html', analytics=analytics)

@app.route('/email-communications', methods=['GET', 'POST'])
def email_communications():
    if not session.get('user_type') == 'admin':
        flash('Please login as an admin to access this page.', 'danger')
        return redirect(url_for('admin_login'))
    
    form = EmailForm()
    if form.validate_on_submit():
        # Logic to send or schedule email
        flash('Email campaign scheduled successfully!', 'success')
        return redirect(url_for('email_communications'))
    
    # Mock email templates and campaigns
    templates = [
        {'id': 1, 'name': 'Welcome Template', 'subject': 'Welcome to SJU Alumni Network'},
        {'id': 2, 'name': 'Event Invitation', 'subject': 'You\'re Invited: {{event_name}}'},
        {'id': 3, 'name': 'Newsletter', 'subject': 'SJU Alumni Monthly Newsletter'}
    ]
    
    campaigns = [
        {'id': 1, 'name': 'March Newsletter', 'sent_to': 892, 'date': '2025-03-01', 'open_rate': '68%'},
        {'id': 2, 'name': 'Alumni Meet Invitation', 'sent_to': 1200, 'date': '2025-02-15', 'open_rate': '75%'}
    ]
    
    return render_template('admin_d_emailcommuincations.html', templates=templates, campaigns=campaigns, form=form)

@app.route('/system-settings', methods=['GET', 'POST'])
def system_settings():
    if not session.get('user_type') == 'admin':
        flash('Please login as an admin to access this page.', 'danger')
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        # Logic to update settings
        flash('System settings updated successfully!', 'success')
        return redirect(url_for('system_settings'))
    
    # Mock settings
    settings = {
        'site_name': 'SJU Alumni Portal',
        'admin_email': 'admin@sju.edu',
        'approval_required': True,
        'allow_job_postings': True,
        'enable_newsletter': True,
        'maintenance_mode': False
    }
    
    return render_template('admin_d_systemsettings.html', settings=settings)

@app.route('/logout')
def logout():
    session.clear()  # Clears user session
    return redirect(url_for('logout_page'))  # Redirects to logout confirmation page

@app.route('/logout_page')
def logout_page():
    return render_template('admin_d_logout.html')  # Shows logout confirmation

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if not session.get('user_type') == 'alumni':
        flash('Please login as an alumni to access this page.', 'danger')
        return redirect(url_for('alumni_login'))
    
    form = ProfileForm()
    if form.validate_on_submit():
        # Logic to update profile
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))
    
    # Mock profile data
    profile_data = {
        'name': 'John Doe',
        'email': session.get('email', ''),
        'graduation_year': '2020',
        'major': 'Information Technology',
        'current_position': 'Senior Software Developer',
        'company': 'Tech Solutions Inc.',
        'location': 'New York, NY',
        'bio': 'Experienced software developer with a passion for creating innovative solutions.',
        'skills': ['Python', 'JavaScript', 'React', 'AWS', 'Database Design'],
        'linkedin': 'linkedin.com/in/johndoe',
        'twitter': '@johndoe',
        'profile_picture': 'profile1.jpg'
    }
    
    return render_template('alumni_d_profile.html', profile=profile_data, form=form)

@app.route('/events')
def events():
    if not session.get('user_type') == 'alumni':
        flash('Please login as an alumni to access this page.', 'danger')
        return redirect(url_for('alumni_login'))
    
    # Mock events data
    upcoming_events = [
        {'id': 1, 'title': 'Annual IT Alumni Meet', 'date': 'March 15, 2025', 'location': 'Main Campus', 'description': 'Join us for our annual IT department alumni gathering.', 'registered': True},
        {'id': 2, 'title': 'Tech Talk Series', 'date': 'April 2, 2025', 'location': 'Virtual Event', 'description': 'Learn about the latest in AI and machine learning.', 'registered': False},
        {'id': 3, 'title': 'Career Networking Night', 'date': 'April 20, 2025', 'location': 'Downtown Conference Center', 'description': 'Connect with employers and fellow alumni.', 'registered': True},
        {'id': 4, 'title': 'Homecoming Weekend', 'date': 'May 5-7, 2025', 'location': 'University Campus', 'description': 'Annual homecoming celebration with various activities.', 'registered': False}
    ]
    
    past_events = [
        {'id': 5, 'title': 'Winter Alumni Gala', 'date': 'December 10, 2024', 'location': 'Grand Hotel', 'description': 'Annual winter celebration for all alumni.'},
        {'id': 6, 'title': 'Industry Expert Panel', 'date': 'February 15, 2025', 'location': 'Business School Auditorium', 'description': 'Panel discussion with industry leaders.'}
    ]
    
    return render_template('alumni_d_events.html', upcoming_events=upcoming_events, past_events=past_events)

@app.route('/register-event/<int:event_id>', methods=['POST'])
def register_event(event_id):
    if not session.get('user_type') == 'alumni':
        flash('Please login as an alumni to access this page.', 'danger')
        return redirect(url_for('alumni_login'))
    
    # Logic to register for an event
    flash(f'Successfully registered for event #{event_id}!', 'success')
    return redirect(url_for('events'))

@app.route('/network')
def network():
    if not session.get('user_type') == 'alumni':
        flash('Please login as an alumni to access this page.', 'danger')
        return redirect(url_for('alumni_login'))
    
    # Mock alumni network data
    alumni = [
        {'id': 1, 'name': 'Sarah Johnson', 'graduation_year': '2019', 'major': 'Computer Science', 'current_position': 'Software Engineer', 'company': 'Google', 'connected': True},
        {'id': 2, 'name': 'Michael Chen', 'graduation_year': '2018', 'major': 'Information Technology', 'current_position': 'IT Manager', 'company': 'Amazon', 'connected': True},
        {'id': 3, 'name': 'Emily Rodriguez', 'graduation_year': '2020', 'major': 'Information Systems', 'current_position': 'Data Analyst', 'company': 'Microsoft', 'connected': False},
        {'id': 4, 'name': 'David Kim', 'graduation_year': '2021', 'major': 'Computer Science', 'current_position': 'Web Developer', 'company': 'Facebook', 'connected': False},
        {'id': 5, 'name': 'Lisa Patel', 'graduation_year': '2017', 'major': 'Information Technology', 'current_position': 'Cybersecurity Specialist', 'company': 'IBM', 'connected': True}
    ]
    
    connections = [alumni[0], alumni[1], alumni[4]]  # Pre-connected alumni
    
    return render_template('alumni_d_network.html', alumni=alumni, connections=connections)

@app.route('/connect/<int:alumni_id>', methods=['POST'])
def connect(alumni_id):
    if not session.get('user_type') == 'alumni':
        flash('Please login as an alumni to access this page.', 'danger')
        return redirect(url_for('alumni_login'))
    
    # Logic to connect with another alumni
    flash(f'Connection request sent to alumni #{alumni_id}!', 'success')
    return redirect(url_for('network'))

@app.route('/jobs', methods=['GET', 'POST'])
def jobs():
    if not session.get('user_type') == 'alumni':
        flash('Please login as an alumni to access this page.', 'danger')
        return redirect(url_for('alumni_login'))
    
    form = JobPostingForm()
    if form.validate_on_submit():
        # Logic to post a new job
        flash('Job posting created successfully!', 'success')
        return redirect(url_for('jobs'))
    
    # Mock job listings
    job_listings = [
        {'id': 1, 'title': 'Senior Software Developer', 'company': 'Tech Solutions Inc.', 'location': 'New York, NY', 'posted_date': 'March 1, 2025', 'description': 'Looking for an experienced developer...', 'posted_by': 'Sarah Johnson (Class of 2019)'},
        {'id': 2, 'title': 'Product Manager', 'company': 'Innovate Corp', 'location': 'San Francisco, CA', 'posted_date': 'March 5, 2025', 'description': 'Seeking a product manager with 3+ years experience...', 'posted_by': 'Michael Chen (Class of 2018)'},
        {'id': 3, 'title': 'Data Scientist', 'company': 'Analytics Partners', 'location': 'Boston, MA', 'posted_date': 'March 7, 2025', 'description': 'Join our data science team to work on cutting-edge projects...', 'posted_by': 'Lisa Patel (Class of 2017)'},
        {'id': 4, 'title': 'UX Designer', 'company': 'Creative Designs', 'location': 'Remote', 'posted_date': 'March 10, 2025', 'description': 'Looking for a talented UX designer to join our team...', 'posted_by': 'Emily Rodriguez (Class of 2020)'}
    ]
    
    your_job_posts = [job_listings[0]]  # Jobs posted by the current user
    
    return render_template('alumni_d_jobboard.html', job_listings=job_listings, your_job_posts=your_job_posts, form=form)

@app.route('/mentorship', methods=['GET', 'POST'])
def mentorship():
    if not session.get('user_type') == 'alumni':
        flash('Please login as an alumni to access this page.', 'danger')
        return redirect(url_for('alumni_login'))
    
    form = MentorshipForm()
    if form.validate_on_submit():
        # Logic to request mentorship or offer to be a mentor
        flash('Mentorship request submitted successfully!', 'success')
        return redirect(url_for('mentorship'))
    
    # Mock mentors and mentees data
    mentors = [
        {'id': 1, 'name': 'Sarah Johnson', 'graduation_year': '2019', 'expertise': 'Software Engineering, Machine Learning', 'availability': 'Weekly calls'},
        {'id': 2, 'name': 'Michael Chen', 'graduation_year': '2018', 'expertise': 'IT Management, Cloud Computing', 'availability': 'Monthly calls'},
        {'id': 3, 'name': 'Lisa Patel', 'graduation_year': '2017', 'expertise': 'Cybersecurity, Network Administration', 'availability': 'Bi-weekly calls'}
    ]
    
    your_mentees = [
        {'id': 1, 'name': 'Alex Thompson', 'graduation_year': '2023', 'interests': 'Web Development', 'status': 'Active'},
        {'id': 2, 'name': 'Jessica Lee', 'graduation_year': '2024', 'interests': 'Mobile App Development', 'status': 'Active'}
    ]
    
    your_mentors = [
        {'id': 1, 'name': 'Michael Chen', 'graduation_year': '2018', 'expertise': 'IT Management, Cloud Computing', 'status': 'Active'}
    ]
    
    return render_template('alumni_d_mentorship.html', mentors=mentors, your_mentees=your_mentees, your_mentors=your_mentors, form=form)

@app.route('/donations', methods=['GET', 'POST'])
def donations():
    if not session.get('user_type') == 'alumni':
        flash('Please login as an alumni to access this page.', 'danger')
        return redirect(url_for('alumni_login'))
    
    form = DonationForm()
    if form.validate_on_submit():
        # Logic to process donation
        flash('Thank you for your generous donation!', 'success')
        return redirect(url_for('donations'))
    
    # Mock donation options and history
    donation_options = [
        {'id': 1, 'name': 'Scholarship Fund', 'description': 'Support students with financial need'},
        {'id': 2, 'name': 'Technology Initiative', 'description': 'Help upgrade campus technology infrastructure'},
        {'id': 3, 'name': 'Research Grant', 'description': 'Fund innovative research projects'},
        {'id': 4, 'name': 'Campus Development', 'description': 'Contribute to new building projects'}
    ]
    
    donation_history = [
        {'date': 'January 15, 2025', 'amount': '$250', 'fund': 'Scholarship Fund'},
        {'date': 'October 10, 2024', 'amount': '$500', 'fund': 'Technology Initiative'}
    ]
    
    impact = {
        'total_raised': '$1.2M',
        'donors': 845,
        'scholarships_funded': 42
    }
    
    return render_template('alumni_d_giveback.html', donation_options=donation_options, donation_history=donation_history, impact=impact, form=form)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if not session.get('user_type') == 'alumni':
        flash('Please login as an alumni to access this page.', 'danger')
        return redirect(url_for('alumni_login'))
    
    form = SettingsForm()
    if form.validate_on_submit():
        # Logic to update settings
        flash('Settings updated successfully!', 'success')
        return redirect(url_for('settings'))
    
    # Mock user settings
    user_settings = {
        'email_notifications': True,
        'event_reminders': True,
        'job_alerts': True,
        'newsletter_subscription': True,
        'profile_visibility': 'All Alumni',
        'two_factor_auth': False
    }
    
    return render_template('alumni_d_settings.html', settings=user_settings, form=form)

@app.route('/logout')
def alogout():
    session.clear()  # Clears user session
    return redirect(url_for('logout_page'))  # Redirects to logout confirmation page

@app.route('/logout_page')
def logout_page():
    return render_template('admin_d_logout.html')  # Shows logout confirmation

if __name__ == '__main__':
    app.run(debug=True)
