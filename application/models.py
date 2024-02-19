from application import db

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Post %d>' % self.id