# Real-Time Chatbot with Flask and OpenAI

## Overview

This project is a real-time chatbot application built using Flask, Flask-SocketIO, and OpenAI's GPT-3.5-turbo. The application allows users to interact with a chatbot that generates responses based on OpenAI's language model. It uses WebSockets for real-time communication and SQLAlchemy for database interactions.


## Features

- Real-time messaging using WebSockets.
- Integration with OpenAI's GPT-3.5-turbo model for generating chatbot responses.
- Persistent storage of user and message data using SQLAlchemy and SQLite.
- Simple web interface for interacting with the chatbot.


## Requirements

- Python 3.6 or higher
- Flask
- Flask-SocketIO
- Flask-SQLAlchemy
- OpenAI Python client


## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/real-time-chatbot.git
    cd real-time-chatbot
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key:**

    - Replace `'your-api-key'` in `ChatApp.py` with your actual OpenAI API key.


## Configuration

The `ChatApp.py` file contains the main application configuration. Ensure you have set your OpenAI API key correctly:

```python
import openai

# Configure your OpenAI API key
openai.api_key = 'your-api-key'
```


## Running the Application

### Start the Flask application:
python app.py

### Open your browser and navigate to:
http://127.0.0.1:5000


## Acknowledgements

- Flask - A lightweight WSGI web application framework.
- Flask-SocketIO - Socket.IO integration for Flask applications.
- SQLAlchemy - SQL toolkit and Object-Relational Mapping (ORM) library.
- OpenAI - Provider of the GPT-3.5-turbo language model.



