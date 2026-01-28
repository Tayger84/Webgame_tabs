from flask import Flask
from .models.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webgame.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    
    
@app.route("/")
def index():
    
    return "DB ready!"

if __name__ == '__main__':
    app.run(debug=True)