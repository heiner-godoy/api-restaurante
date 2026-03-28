import enum
from sqlalchemy import Column, Integer, Boolean, DateTime, String, Enum
from sqlalchemy.orm import relationship
from datetime import timezone, datetime
from database import Base


class CargoEmpleado(str, enum.Enum):
    mesero   = "mesero"
    cocinero = "cocinero"
    cajero   = "cajero"


class Empleados(Base):
    __tablename__ = "empleados"

    id_empleado = Column(Integer, primary_key=True, autoincrement=True)
    nombre      = Column(String(50), unique=True, nullable=False)
    cargo       = Column(Enum(CargoEmpleado), nullable=False)
    activo      = Column(Boolean, default=True, nullable=False)
    creado_en   = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    pagos    = relationship("PagoEmpleado", back_populates="empleado")
    pedidos  = relationship("Pedidos", back_populates="empleado")
    usuarios = relationship("Usuarios", back_populates="empleado")