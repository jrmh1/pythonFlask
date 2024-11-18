from flask import Flask

app = Flask(__name__)

# Root URL route
@app.route('/')
def home():
    return "Welcome to the Homepage!"


# About page route
@app.route('/about')
def about():
    return "This is the About Page."

# Contact page route
@app.route('/contact')
def contact():
    return "This is the Contact Page."

# Dynamic route with variable
@app.route('/user/<username>')
def show_user_profile(username):
    # Show the user profile for the given username
    return f'User: {username}'

if __name__ == '__main__':
    app.run(debug=True)
