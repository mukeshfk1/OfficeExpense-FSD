from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(app, model_class=Base)

class Expense(db.Model):
    id : Mapped[int]= mapped_column(db.Integer, primary_key=True)
    description : Mapped[str] = mapped_column(db.String(200), nullable=False)
    transaction_type : Mapped[str] = mapped_column(db.String(50), nullable=False)
    amount : Mapped[float] = mapped_column(db.Float, nullable=False)
    running_balance : Mapped [float]= mapped_column(db.Float, nullable=False)
    date : Mapped[datetime] = mapped_column(default=lambda: datetime.now())