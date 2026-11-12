# ==========================================
# SISTEMA DE CITAS MEDICAS
# Proyecto de Calidad del Software (SQA)
# ==========================================

pacientes = {}
citas = []

medicos = [
    {"id": 1, "nombre": "Laura Gomez", "especialidad": "Medicina General"},
    {"id": 2, "nombre": "Carlos Perez", "especialidad": "Pediatria"},
    {"id": 3, "nombre": "Ana Martinez", "especialidad": "Cardiologia"}
]

horarios = ["08:00", "09:00", "10:00", "11:00",
            "14:00", "15:00", "16:00"]


# 1. REGISTRAR PACIENTES
def registrar_paciente():
    print("\n--- REGISTRO DE PACIENTES ---")

    documento = input("Documento: ")

    if documento in pacientes:
        print("El paciente ya esta registrado.")
        return

    nombre = input("Nombre completo: ")
    telefono = input("Telefono: ")
    edad = input("Edad: ")

    pacientes[documento] = {
        "nombre": nombre,
        "telefono": telefono,
        "edad": edad
    }

    print("Paciente registrado correctamente.")


# 2. CONSULTAR MEDICOS
def consultar_medicos():
    print("\n--- MEDICOS DISPONIBLES ---")

    for medico in medicos:
        print(
            f"ID: {medico['id']} | "
            f"Nombre: {medico['nombre']} | "
            f"Especialidad: {medico['especialidad']}"
        )


# 3. CONSULTAR HORARIOS DISPONIBLES
def consultar_horarios():
    print("\n--- CONSULTA DE HORARIOS ---")

    consultar_medicos()

    try:
        id_medico = int(input("\nIngrese el ID del medico: "))
    except ValueError:
        print("Ingrese un ID valido.")
        return

    medico = next(
        (m for m in medicos if m["id"] == id_medico),
        None
    )

    if medico is None:
        print("Medico no encontrado.")
        return

    fecha = input("Ingrese la fecha (DD/MM/AAAA): ")

    ocupados = [
        cita["hora"] for cita in citas
        if cita["medico"] == id_medico
        and cita["fecha"] == fecha
        and cita["estado"] == "Activa"
    ]

    disponibles = [
        hora for hora in horarios if hora not in ocupados
    ]

    print("\nHorarios disponibles:")

    if disponibles:
        for hora in disponibles:
            print("-", hora)
    else:
        print("No hay horarios disponibles.")


# 4. PROGRAMAR CITAS
def programar_cita():
    print("\n--- PROGRAMAR CITA MEDICA ---")

    documento = input("Documento del paciente: ")

    if documento not in pacientes:
        print("El paciente no esta registrado.")
        return

    consultar_medicos()

    try:
        id_medico = int(input("\nSeleccione el ID del medico: "))
    except ValueError:
        print("ID invalido.")
        return

    medico = next(
        (m for m in medicos if m["id"] == id_medico),
        None
    )

    if medico is None:
        print("Medico no encontrado.")
        return

    fecha = input("Fecha (DD/MM/AAAA): ")

    ocupados = [
        cita["hora"] for cita in citas
        if cita["medico"] == id_medico
        and cita["fecha"] == fecha
        and cita["estado"] == "Activa"
    ]

    disponibles = [
        hora for hora in horarios if hora not in ocupados
    ]

    if not disponibles:
        print("No hay horarios disponibles.")
        return

    print("Horarios:", ", ".join(disponibles))
    hora = input("Seleccione la hora (HH:MM): ")

    if hora not in disponibles:
        print("Horario no disponible o invalido.")
        return

    nueva_cita = {
        "id": len(citas) + 1,
        "documento": documento,
        "medico": id_medico,
        "fecha": fecha,
        "hora": hora,
        "estado": "Activa"
    }

    citas.append(nueva_cita)

    print("Cita programada correctamente.")
    print("Numero de cita:", nueva_cita["id"])


# 5. MODIFICAR CITAS
def modificar_cita():
    print("\n--- MODIFICAR CITA ---")

    try:
        id_cita = int(input("Numero de cita: "))
    except ValueError:
        print("Numero invalido.")
        return

    cita = next(
        (c for c in citas if c["id"] == id_cita
         and c["estado"] == "Activa"),
        None
    )

    if cita is None:
        print("Cita no encontrada.")
        return

    nueva_fecha = input("Nueva fecha (DD/MM/AAAA): ")
    nueva_hora = input("Nueva hora (HH:MM): ")

    if nueva_hora not in horarios:
        print("Horario invalido.")
        return

    ocupado = any(
        c["medico"] == cita["medico"]
        and c["fecha"] == nueva_fecha
        and c["hora"] == nueva_hora
        and c["estado"] == "Activa"
        and c["id"] != id_cita
        for c in citas
    )

    if ocupado:
        print("Ese horario ya esta ocupado.")
        return

    cita["fecha"] = nueva_fecha
    cita["hora"] = nueva_hora

    print("Cita modificada correctamente.")


# 6. CANCELAR CITAS
def cancelar_cita():
    print("\n--- CANCELAR CITA ---")

    try:
        id_cita = int(input("Numero de cita: "))
    except ValueError:
        print("Numero invalido.")
        return

    cita = next(
        (c for c in citas if c["id"] == id_cita
         and c["estado"] == "Activa"),
        None
    )

    if cita is None:
        print("Cita no encontrada.")
        return

    cita["estado"] = "Cancelada"

    print("Cita cancelada correctamente.")


# 7. CONSULTAR HISTORIAL
def historial_citas():
    print("\n--- HISTORIAL DE CITAS ---")

    documento = input("Documento del paciente: ")

    if documento not in pacientes:
        print("Paciente no encontrado.")
        return

    for cita in citas:
        if cita["documento"] == documento:
            medico = next(
                m for m in medicos
                if m["id"] == cita["medico"]
            )

            print(
                f"Cita: {cita['id']} | "
                f"Medico: {medico['nombre']} | "
                f"Fecha: {cita['fecha']} | "
                f"Hora: {cita['hora']} | "
                f"Estado: {cita['estado']}"
            )


# 8. MENU PRINCIPAL
def menu():
    while True:
        print("\n================================")
        print("   SISTEMA DE CITAS MEDICAS")
        print("================================")
        print("1. Registrar paciente")
        print("2. Consultar medicos")
        print("3. Consultar horarios disponibles")
        print("4. Programar cita")
        print("5. Modificar cita")
        print("6. Cancelar cita")
        print("7. Consultar historial de citas")
        print("8. Salir")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            consultar_medicos()
        elif opcion == "3":
            consultar_horarios()
        elif opcion == "4":
            programar_cita()
        elif opcion == "5":
            modificar_cita()
        elif opcion == "6":
            cancelar_cita()
        elif opcion == "7":
            historial_citas()
        elif opcion == "8":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opcion incorrecta. Intente nuevamente.")


# INICIAR PROGRAMA
if __name__ == "__main__":
    menu()
  
