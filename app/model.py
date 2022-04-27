from flaskblog import db


class Credentials(db.Model):
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100),  nullable=True)

    def __repr__(self):
        return f"Post('{self.email}', '{self.password}')"