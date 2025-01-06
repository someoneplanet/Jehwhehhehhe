from flask import Flask, request, jsonify
from gtts import gTTS
import random
import os

app = Flask(__name__)

# Directory to save the audio files
AUDIO_DIR = "/tmp/audio"  # Use /tmp for serverless functions

if not os.path.exists(AUDIO_DIR):
    os.makedirs(AUDIO_DIR)

# Function to simulate training by saving audio file
def train_voice(audio_file):
    # Placeholder for actual training logic
    print(f"Training with {audio_file}")
    # In practice, here you'd process the audio for training

@app.route('/speak', methods=['POST'])
def speak():
    text = request.json.get('text')
    language = 'en'
    tts = gTTS(text=text, lang=language)
    filename = f"{AUDIO_DIR}/audio_{random.randint(1000, 9999)}.mp3"
    tts.save(filename)
    return jsonify({'audio_url': f'/audio/{filename.split("/")[-1]}'})

@app.route('/train', methods=['POST'])
def train():
    audio_file = request.json.get('audio_file')
    if audio_file:
        train_voice(audio_file)
        return jsonify({'status': 'Training started'})
    return jsonify({'status': 'No audio file provided'}), 400

@app.route('/test', methods=['GET'])
def test():
    test_text = "This is a test message from the Scout voice AI!"
    tts = gTTS(text=test_text, lang='en')
    filename = f"{AUDIO_DIR}/test_audio.mp3"
    tts.save(filename)
    return jsonify({'audio_url': f'/audio/{filename.split("/")[-1]}'})

if __name__ == "__main__":
    app.run(debug=True)
