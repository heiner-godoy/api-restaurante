from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from models.pedidos import EstadoPedido, TipoEntrega

class CreatePedido(BaseModel):
    id_empleado       : int          = Field(..., description="ID del empleado")
    tipo_entrega      : TipoEntrega  = Field(..., description="mesa | domicilio | para_llevar")
    numero_mesa       : Optional[str] = None
    cliente_nombre    : Optional[str] = None
    cliente_telefono  : Optional[str] = None
    cliente_direccion : Optional[str] = None

class ResponsePedido(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_pedido         : int
    id_empleado       : int
    tipo_entrega      : TipoEntrega
    numero_mesa       : Optional[str]
    cliente_nombre    : Optional[str]
    cliente_telefono  : Optional[str]
    cliente_direccion : Optional[str]
    estado            : EstadoPedido
    creado_en         : Optional[datetime]

class UpdatePedido(BaseModel):
    numero_mesa       : Optional[str] = None
    cliente_nombre    : Optional[str] = None
    cliente_telefono  : Optional[str] = None
    cliente_direccion : Optional[str] = None
    estado            : Optional[EstadoPedido] = None