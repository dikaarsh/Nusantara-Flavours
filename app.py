
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
import os
from extensions import db
from routes.user_routes import user_blueprint
from routes.resep_routes import resep_blueprint
from routes.favorit_routes import favorit_blueprint
from routes.pencarian_routes import pencarian_blueprint
from models import Resep, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB max upload
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

import models

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(resep_blueprint, url_prefix='/reseps')
app.register_blueprint(favorit_blueprint, url_prefix='/favorits')
app.register_blueprint(pencarian_blueprint, url_prefix='/pencarians')

@app.route('/')
def beranda():
    return render_template('beranda.html')

@app.route('/kategori')
def kategori():
    return render_template('kategori.html')

@app.route('/favorit')
@login_required
def favorit():
    return render_template('favorit.html')

@app.route('/resep/<int:id>')
def detail_resep(id):
    resep = Resep.query.get(id)
    return render_template('detail_resep.html', resep=resep)

@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    if query:
        reseps = Resep.query.filter(Resep.nama_resep.ilike(f'%{query}%')).all()
        results = [{'id': r.resep_id, 'nama_resep': r.nama_resep, 'nama_daerah': r.nama_daerah} for r in reseps]
    else:
        results = []
    return jsonify(results)

@app.route('/filter_kategori')
def filter_kategori():
    provinsi = request.args.get('provinsi', '')
    reseps = Resep.query.filter(Resep.kategori.ilike(f'%{provinsi}%')).all()
    results = [{'id': r.resep_id, 'nama_resep': r.nama_resep, 'nama_daerah': r.nama_daerah} for r in reseps]
    return jsonify(results)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('beranda'))
        else:
            flash('Email atau Password salah')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        password = request.form['password']
        if User.query.filter_by(email=email).first():
            flash('Email sudah terdaftar')
        else:
            new_user = User(nama=nama, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Pendaftaran berhasil, silakan login.')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('beranda'))

@app.route('/tambah_resep', methods=['GET', 'POST'])
@login_required
def tambah_resep():
    if request.method == 'POST':
        nama_resep = request.form['nama_resep']
        kategori = request.form['kategori']
        nama_daerah = request.form['nama_daerah']
        bahan = request.form['bahan']
        instruksi = request.form['instruksi']
        foto_file = request.files['foto']
        filename = None
        if foto_file:
            filename = secure_filename(foto_file.filename)
            foto_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            foto_file.save(foto_path)
        resep = Resep(
            user_id=current_user.user_id,
            nama_resep=nama_resep,
            kategori=kategori,
            nama_daerah=nama_daerah,
            bahan=bahan,
            instruksi=instruksi,
            foto=filename
        )
        db.session.add(resep)
        db.session.commit()
        flash('Resep berhasil ditambahkan!')
        return redirect(url_for('beranda'))
    return render_template('tambah_resep.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
