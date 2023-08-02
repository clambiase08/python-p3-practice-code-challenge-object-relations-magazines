# from classes.subscription import Subscription


class Magazine:
    all = []

    def __init__(self, title):
        self.title = title
        Magazine.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value
        else:
            raise Exception("Title must be a string")

    def __repr__(self):
        return f"<Magazine: {self.title}>"
