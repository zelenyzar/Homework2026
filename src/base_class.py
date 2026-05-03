from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс, определяющий абстрактный метод для Product"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
