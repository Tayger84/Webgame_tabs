from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    
    player_name = db.Column(db.String(120), nullable=False)
    
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    
class Age(db.Model):
    __tablename__ = "ages"
    """ Time axys of the Game """
    id = db.Column(db.Integer, primary_key=True)
    age_number = db.Column(db.String(20), nullable=False)
    start_age = db.Column(db.String(25), nullable=False)
    end_age = db.Column(db.String(25), nullable=False)
    remain_time = db.Column(db.String(30), unique=False, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    
    snapshots = db.relationship("Snapshot", backref="age", lazy=True)
    
class UserAgeState(db.Model):
    __tablename__ = "user_age_states"
    
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
        )    
    
    age_id = db.Column(
        db.Integer, 
        db.ForeignKey("ages.id"),
        nullable=False
    )

    player_name_changed = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )
    
    changed_at = db.Column(db.DateTime, nullable=True)

    __table_args__ = (
        db.UniqueConstraint("user_id", "age_id", name = "uq_user_age")
    )

class Country(db.Model):
    __tablename__ = "countries"
    """ Identity of the player country """
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False) #123
    name = db.Column(db.String(100), nullable=False) # Country name
    player = db.Column(db.String(120), nullable=False) # Player name
    alliance = db.Column(db.String(100), nullable=True) # Alliance name where the Country is
    regime = db.Column(db.String(20), nullable=True) # Type of regime sets in Country
    
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey("users.id"),
        nullable=False
    )
    
    user = db.relationship("User", backref="countries")
    
    snapshots = db.relationship('Snapshot', backref='country', lazy=True)
    
    def __repr__(self):
        return f"<Country #{self.number}{self.name}>"
    
class Snapshot(db.Model):
    """ History of a country properties """
    
    __tablename__ = "snapshots"
    id = db.Column(db.Integer, primary_key=True)
    
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    age_id = db.Column(db.Integer, db.ForeignKey('ages.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
        
    json_data = db.Column(db.JSON, nullable=False)
    
    snapshot_hash = db.Column(db.String(64), nullable=False)
    
    __table_args__ = (
        db.UniqueConstraint(
            "country_id",
            "age_id",
            "snapshot_hash",
            name = "uq_country_age_snapshot"
        ),
    )

    def __repr__(self):
        return f"<Snapshot Country ID =  {self.country_id} age_id = {self.age_id} at={self.created_at}>"    
    