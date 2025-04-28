from flask import Flask, render_template
from extensions import db
from models import User  # Pastikan models.py kamu ada dan User sudah didefinisikan
import os

app = Flask(__name__)
# Setting koneksi ke SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Route utama
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

# Optional: Route API kalau mau json-an
@app.route('/api/users')
def get_users():
    users = User.query.all()
    return {
        "users": [
            {
                "id": user.user_id,
                "name": user.nama,
                "email": user.email
            } for user in users
        ]
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
