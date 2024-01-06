from openai import OpenAI
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_wallpaper():
    # Retrieve user preferences from the form submission
    user_preferences = request.form
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


open_ai_api_key = os.getenv('OPEN_AI_API_KEY')
client = OpenAI(api_key=open_ai_api_key)

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url