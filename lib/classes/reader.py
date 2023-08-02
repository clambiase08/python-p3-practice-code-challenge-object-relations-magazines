# from classes.subscription import Subscription


class Reader:
    all = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Reader.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) == str and len(value) > 0:
            self._name = value
        else:
            raise Exception("Invalid name")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if type(value) == str and len(value) > 0:
            self._email = value
        else:
            raise Exception("Invalid email")

    def __repr__(self):
        return f"<Reader | name: {self.name} email: {self.email}>"
