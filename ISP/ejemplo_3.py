from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class AllInOnePrinter(Printer, Scanner, Fax):
    def print(self, document):
        print(f"Printing: {document}")
    
    def scan(self, document):
        print(f"Scanning: {document}")
    
    def fax(self, document):
        print(f"Faxing: {document}")

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")

class NewPrinter(Printer, Scanner):
    def print(self, document):
        print(f"Printing: {document}")
    
    def scan(self, document):
        print(f"Scanning: {document}")


def print_document(printer: Printer, document):
    printer.print(document)

def scan_document(scanner: Scanner, document):
    scanner.scan(document)

# Uso
all_in_one = AllInOnePrinter()
old_printer = OldPrinter()
new_printer = NewPrinter()

print_document(all_in_one, "all_in_one->Informe anual")
print_document(old_printer, "old_printer->Carta")
print_document(new_printer, "new_printer->Foto")

scan_document(all_in_one, "all_in_one->Contrato")
scan_document(new_printer, "new_printer->ID")

# Esto generaría un error en tiempo de ejecución, ya que OldPrinter no implementa Scanner
#scan_document(old_printer, "old_printer->Documento")

