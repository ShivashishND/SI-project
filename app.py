from flask import Flask, request, jsonify, Response
import requests
import constants
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = constants.SWAGGER_URL
API_URL = constants.API_URL
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "SI - Shivashish Computer Vision API's"
    }
)

app = Flask(__name__)

headers = {"Content-Type":"application/json", "Ocp-Apim-Subscription-Key":constants.SUBSCRIPTION_KEY}

@app.route('/')
def home():
    return Response('<h1>Please use one of the provided endpoints</h1><ul><li>/detect</li><li>/describe</li><li>/read_text</li></ul>')

@app.route('/describe', methods=['POST'])
def describe_image():
    data = request.json
    url = constants.AZURE_IMAGE_DESCRIBE_URL

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 400:
        return Response("Not a valid image", status=400)

    response_data = response.json()
    text_description = response_data['description']['captions'][0]['text']
    return text_description

@app.route('/detect', methods=['POST'])
def detect_image():
    data = request.json
    url = constants.AZURE_IMAGE_DETECT_URL
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 400:
        return Response("Not a valid image URL", status=400)
    
    response_data = response.json()
    objects = []

    for obj in response_data['objects']:
        objects.append(obj['object'])
    
    if not objects:
        return Response("No objects detected")

    return jsonify(objects)

@app.route('/read_text', methods=['POST'])
def read_text_from_image():
    data = request.json
    url = constants.AZURE_READ_TEXT_URL
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 400:
        return Response("Not a valid image", status=400)

    response_data = response.json()
    regions = response_data['regions']

    if not regions:
        return Response("Could not detect any text")

    lines = regions[0]['lines']
    all_words = []
    for line in lines:
        words = line['words']
        for word in words:
            all_words.append(word['text'])

    all_words = " ".join(all_words)
    return Response(all_words)

app.register_blueprint(swaggerui_blueprint)

if __name__ == "__main__":
    app.run(debug=True)