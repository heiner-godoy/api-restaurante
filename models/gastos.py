import enum
from sqlalchemy import Column, Integer, DateTime, String, Numeric, Text, Enum
from datetime import timezone, datetime
from database import Base


class CategoriaGasto(str, enum.Enum):
    hormiga  = "hormiga"
    fijo     = "fijo"
    extra    = "extra"
    mercado  = "mercado"
    aseo     = "aseo"
    cocina   = "cocina"


class Gasto(Base):
    __tablename__ = "gastos"  # ← corregido, faltaba la 'n'

    id_gasto    = Column(Integer, primary_key=True, autoincrement=True)
    fecha       = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    descripcion = Column(Text, nullable=False)
    monto       = Column(Numeric(10, 2), nullable=False)  # ← Numeric no Text
    categoria   = Column(Enum(CategoriaGasto), nullable=False)
    creado_en   = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))