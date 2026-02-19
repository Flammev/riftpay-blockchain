#what we use to connect to the database
from sqlalchemy import create_engine, VARCHAR, Integer, Column, text, func, ForeignKey, String, DateTime, Float, Boolean, Text
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base 
from config import database_url


engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
con = engine.connect()
Base = declarative_base()

class Person(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    frist_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False)
    account_number = Column(String(20), nullable=False, unique=True)

    bank_accounts = relationship("BankAccount", back_populates="user")

class BankAccount(Base):
    __tablename__ = 'bank_accounts'
    state = ['active', 'inactive', 'suspended']
    account_num = Column(Integer, primary_key=True)
    balance = Column(Float, nullable=False)
    account_type = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    card_num = Column(String(20), nullable=False, unique=True)
    transaction_history = Column(Text, nullable=True)

    user = relationship("Person", back_populates="bank_accounts")

class Card(Base):
    __tablename__ = 'cards'
    state = ['active', 'inactive', 'suspended']
    card_num = Column(String(20), primary_key=True)
    card_type = Column(String(50), nullable=False)
    expiry_date = Column(DateTime, nullable=False)
    cvv = Column(String(4), nullable=False)
    account_num = Column(Integer, ForeignKey('bank_accounts.account_num'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('Person')
    bank_account = relationship('BankAccount')

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    transaction_type = Column(String(50), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    receiver_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    sender_rel = relationship('Person', foreign_keys=[sender_id])
    receiver_rel = relationship('Person', foreign_keys=[receiver_id])

class AuditLog(Base):
    __tablename__ = 'audit_logs'
    log_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    action = Column(String(255), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    user = relationship('Person')

# Only create tables that don't already exist (avoid conflicts with Django-managed tables)
from sqlalchemy import inspect as sa_inspect
_inspector = sa_inspect(engine)
_existing = set(_inspector.get_table_names())
_our_tables = [t for t in Base.metadata.sorted_tables if t.name not in _existing]
Base.metadata.create_all(bind=engine, tables=_our_tables)
session = SessionLocal()
session.commit()
    





#con.execute(text("""CREATE TABLE IF NOT EXISTS person (
           # id SERIAL PRIMARY KEY,
           # name VARCHAR(255) NOT NULL,
           # email VARCHAR(255) NOT NULL UNIQUE
#);"""))
#con.commit()
