class Payload:
    # def __init__(self, payload):
    #     self.payload = payload
    #
    # def get_payload(self):
    #     return self.payload
    #
    # def set_payload(self, payload):
    #     pass

    __instance__ = None

    def __init__(self):
        """ Constructor.
        """
        if Payload.__instance__ is None:
            Payload.__instance__ = self
        else:
            raise Exception("You cannot create another Payload class")

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
        """
        if not Payload.__instance__:
            Payload()
        return Payload.__instance__

    @staticmethod
    def set_instance(payload):
        Payload.__instance__ = payload



