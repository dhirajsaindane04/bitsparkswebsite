from flask import render_template, request, redirect, url_for, flash
from flask import current_app as app


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/website-development')
def website_development():
    return render_template('website.html')

@app.route('/website-development')
def mobapp_development():
    return render_template('mobile.html')

@app.route('/software-development')
def software_development():
    return render_template('software.html')

@app.route('/trainings&internships')
def training_interships():
    return render_template('training.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Save to local file
        with open('contact_messages.txt', 'a') as f:
            f.write(f'Name: {name}\nEmail: {email}\nMessage: {message}\n\n')

        flash('Message sent successfully!')
        return redirect(url_for('home'))

    return render_template('contact.html')
