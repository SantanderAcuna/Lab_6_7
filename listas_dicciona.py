# Lista de nombres de estudiantes
estudiantes = ["Juan", "Ana", "Luis"]
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante}")

# Diccionario de información de contacto
contactos = {"Juan": "juan@example.com", "Ana": "ana@example.com"}
for nombre, correo in contactos.items():
    print(f"{nombre} -> {correo}")

# Agregar elementos a una lista y actualizar valores en un diccionario
nuevo_estudiante = input("Ingresa el nombre de un nuevo estudiante: ")
estudiantes.append(nuevo_estudiante)
print("Lista actualizada:", estudiantes)

contactos[nuevo_estudiante] = input(f"Ingresa el correo de {nuevo_estudiante}: ")
print("Contactos actualizados:", contactos)
