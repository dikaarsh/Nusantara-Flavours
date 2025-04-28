from flask import Flask, render_template
from extensions import db
import os

def create_app():
    app = Flask(__name__)

    # Set Database Path (Aman untuk lokal & Railway)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import dan Register semua Blueprint
    from routes.user_routes import user_blueprint
    from routes.resep_routes import resep_blueprint
    from routes.favorit_routes import favorit_blueprint
    from routes.pencarian_routes import pencarian_blueprint

    app.register_blueprint(user_blueprint)
    app.register_blueprint(resep_blueprint)
    app.register_blueprint(favorit_blueprint)
    app.register_blueprint(pencarian_blueprint)

    # Route untuk Beranda
    @app.route('/')
    def home():
        return render_template('index.html')

    return app

# Inisialisasi app
app = create_app()
