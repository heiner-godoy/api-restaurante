API Restaurante
Sistema de gestión para restaurante con control de pedidos, ventas, facturación y balance. Backend en FastAPI + PostgreSQL.

Tabla de contenidos

Descripción general
Arquitectura
Requisitos
Instalación
Variables de entorno
Endpoints de la API
Roles y permisos
Estructura del proyecto


Descripción general
Sistema backend para administrar un restaurante desde un panel web. Permite gestionar pedidos en tiempo real, controlar ventas, generar facturas para empacadores y clientes, registrar gastos y calcular el balance diario, mensual y anual.
Funcionalidades principales:

Gestión de pedidos por mesa, domicilio o para llevar
Soporte para adiciones por plato (maduro, huevo, etc.)
Selección de tipo de sopa por pedido
Generación automática de facturas (empacador y cliente)
Cálculo de cambio al momento del pago
Registro de gastos (hormiga, fijo, extra, mercado, aseo, cocina)
Pagos diarios a empleados
Balance diario, mensual y anual
Autenticación con JWT y roles (admin, cajero, mesero)
WebSocket para pedidos en tiempo real


Arquitectura
[Panel Web / App Empleados]
        |
        | HTTP / WebSocket
        |
[PC Servidor]
        |
        ├── main.py           → punto de entrada
        ├── FastAPI :8000     → API REST + WebSocket
        │     ├── routers/    → endpoints HTTP
        │     ├── controllers/ → lógica de cada petición
        │     └── services/   → lógica de negocio
        ├── database.py       → conexión PostgreSQL
        └── PostgreSQL :5432  → base de datos

Requisitos

Python 3.11 o superior
PostgreSQL 14 o superior


Instalación
1. Clonar el repositorio
bashgit clone https://github.com/tu-usuario/api-restaurante.git
cd api-restaurante
2. Crear entorno virtual
bash# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
3. Instalar dependencias
bashpip install -r requirements.txt
4. Crear la base de datos en PostgreSQL
sqlCREATE DATABASE restaurante;
CREATE USER admin_rest WITH PASSWORD 'tu_password';
GRANT ALL PRIVILEGES ON DATABASE restaurante TO admin_rest;
5. Configurar variables de entorno
bash# Windows
copy .env.example .env

# Linux / Mac
cp .env.example .env
6. Arrancar el servidor
bashpython main.py
```

Las tablas se crean automáticamente en el primer arranque.

### 7. Verificar
```
http://localhost:8000/docs

Variables de entorno
envDATABASE_URL=postgresql://admin_rest:tu_password@localhost:5432/restaurante
JWT_SECRET=reemplaza_con_string_largo_aleatorio
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=480
CORS_ORIGINS=http://localhost:4200
Para generar un JWT_SECRET seguro:
bashpython -c "import secrets; print(secrets.token_hex(32))"
```

---

## Endpoints de la API

### Autenticación

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/auth/login` | Login → retorna JWT |
| GET | `/api/auth/me` | Perfil del usuario actual |

### Roles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/roles` | Listar roles |
| POST | `/api/roles` | Crear rol (admin) |
| PUT | `/api/roles/{id_rol}` | Actualizar rol (admin) |
| DELETE | `/api/roles/{id_rol}` | Eliminar rol (admin) |

### Usuarios

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/usuarios` | Listar usuarios (admin) |
| POST | `/api/usuarios` | Crear usuario (admin) |
| PATCH | `/api/usuarios/{id_usuario}` | Actualizar usuario (admin) |
| DELETE | `/api/usuarios/{id_usuario}` | Eliminar usuario (admin) |

### Empleados

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/empleados` | Listar empleados |
| POST | `/api/empleados` | Crear empleado (admin) |
| PATCH | `/api/empleados/{id_empleado}` | Actualizar empleado (admin) |
| DELETE | `/api/empleados/{id_empleado}` | Desactivar empleado (admin) |

### Platos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/platos` | Listar platos |
| POST | `/api/platos` | Crear plato (admin) |
| PATCH | `/api/platos/{id_plato}` | Actualizar plato (admin) |
| DELETE | `/api/platos/{id_plato}` | Desactivar plato (admin) |

### Adiciones

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/adiciones` | Listar adiciones |
| POST | `/api/adiciones` | Crear adición (admin) |
| PATCH | `/api/adiciones/{id_adicion}` | Actualizar adición (admin) |
| DELETE | `/api/adiciones/{id_adicion}` | Desactivar adición (admin) |

### Pedidos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/pedidos` | Listar pedidos |
| GET | `/api/pedidos/{id_pedido}` | Obtener pedido |
| GET | `/api/pedidos/abiertos` | Pedidos pendientes de pago |
| POST | `/api/pedidos` | Crear pedido |
| PATCH | `/api/pedidos/{id_pedido}` | Actualizar pedido |
| DELETE | `/api/pedidos/{id_pedido}` | Cancelar pedido |

### Detalle de pedido

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/pedidos/{id_pedido}/detalles` | Ver detalles del pedido |
| POST | `/api/pedidos/{id_pedido}/detalles` | Agregar plato al pedido |
| PATCH | `/api/detalles/{id_detalle}` | Actualizar detalle |
| DELETE | `/api/detalles/{id_detalle}` | Eliminar plato del pedido |

### Ventas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/ventas` | Listar ventas |
| GET | `/api/ventas/{id_venta}` | Obtener venta |
| POST | `/api/ventas` | Registrar pago |

### Facturas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/facturas/{id_factura}` | Obtener factura |
| PATCH | `/api/facturas/{id_factura}` | Actualizar estado |

### Gastos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/gastos` | Listar gastos |
| POST | `/api/gastos` | Registrar gasto |
| PATCH | `/api/gastos/{id_gasto}` | Actualizar gasto |
| DELETE | `/api/gastos/{id_gasto}` | Eliminar gasto |

### Pagos empleados

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/pagos-empleados` | Listar pagos |
| POST | `/api/pagos-empleados` | Registrar pago |

### Balance

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/balance/diario` | Balance del día |
| GET | `/api/balance/mensual` | Balance del mes |
| GET | `/api/balance/anual` | Balance del año |

---

## Roles y permisos

| Acción | admin | cajero | mesero |
|--------|-------|--------|--------|
| Ver pedidos | ✅ | ✅ | solo los suyos |
| Crear pedidos | ✅ | ✅ | ✅ |
| Cobrar / venta | ✅ | ✅ | ❌ |
| Generar factura | ✅ | ✅ | ❌ |
| Registrar gastos | ✅ | ✅ | ❌ |
| Ver balance | ✅ | ❌ | ❌ |
| Gestionar empleados | ✅ | ❌ | ❌ |
| Gestionar platos | ✅ | ❌ | ❌ |
| Gestionar usuarios | ✅ | ❌ | ❌ |

---

## Estructura del proyecto
```
api-restaurante/
│
├── controllers/
│   ├── auth.py
│   ├── rol.py
│   ├── usuario.py
│   ├── empleado.py
│   ├── plato.py
│   ├── adicion.py
│   ├── pedido.py
│   ├── detalle_pedido.py
│   ├── venta.py
│   ├── factura.py
│   ├── gasto.py
│   ├── pago_empleado.py
│   └── balance.py
│
├── core/
│   ├── config.py         ← settings desde .env
│   ├── security.py       ← JWT + bcrypt
│   └── dependencies.py   ← inyección de dependencias
│
├── models/
│   ├── rol.py
│   ├── usuarios.py
│   ├── empleados.py
│   ├── platos.py
│   ├── adicciones.py
│   ├── pedidos.py
│   ├── detalle_pedido.py
│   ├── detalle_adicion.py
│   ├── ventas.py
│   ├── factura.py
│   ├── pagos_empleado.py
│   ├── gastos.py
│   └── balance.py
│
├── routers/
│   ├── auth.py
│   ├── rol.py
│   ├── usuario.py
│   ├── empleado.py
│   ├── plato.py
│   ├── adicion.py
│   ├── pedido.py
│   ├── venta.py
│   ├── factura.py
│   ├── gasto.py
│   ├── pago_empleado.py
│   └── balance.py
│
├── schemas/
│   ├── rol.py
│   ├── usuario.py
│   ├── empleado.py
│   ├── plato.py
│   ├── adicion.py
│   ├── pedido.py
│   ├── pedido_detalle.py
│   ├── venta.py
│   ├── factura.py
│   ├── gasto.py
│   ├── pago_empleado.py
│   └── balance.py
│
├── services/
│   ├── rol.py
│   ├── usuario.py
│   ├── empleado.py
│   ├── plato.py
│   ├── adicion.py
│   ├── pedido.py
│   ├── venta.py
│   ├── factura.py
│   ├── gasto.py
│   ├── pago_empleado.py
│   └── balance.py
│
├── database.py
├── main.py
├── websocket.py
├── requirements.txt
├── .env
└── .gitignore

Licencia
MIT
