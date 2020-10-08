class SignUpObject:

    def __init__(self,**kwargs): #SignUp
        self.__username=kwargs["username"]
        self.__isAdmin = kwargs["isAdmin"]
        self.__dateOfBirth = kwargs["dateOfBirth"]
        self.__email=kwargs["email"]
        self.__name = kwargs["name"]
        self.__password = kwargs["password"]
        self.__superpower=kwargs["superpower"]


    def get_name(self):
        return self.__name
    def get_username(self):
        return self.__username
    def get_email(self):
        return self.__email
    def get_superpower(self):
        return self.__superpower
    def get_dateOfBirth(self):
        return self.__dateOfBirth
    def get_isAdmin(self):
        return self.__isAdmin
    def get_password(self):
        return self.__password


    def set_name(self,name):
        self.__name=name
    def set_username(self,username):
        self.__username=username
    def set_email(self,email):
        self.__email=email
    def set_superpower(self,superpower):
        self.__superpower=superpower
    def set_dateOfBirth(self,dateOfBirth):
        self.__dateOfBirth=dateOfBirth
    def set_isAdmin(self,isAdmin):
        self.__isAdmin=isAdmin
    def set_password(self, password):
        self.__isAdmin = password

