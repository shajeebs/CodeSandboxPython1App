from flask import Flask

# Create the app.
app = Flask(__name__)

# Define the factorial function.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Define the index route.
@app.route("/")
def index():
    return """
    <html>
    <head>
        <title>Factorial Calculator</title>
    </head>
    <body>
        <form action="/factorial" method="post">
            <input type="number" name="number" placeholder="Enter a number">
            <input type="submit" value="Calculate">
        </form>
    </body>
    </html>
    """

# Define the factorial route.
@app.route("/factorial", methods=["POST"])
def factorial():
    # Get the number from the form.
    number = request.form["number"]

    # Calculate the factorial.
    factorial = factorial(int(number))

    # Return the factorial.
    return str(factorial)

# Run the app.
if __name__ == "__main__":
    app.run(debug=True)
