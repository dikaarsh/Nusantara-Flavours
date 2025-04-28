
from flask import Blueprint, request, jsonify
from models import Resep
from extensions import db

resep_blueprint = Blueprint('reseps', __name__)

@resep_blueprint.route('/', methods=['POST'])
def create_resep():
    data = request.json
    resep = Resep(**data)
    db.session.add(resep)
    db.session.commit()
    return jsonify({'message': 'Resep created'}), 201

@resep_blueprint.route('/', methods=['GET'])
def get_reseps():
    reseps = Resep.query.all()
    return jsonify([{'resep_id': r.resep_id, 'nama_resep': r.nama_resep} for r in reseps])
