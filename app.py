from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Configuration class
class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432/bitsparks'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Initialize the database
db = SQLAlchemy()

# Contact model
class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    sent_time = db.Column(db.Text, nullable=False)
    orgname = db.Column(db.String(150), nullable=True)  


# App creation function
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the app with the database
    db.init_app(app)

    # Routes
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

    @app.route('/mobapp-development')
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
            time = datetime.now()
            orgname = "Bitsparks Technologies"
            # Create a new Contact entry
            new_contact = Contact(name=name, email=email, message=message,sent_time=time, orgname=orgname)

            # Save to the database
            db.session.add(new_contact)
            db.session.commit()

            flash('Message sent successfully!')
            return redirect(url_for('home'))

        return render_template('contact.html')

    return app

# Main entry point
if __name__ == "__main__":
    app = create_app()

    # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)
