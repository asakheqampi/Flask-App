# Name Submission App

## Project Overview
A simple web application where users can input their names to receive a personalized greeting. The app demonstrates form handling, data validation, and dynamic error messages using Flask.

## Features
- Input form for user names.
- Validation to ensure names contain only alphabetic characters.
- Dynamic error messages for invalid inputs.
- Personalized greeting on valid submission.
- Responsive design with basic CSS.

## Technology Stack
- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Tools**: Ngrok (for public URL testing)

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone <repository_url>

Navigate to the project directory:
cd flask_project
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

Install the required dependencies:
pip install flask

Run the application:
python app.py
Use Ngrok to expose the app (if needed):
ngrok http 5000

Usage
Open the app in your browser.
Enter a valid name and click "Submit" to receive a personalized greeting.
If an invalid name is entered, an error message will guide the user to input a valid name.

File Structure
flask_project/
│
├── static/
│   └── styles.css
├── templates/
│   ├── greet.html
│   └── home.html
├── app.py
└── requirements.txt

Key Code Highlights

Form Validation:

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', '').strip()
    if not name.isalpha():
        error = "Name must contain only letters. Please try again."
        return render_template('home.html', error=error)
    return render_template('greet.html', name=name)

Dynamic Error Handling in HTML:
{% if error %}
    <p style="color: red;">{{ error }}</p>
{% endif %}

Testing
Valid inputs: "John", "Alice".
Invalid inputs: "123", "@John", "", spaces.
Checked for error messages and correct redirection.

Lessons Learned
Flask form handling and validation.
Debugging and refining code iteratively.
Testing with valid and invalid inputs.

Future Improvements
Add a database to store submitted names.
Enhance CSS for a modern look.
Extend validation to allow names with spaces (e.g., "Mary Jane").

---






