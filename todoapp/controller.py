from flask import request

from todoapp import app, db
from todoapp.db_model import User, UserSchema


@app.route('/user', methods=['POST'])
def add_user():
    user = User(**request.json)
    db.session.add(user)
    db.session.commit()
    return UserSchema().jsonify(user)


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    return UserSchema().jsonify(user)


@app.route('/user', methods=['GET'])
def get_all_users():
    all_users = User.query.all()
    return UserSchema(many=True).jsonify(all_users)


@app.route('/user/<int:user_id>/list', methods=['POST'])
def create_list(user_id):
    pass


@app.route('/user/<int:user_id>/list', methods=['GET'])
def get_user_all_lists(user_id):
    pass


@app.route('/user/<int:user_id>/list/<int:list_id>', methods=['GET'])
def get_user_list(user_id, list_id):
    pass


@app.route('/list/<int:list_id>/task', methods=['POST'])
def create_task(list_id):
    pass


@app.route('/list/<int:list_id>/task', methods=['GET'])
def get_all_tasks_in_list(list_id):
    pass


@app.route('/list/<int:list_id>/task/<int:task_id>', methods=['GET'])
def get_task(list_id, task_id):
    pass
