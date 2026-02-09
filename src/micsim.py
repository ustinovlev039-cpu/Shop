class MixsimLog:

    def __init__(self, *args, **kwargs):
        print(repr(self))
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.product_name}, {self.product_description}, {self._price}, {self.quantity})"
