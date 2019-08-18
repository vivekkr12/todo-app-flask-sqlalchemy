from datetime import datetime

from todoapp import db, ma


class User(db.Model):
    __tablename__ = 'users'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(100), nullable=False)
    email: str = db.Column(db.String(200), nullable=False)
    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return 'User({}, name: {}, email: {}, created: {}, updated: {})'.format(self.id, self.name, self.email,
                                                                                self.created_at, self.updated_at)


class TodoList(db.Model):
    __tablename__ = 'todo_lists'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(100), nullable=False)
    user_id: int = db.Column(db.Integer, db.ForeignKey('users.id'))
    user: User = db.relationship('User')
    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return 'List({}, name: {}, owner: {}, created: {}, updated: {})'.format(self.id, self.name, self.user_id,
                                                                                self.created_at, self.updated_at)


class Task(db.Model):
    __tablename__ = 'tasks'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    list_id: int = db.Column(db.Integer, db.ForeignKey('todo_lists.id'))
    list: TodoList = db.relationship('TodoList', backref='tasks')
    desc: str = db.Column(db.String(500), nullable=False)
    status: int = db.Column(db.Integer, default=0, nullable=False)
    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return 'Task({}, list: {}, desc: {}, created: {}, updated: {})'.format(self.id, self.list_id, self.desc,
                                                                               self.created_at, self.updated_at)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


class TodoListSchema(ma.ModelSchema):
    class Meta:
        model = TodoList


class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task
