#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 130, 40, 70), Rectangle(110, 32, 12, 80)]
    list_squares = [Square(35)]

    Base.draw(list_rectangles, list_squares)
