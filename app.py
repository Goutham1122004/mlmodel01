# app.py
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve user input from the form
        features = [float(x) for x in request.form.values()]

        # Generate a random house price based on input features (for demonstration purposes)
        prediction = np.random.randint(50000, 500000)

        # Display the predicted price
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
