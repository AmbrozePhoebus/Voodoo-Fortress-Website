from flask import Flask

# Maak een Flask-app
app = Flask(__name__)

# Definieer een route voor de startpagina
@app.route('/')
def home():
    return 'Welkom op mijn website!'

if __name__ == '__main__':
    app.run()