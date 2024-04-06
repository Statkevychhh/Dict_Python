class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)
    
    def __getitem__(self, item):
        if not 0 <= item <= len(self.marks):
            raise IndexError('Неправильний індекс')
        return self.marks[item]
    
    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Індекс повинен бути цілим невід\'ємним числом')
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
        self.marks[key] = value
    
    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        
        del self.marks[key]


s1 = Student('Сірожа', [5, 5, 3, 2, 5])
print(s1[2])

s1[2] = 4
print(s1[2])

s1[7] = 1
print(s1.marks)

del s1[7]
print(s1.marks)