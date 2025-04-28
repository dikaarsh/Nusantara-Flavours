
from flask import Blueprint, request, jsonify
from models import User
from extensions import db

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/', methods=['POST'])
def create_user():
    data = request.json
    user = User(nama=data['nama'], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

@user_blueprint.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'user_id': u.user_id, 'nama': u.nama, 'email': u.email} for u in users])
