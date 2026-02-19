from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine, Float, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from alchemy_con import Base
from config import database_url

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class BlockchainProof(Base):
    __tablename__ = "blockchain_proofs"

    id = Column(Integer, primary_key=True)
    transaction_id = Column(String(50), nullable=False)
    blockchain = Column(String(20), default="STELLAR")
    proof_hash = Column(String(64), nullable=False)
    stellar_tx_hash = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

Base.metadata.create_all(bind=engine)
session = SessionLocal()
session.commit()