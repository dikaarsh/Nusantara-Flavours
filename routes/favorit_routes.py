
from flask import Blueprint, request, jsonify
from models import Favorit
from extensions import db

favorit_blueprint = Blueprint('favorits', __name__)

@favorit_blueprint.route('/', methods=['POST'])
def create_favorit():
    data = request.json
    favorit = Favorit(**data)
    db.session.add(favorit)
    db.session.commit()
    return jsonify({'message': 'Favorit created'}), 201

@favorit_blueprint.route('/', methods=['GET'])
def get_favorits():
    favorits = Favorit.query.all()
    return jsonify([{'favorit_id': f.favorit_id, 'user_id': f.user_id, 'resep_id': f.resep_id} for f in favorits])
