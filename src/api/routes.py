"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
#from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route("/signup", methods=["POST"])
def signup():
    if request.method == 'POST':
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        #access_token = create_access_token(identity = email)

        if not email:
            return 'Email is required', 401
        if not password:
            return 'Password is required', 401
        
        email_query = User.query.filter_by(email=email).first()
        if email_query:
            return 'This email already exists' , 401

        user = User()
        user.email = email
        user.password = password
        user.is_active = True
        print(user)
        db.session.add(user)
        db.session.commit()

        response = {
            'msg': 'User added successfully',
            #'token': access_token,
            'email': email
        }
        return jsonify(response), 200

@api.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    users = list(map(lambda index: index.serialize(), users))
    response_body = {
        "users": users
    }   
    return jsonify(response_body), 200

# DELETE USER 
@api.route("/users/<int:user>/", methods=["DELETE"])
def delete_user(user):
    users = User.query.filter(User.id == user).first()
    if users is None:
        return jsonify({
            "message": "User does not exist"
        }), 404
    db.session.delete(users)
    db.session.commit()

    return jsonify({
        "message": "User was deleted successfully"
    }), 201
    
# GET 1 SPECIFIC USER
@api.route("/users/<int:user>/", methods=["GET"])
def get_specific_user(user):
    user = User.query.filter(User.id == user).first()

    if user is None:
        return jsonify({
            "message": "No user found"
        }), 404

    return jsonify({
        "user": user.serialize()
    }), 200
    


#@api.route("/signup", methods=["POST"])
#def create_token():
    #email = request.json.get("email", None)
    #password = request.json.get("password", None)
    # Query your database for username and password. #We are expecting either GOOD or BAD email
    #email_check = User.query.filter_by(email=email, password=password).first() #1st email is name of column in table, #2 is email you are writing
    
    #if len(User.query.filter_by(email=email).all()) > 0: #if we find something > 0, will find what is below #User is the table                                              
    #if email is None:
        # the user was not found on the database
        #return jsonify({"msg": "Bad email or password"}), 401
    
    # create a new token with the user id inside #email is good/found
    #access_token = create_access_token(identity=email.id)
    #eturn jsonify({ "token": access_token, "email": email.id }), 200