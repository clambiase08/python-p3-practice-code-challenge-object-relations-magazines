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

    def subscriptions(self):
        from classes.subscription import Subscription

        return [
            subscription
            for subscription in Subscription.all
            if subscription.reader == self
        ]

    def magazines(self):
        return [subscription.magazine for subscription in self.subscriptions()]

    def subscribe(self, magazine, price):
        from classes.subscription import Subscription

        Subscription(magazine, self, price)

    def total_subscription_price(self):
        return sum([subscription.price for subscription in self.subscriptions()])

    def cancel_subscription(magazine):
        pass

    def __repr__(self):
        return f"{self.name}"
