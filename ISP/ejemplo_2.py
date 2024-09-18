from abc import ABC, abstractmethod

class MultifunctionPrinter(ABC):
    @abstractmethod
    def print(self, document):
        pass
    
    @abstractmethod
    def scan(self, document):
        pass
    
    @abstractmethod
    def fax(self, document):
        pass

class AllInOnePrinter(MultifunctionPrinter):
    def print(self, document):
        print(f"Printing: {document}")
    
    def scan(self, document):
        print(f"Scanning: {document}")
    
    def fax(self, document):
        print(f"Faxing: {document}")

class OldPrinter(MultifunctionPrinter):
    def print(self, document):
        print(f"Printing: {document}")
    
    def scan(self, document):
        raise NotImplementedError("This printer cannot scan.")
    
    def fax(self, document):
        raise NotImplementedError("This printer cannot fax.")



