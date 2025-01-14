from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'  # Needed for flash messages

@app.route('/')
def index():
    return render_template('index.html', message="Welcome to the Flask App!")

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')

    if not name or not name.isalpha():
        flash('Invalid name! Please enter alphabetic characters only.', 'error')
        return render_template('index.html')

    return render_template('greet.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)