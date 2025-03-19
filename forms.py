from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField, EmailField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
class LoginForm(FlaskForm):
    user_type = SelectField('User Type', choices=[('admin', 'Admin'), ('alumni', 'Alumni')], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')  # Added Remember Me checkbox
    submit = SubmitField('Login')

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Register')


class EventForm(FlaskForm):
    title = StringField('Event Title', validators=[DataRequired()])
    description = TextAreaField('Event Description', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Create Event')

class EmailForm(FlaskForm):
    recipient = EmailField('Recipient Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Email')


class ProfileForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    bio = TextAreaField('Bio')
    location = StringField('Location')
    submit = SubmitField('Update Profile')

class JobPostingForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    company = StringField('Company Name', validators=[DataRequired()])
    description = TextAreaField('Job Description', validators=[DataRequired()])
    salary = FloatField('Salary')
    submit = SubmitField('Post Job')


class MentorshipForm(FlaskForm):
    mentor_name = StringField('Mentor Name', validators=[DataRequired()])
    expertise = StringField('Expertise', validators=[DataRequired()])
    availability = StringField('Availability', validators=[DataRequired()])
    submit = SubmitField('Apply for Mentorship')

class DonationForm(FlaskForm):
    donor_name = StringField('Donor Name', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    message = TextAreaField('Message')
    submit = SubmitField('Donate')

class SettingsForm(FlaskForm):
    notification_preferences = SelectField('Notifications', choices=[('email', 'Email'), ('sms', 'SMS'), ('none', 'None')], validators=[DataRequired()])
    privacy_level = SelectField('Privacy Level', choices=[('public', 'Public'), ('private', 'Private')], validators=[DataRequired()])
    submit = SubmitField('Save Settings')

