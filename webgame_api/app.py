from flask import Flask, render_template, request
from .models.models import db, User, Age, Country, Snapshot
from .parsers.overview import parse_alliance_overview

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webgame.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    
    
@app.route("/")
def dashboard():
    stats = {
        
        "users": User.query.count(),
        "ages": Age.query.count(),
        "countries": Country.query.count(),
        "snapshots": Snapshot.query.count()
        
    }
    
    active_age = Age.query.filter_by(is_active=True).first()
    
    latest_snapshot = (        
        Snapshot.query.order_by(Snapshot.created_at.desc()).limit(5).all()
    )
    
    return render_template(
        "dashboard.html", 
        stats=stats,
        active_age=active_age,
        latest_snapshots=latest_snapshot
    )

@app.route("/countries")
def countries():
    countries = Country.query.order_by(Country.number.asc()).all()
    return render_template("countries.html", countries=countries)

@app.route("/snapshots")
def snapshots():
    snapshots = (Snapshot.query.order_by(Snapshot.created_at.desc()).all())
    
    return render_template("snapshots.html", snapshots=snapshots)

@app.route("/ages")
def ages():
    ages = Age.query.order_by(Age.id.desc()).all()
    return render_template("ages.html", ages=ages)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    uploaded_filename = None
    file_preview = None
    
    parsed_overview = None
    alliance_name = None
    
    if request.method == "POST":
        uploaded_file = request.files.get("html_file") # the same like in <input name="html_file">
        
        if uploaded_file:
            uploaded_filename = uploaded_file.filename
            
            file_bytes = uploaded_file.read()
            file_text = file_bytes.decode("utf-8", errors="replace")
            
            file_preview = file_text[:1000]
            
            parsed_overview = parse_alliance_overview(file_text)
            country = parsed_overview.values()
            alliance_name = list(country)
            
    
    return render_template(
        "upload.html",
        uploaded_filename=uploaded_filename,
        file_preview=file_preview,
        alliance_name=alliance_name,
        parsed_overview=parsed_overview,
        
        )

if __name__ == '__main__':
    app.run(debug=True)