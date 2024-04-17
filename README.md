# Song Identifier

## Overview
Song Identifier is a web app built off of the Snaptutor app. My app is designed to help users find the name and artist of a song from a snippet of its lyrics. Based on the Flask framework and leveraging Generative AI, it offers a user-friendly interface where users can input lyrics and receive the corresponding song information.

## File Structure
- `app.py`: The Flask application's main file with routes and logic for song identification.
- `database.db`: A SQLite database that stores user queries and the identified songs.
- `requirements.txt`: Lists the Python dependencies required to run the application.
- `schema.sql`: SQL schema definitions for initializing the database tables.
- `static/`: Contains static files such as stylesheets and images.
  - `main.css`: Defines the app's styling, with a black and green color theme.
- `templates/`: Holds HTML templates for rendering views.
  - `index.html`: The main HTML template for user interaction.
- `LICENSE`: The project's license document.

## Problem
Remembering only fragments of song lyrics and struggling to identify the song is a common issue. Search engines may not provide accurate results for incomplete or non-unique lyrics.

## Solution
The app offers a straightforward interface for inputting lyrics and retrieving song names and artists. It uses a Generative AI model through the OpenAI API to analyze the lyrics and find the best match, offering an efficient and user-friendly solution.

## How It Works
Users enter lyrics into the web interface. `app.py` processes the input using the Generative AI model from OpenAI. The predicted song title and artist are then displayed to the user. All submissions are stored in `database.db`, which can help improve the model's performance over time.

## Launching the App
To get the Song Identifier app up and running on your local system, perform the following steps:

1. Clone the repository to your machine.
2. Change to the project directory.
3. In the .env file enter your "OPENAI_API_KEY"
4. Create a virtual environment with `python3 -m venv venv`.
5. Activate the virtual environment:
      Use `source venv/bin/activate`
6. Install the necessary dependencies with `pip install -r requirements.txt`.
7. Set the Flask app environment variable with `export FLASK_APP=app.py` 
8. (Optional) Set the Flask environment to development for debugging purposes with `export FLASK_ENV=development` 
9. Launch the app with `flask run`. The app will be available at `http://localhost:5000`.
