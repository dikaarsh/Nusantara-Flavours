
from extensions import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Resep(db.Model):
    resep_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    nama_resep = db.Column(db.String(100))
    kategori = db.Column(db.String(100))
    nama_daerah = db.Column(db.String(100))
    bahan = db.Column(db.Text)
    instruksi = db.Column(db.Text)
    foto = db.Column(db.String(200))

class Favorit(db.Model):
    favorit_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    resep_id = db.Column(db.Integer, db.ForeignKey('resep.resep_id'))

class Pencarian(db.Model):
    pencarian_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    kata_kunci = db.Column(db.String(100))
    waktu_pencarian = db.Column(db.DateTime)
