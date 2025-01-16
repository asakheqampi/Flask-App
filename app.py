from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'mysecretkey208'  # Replace with a secure key

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/greet', methods=['POST'])
def greet():
    # Extract the name from the form
    name = request.form.get('name', '').strip()

    # Validate the name
    if not name.isalpha():
        error = "Name must contain only letters. Please try again."
        return render_template('home.html', error=error)

    # Render the greet page for valid inputs
    return render_template('greet.html', name=name)


if __name__ == "__main__":
    app.run()
