# QuizzlerApp

## Description
QuizzlerApp is a Python-based quiz application that leverages Object-Oriented Programming (OOP) principles and a graphical user interface (GUI) built with Tkinter. The application fetches questions from the Open Trivia Database (OTDB) and presents them to the user in a True/False format. Users can interact with the app, answer questions, and track their scores.

## Features
- **Dynamic Question Fetching:** Questions are fetched in real-time from the Open Trivia Database API.
- **OOP Structure:** The app is built using classes and objects, making it modular and easy to extend.
- **GUI Interface:** A user-friendly GUI built with Tkinter.
- **Scoring System:** Keeps track of the user's score throughout the quiz.

## Files Overview
- **main.py:** The main entry point for the application. Initializes the quiz and UI.
- **quiz_brain.py:** Contains the logic for fetching questions, tracking the score, and validating answers.
- **ui.py:** Manages the graphical user interface using Tkinter.
- **question_model.py:** A class to represent each question, holding the question text and the correct answer.
- **data.py:** Fetches questions from the OTDB API.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/QuizzlerApp.git
   cd QuizzlerApp
