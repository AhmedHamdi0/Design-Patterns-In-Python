from Singleton.SingletonMeta import SingletonMeta


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        return 1
