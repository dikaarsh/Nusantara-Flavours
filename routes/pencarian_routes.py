
from flask import Blueprint, request, jsonify
from models import Pencarian
from extensions import db

pencarian_blueprint = Blueprint('pencarians', __name__)

@pencarian_blueprint.route('/', methods=['POST'])
def create_pencarian():
    data = request.json
    pencarian = Pencarian(**data)
    db.session.add(pencarian)
    db.session.commit()
    return jsonify({'message': 'Pencarian created'}), 201

@pencarian_blueprint.route('/', methods=['GET'])
def get_pencarians():
    pencarians = Pencarian.query.all()
    return jsonify([{'pencarian_id': p.pencarian_id, 'kata_kunci': p.kata_kunci} for p in pencarians])
