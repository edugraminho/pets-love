from flask import Blueprint
from http import HTTPStatus
from app.models.breed_model import Breed, BreedSchema

bp_breed = Blueprint('bp_breed', __name__, url_prefix='/breed')


@bp_breed.route('/', methods=['GET'])
def get():
    breed = Breed.query.all()

    return {'data': BreedSchema(many=True).dump(breed)}, HTTPStatus.OK


@bp_breed.route('/', methods=['POST'])
def create():
    data = request.get_json()

    breed = Breed(
        name=data["name"]
    )

    try:
        db.session.add(breed)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)