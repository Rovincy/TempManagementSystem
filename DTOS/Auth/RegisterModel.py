from flask import Flask, request, render_template, redirect
import mysql.connector

class RegisterModel:
    def __init__(self, username, email, password, confirm_password, phone_number):
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.phone_number = phone_number
        
    app = Flask(__name__)

    # MySQL database connection
    db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
    cursor = db.cursor()

    # Route for the registration page
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            # Extract data from the registration form
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
        
             # Check if the username or email already exists in the database
            query = "SELECT * FROM clients WHERE username = %s OR email = %s"
            cursor.execute(query, (username, email))
            existing_client = cursor.fetchone()

        if existing_client:
            # If username or email already exists, render the registration page with an error message
            return render_template('register.html', error='Username or email already exists')
        else:
            # Insert the new client into the database
            insert_query = "INSERT INTO clients (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (username, email, password))
            db.commit()
            
            # Redirect the client to the login page after successful registration
            return redirect('/login')
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

