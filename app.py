from flask import Flask, render_template

# Maak een Flask-applicatie
app = Flask(__name__)

# Definieer een route voor de startpagina
@app.route('/')
def home():
    # Laad de HTML-template in en geef deze weer
    return render_template('Horror.html')

# Voeg meer routes toe zoals gewenst

if __name__ == '__main__':
    # Start de Flask-ontwikkelingsserver
    app.run()
