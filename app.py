from flask import Flask, render_template
from extensions import db
from routes.user_routes import user_blueprint
from routes.resep_routes import resep_blueprint
from routes.favorit_routes import favorit_blueprint
from routes.pencarian_routes import pencarian_blueprint

app = Flask(__name__)

# Konfigurasi Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Register Blueprints
app.register_blueprint(user_blueprint)
app.register_blueprint(resep_blueprint)
app.register_blueprint(favorit_blueprint)
app.register_blueprint(pencarian_blueprint)


@app.route('/')
def home():
    return render_template('index.html')
