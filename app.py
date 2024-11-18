from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # Data to be passed to the template
    message = "Hello from Flask with Jinja2 Templates!"
    subtitle = "Hello World!"

    # Render the template and pass the variables
    return render_template('index.html', message=message, subtitle=subtitle)


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
