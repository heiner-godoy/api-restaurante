import enum
from sqlalchemy import Column, Integer, Boolean, DateTime, String, Numeric, Enum
from sqlalchemy.orm import relationship
from datetime import timezone, datetime
from database import Base


class CargoEmpleados(str, enum.Enum):
    mesero = "meser@"
    cocinero = "cocinero@"
    cajero = "cajer@"


class Empleados(Base):
    __tablename__ = "empleados"

    id_empleado = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    nombre = Column(String(50), unique=True, nullable=False)
    cargo = Column(Enum(CargoEmpleados), nullable=False)
    activo = Column(Boolean, default=True, nullable=False)
    creado_en = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    pagos = relationship("PagoEmpleado", back_populates="empleado")
    pedidos = relationship("Pedidos", back_populates="empleado")
    usuarios = relationship("Usuarios", back_populates="empleado")

