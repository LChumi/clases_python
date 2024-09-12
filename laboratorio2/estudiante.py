estudiantes_materias ={
    'Daniel': ['Matematicas', 'Computacion'],
    'Maria': ['Matematica', 'Fisica']
}

def devolver_materias(nombre):
    try:
        return estudiantes_materias[nombre]
    except KeyError:
        print(f"El estudiantes '{nombre}' no esta registrado .")
        return[]