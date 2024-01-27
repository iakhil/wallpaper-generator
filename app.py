from openai import OpenAI
import os
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image 
import requests 
from io import BytesIO

app = Flask(__name__)


def resize_image(image_url):
    response = requests.get(image_url)
    with Image.open(BytesIO(response.content)) as img:
        new_size = (1080, 2400)
        image_url = img.resize(new_size)
        print(image_url)
        return image_url


def create_wallpaper(user_preferences):
    open_ai_api_key = os.getenv('OPEN_AI_API_KEY')
    client = OpenAI(api_key=open_ai_api_key)
    theme = user_preferences['theme']
    color = user_preferences['color']
    additional = user_preferences['additional']
    response = client.images.generate(
    model="dall-e-2",
    prompt=f"Generate a ultra high-quality wallpaper image of the theme {theme} in the color of {color} with the presence of {additional}. Make the image appear picturesque and alluring.",
    size="1024x1024",
    quality="standard",
    n=1,
    )
    image_url = response.data[0].url
    return image_url



@app.route('/')
def index():
    image_url = request.args.get('image_url')
    return render_template('index.html', image_url=image_url)

@app.route('/generate', methods=['POST'])
def generate_wallpaper():
    # Retrieve user preferences from the form submission
    user_preferences = request.form
    image_url = create_wallpaper(user_preferences)
    return redirect(url_for('index', image_url=image_url))

if __name__ == '__main__':
    app.run(debug=True)

