"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    wants_game = request.args.get("yes_game")
    not_playing = request.args.get("no_game")
    
    if wants_game:
        return render_template("game.html")

    if not_playing:
        return render_template("goodbye.html")
    
@app.routes('/madlib')
def show_madlib():
    return render_template("madlib.html")

""" if wants_compliments:

    player = request.args.get("person")
    wants_compliments = request.args.get("wants_compliments")
    
        nice_things = sample(COMPLIMENTS, 3)
    else:
        nice_things = []
    return render_template("compliments.html",
                           compliments=nice_things, name=player)"""
if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
