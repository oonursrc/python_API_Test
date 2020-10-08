class QueryInfoResponseObject:

    def __init__(self,id,name,username,email,superpower,dateOfBirth,isAdmin): #Query one user
        self.__id=id
        self.__name=name
        self.__username=username
        self.__email=email
        self.__superpower=superpower
        self.__dateOfBirth=dateOfBirth
        self.__isAdmin=isAdmin



    def get_id(self):
        return self.__id
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



    def set_id(self,id):
        self.__id=id
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


