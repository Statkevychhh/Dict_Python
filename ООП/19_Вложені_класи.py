class Women:
    title = 'об\'єкт класу для поля title'
    photo = 'об\'єкт класу для поля photo'
    
    def __init__(self, user, psw):
        self.__user = user
        self.__psw = psw
        self.meta = self.Meta((user + '@' + psw))
    
    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self.access = access



w = Women('root', '12345')
print(w.photo)
print(w.Meta.ordering)
print(w.__dict__)
print(w.meta.__dict__)