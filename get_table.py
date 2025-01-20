from model import db, app, Customer

with app.app_context():
    Customer=db.session.get(Customer,1)
    
    db.session.commit()