class User:
    
    def __init__(self,name, age, email, password):
        self.__name = name
        self.__age = age
        self.__email = email
        self.__password = password

    @property
    def Name(self):
        return self.__name

    @property
    def Age(self):
        return self.__age

    @property
    def Email(self):
        return self.__email

    @property
    def password(self):
        return self.__password