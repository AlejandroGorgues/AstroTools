"""
Class that contains the coordinates of the rectangle to be drawed along all slices
"""

__all__= ['rectangle_selection']

class rectangle_selection:

    def __init__(self, ix, iy, ex, ey):
        self.__ix = ix
        self.__iy = iy
        self.__ex = ex
        self.__ey = ey

    @property
    def ix(self):
        return self.__ix

    @property
    def iy(self):
        return self.__iy

    @property
    def ex(self):
        return self.__ex

    @property
    def ey(self):
        return self.__ey

    @ix.setter
    def ix(self, ix):
        self.__ix = ix

    @iy.setter
    def iy(self, iy):
        self.__iy = iy

    @ex.setter
    def ex(self, ex):
        self.__ex = ex

    @ey.setter
    def ey(self, ey):
        self.__ey = ey
