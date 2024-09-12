from .estudiante import devolver_materias

def estudiante_registrado_materias(nombre, materia):
    try:
        materias = devolver_materias(nombre)
        return materia in materias
    except Exception as e:
        print(f"Ocurrio un error: {e}")
        return False