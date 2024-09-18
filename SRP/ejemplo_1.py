class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    
    def calcular_salario(self):
        # Lógica para calcular el salario
        return self.salario * 1.1  # Ejemplo simple: 10% de aumento
    
    def guardar_en_base_de_datos(self):
        # Lógica para guardar el empleado en la base de datos
        print(f"Guardando empleado {self.nombre} en la base de datos")
    
    def generar_reporte(self):
        # Lógica para generar un reporte del empleado
        return f"Reporte de {self.nombre}: Cargo: {self.cargo}, Salario: {self.salario}"

# Uso
empleado = Empleado("Juan", "Desarrollador", 50000)
nuevo_salario = empleado.calcular_salario()
empleado.guardar_en_base_de_datos()
reporte = empleado.generar_reporte()

