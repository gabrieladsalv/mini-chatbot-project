from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from config import Config
import openai


openai.api_key = 'your-openai-api-key'

class ChatApp:
    def __init__(self):
        
        self.app = Flask(__name__, template_folder='src/templates')
        self.app.config.from_object(Config)
        self.socketio = SocketIO(self.app)
        self.db = SQLAlchemy(self.app)

        
        with self.app.app_context():
            self.setup_database()

        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.socketio.on('message')
        def handle_message(message):
            print('Received message:', message)
            response = self.get_openai_response(message)
            emit('response', response)

    def setup_database(self):
        
        class User(self.db.Model):
            id = self.db.Column(self.db.Integer, primary_key=True)
            username = self.db.Column(self.db.String(80), unique=True, nullable=False)
            messages = self.db.relationship('Message', backref='user', lazy=True)

        class Message(self.db.Model):
            id = self.db.Column(self.db.Integer, primary_key=True)
            content = self.db.Column(self.db.String(200), nullable=False)
            user_id = self.db.Column(self.db.Integer, self.db.ForeignKey('user.id'), nullable=False)

        
        self.db.create_all()

    def get_openai_response(self, prompt):
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=prompt,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return str(e)

    def run(self):
        
        self.socketio.run(self.app, debug=True)
