from config import settings


class BaseObject:
    def __init__(self, height: float, width: float):
        self._height = height
        self._width = width
        self._colour = 'purple'

    def fall(self):
        """Object is falling"""
        ...

    def color(self):
        """Shows object colour"""
        ...

    def newton_acceleration(self):
        """Object is **extremely** falling"""
        ...


class Object3D(BaseObject):
    def __init__(self, depth: float, height: float, width: float):
        super().__init__(height, width)
        self._depth = depth

    def fall(self):
        print(f'{ObjectCircle.__name__} is falling...')
        print(f'Height: {self._height} Width: {self._width}, Depth: {self._depth}')

    def color(self):
        print(f'My colour is {self._colour}')


class ObjectCircle(BaseObject):
    def __init__(self, height: float, width: float):
        super().__init__(height, width)

    def fall(self):
        print(f'{ObjectCircle.__name__} is falling...')
        print(f'Height: {self._height} Width: {self._width}')


a = BaseObject(2, 2)
b = Object3D(2, 2, 2)
c = ObjectCircle(2, 2)
b.fall()
b.newton_acceleration()
b.color()
c.fall()
