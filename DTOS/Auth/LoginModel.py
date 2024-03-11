class LoginModel():
    def __init__(self, username, password):
        self.username = username
        self.password = password


# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password match
        query = "SELECT * FROM administrators WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        admin = cursor.fetchone()

        if admin:
            # If login successful, store admin ID in session
            session['admin_id'] = admin[0]
            return redirect('/dashboard')
        else:
            # If login failed, redirect back to login page with an error message
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

# Route for the dashboard page
@app.route('/dashboard')
def dashboard():
    # Check if admin is logged in
    if 'admin_id' in session:
        return render_template('dashboard.html')
    else:
        # If not logged in, redirect to login page
        return redirect('/login')

# Route for logging out
@app.route('/logout')
def logout():
    # Remove admin ID from session
    session.pop('admin_id', None)
    return redirect('/login')