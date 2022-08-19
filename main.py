from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    r = requests.get(url="https://api.3geonames.org/?randomland=FR&json=1")
    json = r.json()
    city = json['nearest']['city']
    return f"""
    <!doctype HTML>
    <head>
    </head>
    <h1>Trouve ton daron !</h1>
    <p>
    Sur ce site nous donnons l'emplacement de ton papa parti cherché du lait en temps réel !
    </p>
    <p>Ton papa se situe actuellement à : </p>
    <br>
    <b>{city}</b>
    <h5>made with love by yazz</h5>
    
    """

if __name__ == '__main__':
    app.run()
