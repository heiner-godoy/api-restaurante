from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings  

engine = create_engine(
    settings.DATABASE_URL,  # ← settings en minúscula
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,  
    bind=engine
)

Base = declarative_base()


def crear_tablas():
    from models.rol import Rol
    from models.usuarios import Usuarios
    from models.empleados import Empleados
    from models.platos import Platos
    from models.adicciones import Adicciones
    from models.pedidos import Pedidos
    from models.detalle_pedido import PedidoDetalles
    from models.detalle_adicion import DetalleAdiccion
    from models.ventas import Ventas
    from models.factura import Factura
    from models.pagos_empleado import PagoEmpleado
    from models.gastos import Gasto
    from models.balance import Balance
    Base.metadata.create_all(bind=engine)
