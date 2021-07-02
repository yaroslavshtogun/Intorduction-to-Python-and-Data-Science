# import Flask library and Tamplate 
from flask import Flask, render_template

app = Flask(__name__)   # Leting Flask know that HTML file is located in templates folder
                        # in the same directory as this app.py file is located

@app.route('/')         # the route decorator to specify the URL that should triger 
                        # the execution of the of the index function
# index() function simply render the first_app.html HTML file
# located in templates folder
def index():
    return render_template('first_app.html')

# We use run() function to only run the application on the server when this script is 
# directly executed by Python interpreter which we ensured using the if statement with
# __name__ == '__main__'
if __name__ == '__main__':
    app.run(debug=True)
