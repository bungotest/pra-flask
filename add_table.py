from model import db, app, Customer

with app.app_context():
    new_customer=Customer(company_name='Yamada Ya', employee_number=100)
    db.session.add(new_customer)
    db.session.commit()