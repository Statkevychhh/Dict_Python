from abc import ABC, abstractmethod



class MyInterface(ABC):  # - Інтерфейс
    @abstractmethod
    def method(self):  # - Абстрактний метод
        pass

# Абстрактний клас - це клас який містить хочаб 1 абстрактний метод.