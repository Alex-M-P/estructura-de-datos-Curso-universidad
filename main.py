from fastapi import FastAPI

# paquete de ejercicios 
from ejercicios import  multiplicacion, suma, calcularFactorialRecursivo

# paquete de cda
from cda import ColasVehiculo



app = FastAPI()

# ----- paquete ejercicios ---------------------------------------
@app.get("/")
def read_root():
    return {"Hello": "World", "mensaje": "Bienvenido a la API  "}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/suma/{a}/{b}")
def sumar(a: int, b: int):
    resultado = suma(a, b)
    return {"resutado": resultado}

@app.get("/multiplicacion/{a}/{b}")
def multiplicar(a: int, b: int):
    resultado = multiplicacion(a, b)
    return {"resutado": resultado}     

@app.get("/calcularFactorialRecursivo/{a}")
def obtenerFactorial(a: int):
    resultado = calcularFactorialRecursivo(a)
    return {"resutado": resultado}


# ------ Paquete cda ---------------------------------------------

@app.post("/registrarVehiculo/")
def registrarVehiculo(marca: str, modelo: str, anio: int, tipo: str):
    colas_vehiculo = ColasVehiculo()
    vehiculo = colas_vehiculol.agregar_vehiculo(marca, modelo, anio, tipo)
    return {"vehiculo": vehiculo}