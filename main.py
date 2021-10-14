import flask
import requests
# import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    response = requests.get("https://www.scorebat.com/video-api/v3/")
    if response.status_code != 200:
        return {"message": f"The upstream service has responded with the following error: {response.reason}"}
    else:
        return response.json()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
