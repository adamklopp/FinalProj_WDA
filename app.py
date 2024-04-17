import os
from flask import Flask, render_template, request, jsonify
import sqlite3
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# The index route where users can submit lyrics and receive song details.
@app.route("/", methods=("GET", "POST"))
def index():
    song_info = None
    if request.method == "POST":
        lyrics = request.form["lyrics"]
        
        if not openai.api_key:
            print("No OpenAI API Key provided.")
            return "OpenAI API Key is missing!", 500
        
        try:
            response = openai.Completion.create(
                model="gpt-3.5-turbo", 
                prompt=f"Which song contains these lyrics? {lyrics}",
                max_tokens=150 
            )
            song_info = response.choices[0].text.strip()
        except openai.error.OpenAIError as oe:
            print(f"OpenAIError: {oe}")
            return "An error occurred while calling the OpenAI API.", 500
        
        conn = get_db_connection()
        conn.execute("INSERT INTO song_identifications (lyrics, song_info) VALUES (?, ?)",
                     (lyrics, song_info))
        conn.commit()
        conn.close()

    return render_template("index.html", song_info=song_info)