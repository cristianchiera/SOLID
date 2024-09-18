class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

class CalculadoraSalario:
    def calcular_salario(self, empleado):
        # Lógica para calcular el salario
        return empleado.salario * 1.1  # Ejemplo simple: 10% de aumento

class AlmacenadorEmpleado:
    def guardar_en_base_de_datos(self, empleado):
        # Lógica para guardar el empleado en la base de datos
        print(f"Guardando empleado {empleado.nombre} en la base de datos")

class GeneradorReporteEmpleado:
    def generar_reporte(self, empleado):
        # Lógica para generar un reporte del empleado
        print(f"Reporte de {empleado.nombre}: Cargo: {empleado.cargo}, Salario: {empleado.salario}")

# Uso
empleado = Empleado("Juan", "Desarrollador", 50000)

calculadora = CalculadoraSalario()
nuevo_salario = calculadora.calcular_salario(empleado)

almacenador = AlmacenadorEmpleado()
almacenador.guardar_en_base_de_datos(empleado)

generador_reporte = GeneradorReporteEmpleado()
reporte = generador_reporte.generar_reporte(empleado)