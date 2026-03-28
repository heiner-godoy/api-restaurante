import enum
from sqlalchemy import Column, Integer, DateTime, Numeric, Enum ,Date
from datetime import timezone, datetime
from database import Base

class TipoPeriodo(str, enum.Enum):
    diario = "diario"
    mensual = "mensual"
    anual = "anual"

class Balance(Base):
    __tablename__ = "balance"

    id_balance      = Column(Integer, primary_key=True, autoincrement=True)
    tipo_periodo    = Column(Enum(TipoPeriodo), nullable=False)  # diario | mensual | anual
    fecha           = Column(DateTime, nullable=False)
    total_ventas    = Column(Numeric(10, 2), default=0)
    total_adiciones = Column(Numeric(10, 2), default=0)
    total_gastos    = Column(Numeric(10, 2), default=0)
    total_pagos     = Column(Numeric(10, 2), default=0)
    utilidad        = Column(Numeric(10, 2), default=0)
    creado_en       = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))