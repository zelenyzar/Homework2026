class MixinPrint:
    """Класс, определяющий параметры созданного экземпляра"""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        result_mixin = ""
        for value in self.__dict__.values():
            result_mixin += str(value) + ", "
        return f"{self.__class__.__name__}({result_mixin.rstrip(', ')})"
