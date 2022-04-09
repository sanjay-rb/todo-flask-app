from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    todos = db.relationship('Todo', backref='by', lazy=True)

    def signup(self):
        db.session.add(self)
    
    def delete(self):
        db.session.delete(self)

    def commit(self):
        db.session.commit()
        
    def rollback(self):
        db.session.rollback()

    def toJson(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "email" : self.email,
        }

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, email={self.email})'

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(5000), nullable=False)
    due_date = db.Column(db.String(20), nullable=False)
    is_completed = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def add(self):
        db.session.add(self)
    
    def delete(self):
        db.session.delete(self)

    def commit(self):
        db.session.commit()
        
    def rollback(self):
        db.session.rollback()

    def toJson(self):
        return {
            "id" : self.id,
            "content" : self.content,
            "due_date" : self.due_date,
            "is_completed" : self.is_completed,
            "user_id" : self.user_id
        }

    def __repr__(self):
        return f'Todo(id={self.id}, content={self.content}, due_date={self.due_date}, is_completed={self.is_completed}, user_id={self.user_id})'