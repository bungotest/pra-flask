import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from datetime import datetime

base_dir = os.path.dirname(__file__)

app = Flask(__name__)

database_path = os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app, model_class=Base)

class Customer(db.Model):
    __tablename__ = 'customer'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    company_name: Mapped[str] = mapped_column(db.String(50), nullable=False, index=True)
    employee_number: Mapped[int] = mapped_column(db.Integer, nullable=False)
    # created_at: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now())
    # updated_at: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now(), onupdate=func.now())
    
    def __str__(self):
        return f"id={self.id}, company_name={self.company_name}, employees={self.employee_number}"

print(db)
print(db.metadata.tables)


