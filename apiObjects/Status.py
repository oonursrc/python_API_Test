class Status:
    # def __init__(self, status):
    #     self.status = status
    #
    # def get_status(self):
    #     return self.status
    #
    # def set_status(self, status):
    #     pass

    __instance__ = None

    def __init__(self):
        """ Constructor.
        """
        if Status.__instance__ is None:
            Status.__instance__ = self
        else:
            raise Exception("You cannot create another Status class")

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
        """
        if not Status.__instance__:
            Status()
        return Status.__instance__

    @staticmethod
    def set_instance(status):
        Status.__instance__ = status



