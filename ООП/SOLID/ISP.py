from abc import abstractmethod


# 1) НЕ ПРАВИЛЬНО!!!
class Machine:
    def mprint(self, document):
        raise NotImplementedError
    
    def fax(self, document):
        raise NotImplementedError
    
    def scan(self, document):
        raise NotImplementedError



class MultiFunctionPrinter(Machine):
    def mprint(self, document):
        pass
    
    def fax(self, document):
        pass
    
    def scan(self, document):
        pass


class OldFachionedPrinter(Machine):
    def mprint(self, document):
        pass
    
    def fax(self, document):
        pass
    
    def scan(self, document):
        pass




# 2)Виправлення
class Printer:
    @abstractmethod
    def mprint(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner, Fax):
    @abstractmethod
    def mprint(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass



class MyPrinter(Printer):
    def mprint(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def mprint(self, document):
        pass
        
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer,  scanner, fax):
        self.printer = printer
        self.scanner = scanner
        self.fax = fax
    
    def mprint(self, document):
        self.printer.print(document)
        
    def scan(self, document):
        self.scanner.scan(document)
    
    def fax(self, document):
        self.fax.fax(document)