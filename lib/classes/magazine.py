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

    def subscriptions(self):
        from classes.subscription import Subscription

        return [
            subscription
            for subscription in Subscription.all
            if subscription.magazine == self
        ]

    def readers(self):
        return [subscription.reader for subscription in self.subscriptions()]

    def email_list(self):
        emails = [subscription.reader.email for subscription in self.subscriptions()]
        return ";".join(emails)

    @classmethod
    def most_popular(cls):
        # return sorted(
        #     cls.all,
        #     key=lambda magazine: len(magazine.subscriptions())
        # )[-1]
        return max(cls.all, key=lambda magazine: len(magazine.subscriptions()))

    def __repr__(self):
        return f"{self.title}"
