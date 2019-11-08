from flask import Flask, render_template, request 


app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')

@app.route('/fortune')
def fortune_form():
    """Renders the fortune form page."""
    return render_template('fortune_form.html')


@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_favorite_vehicle = request.args.get('vehicle')
    # ... etc

    if users_favorite_vehicle == 'Bike':
        # fortune is "You'll have a magical day!"
        fortune = "You will have an additional $9,000 at the end of the year in Savings!"
    elif users_favorite_vehicle == "Car":
        # fortune is ...
        fortune = "Your abilites will astonish you. They will yield a variety of blessings in monetary value, friendships, good spirits and postive vibes. Your love life will be joyful and fulfilling."
    elif users_favorite_vehicle == "Boat":
        # fortune is ...
        fortune = "You will make moves beyond your imagination. It will take you to the hills. You will look down and recgonize your gifts of joy and friendship."
    # elif users_favorite_vehicle == "Subaru":
    #     # fortune is ...
    #     fortune = "You will go on and lead the most amazing adventures. Field with majestic beauty. Even in times when you are down, you will be supported with joy and fulfillment"
    else:
        # no other fortune applies, return default fortune
        fortune = "Just keep breathing, you will get their eventually"

    return render_template ('fortune_results.html', fortune=fortune)