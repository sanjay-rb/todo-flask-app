from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)

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
            "id":self.id,
            "name" : self.name,
            "email":self.email,
        }

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, email={self.email})'