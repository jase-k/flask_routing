from flask import Flask  # Import Flask to allow us to create our app
from flask import render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


# @app.route('/') #return a page to choose routes
# def pick_route():
#     return render_template("/index.html")
@app.errorhandler(404)
def throw_error(e):
    return "Sorry, No response! Try Again!", 404 

@app.route('/hello')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "You are a DOJO!"
# Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
@app.route('/repeat/<int:num>/<string:phrase>')
def repeat(num, phrase):
    return phrase * int(num)

@app.route('/say/<string:name>')
def hello(name):
    return f"Hi {name}!"
    
@app.route('/success')
def success():
    return "success"
    # app.run(debug=True) should be the very last statement! 

@app.route('/users/<string:username>/<int:id>')
def display_user_info(username, id):
    print(username)
    print(id)
    return f"Your Action is completes"




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

