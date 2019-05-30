"""   Модуль Сhessman   """


class Сhessman:
    """ Класс  описывает шахматные фигуры"""
    name = 'Пешка'
    color = 'white'
    moves = ((0, 1),)
    cost = 100
    position = tuple()

    @classmethod
    def possible_moves(self):
        """вычитает ходы за пределы доски"""
        moves = [xy for xy in self.moves if 0 < (self.position[0] + xy[0]) < 9 if 0 < (self.position[1] + xy[1]) < 9]
        return moves

    @classmethod
    def print_status(self):
        """ показывает текущее состояние фигуры"""
        print(str(self.name) + '   цвет: ' + str(self.color))
        print('Позиция фигуры ' + str(self.position))
        print('Ценность фигуры: ' + str(self.cost))
        moves = self.possible_moves()
        print('Возможные ходы: ' + str(moves))

    @classmethod
    def moving_chessman(self, new_position):
        """ движение фигуры на новую позицию"""
        if (0 < new_position[0] < 9) and (0 < new_position[1] < 9):
            if new_position in self.moves:
                self.position = new_position


class Pawn(Сhessman):
    """ Описывает фигуру Пешка"""

    moves = (0, 1)  # возможные ходы
    start_moves = ((0, 1), (0, 2))  # возможные ходы


class King(Сhessman):
    """ Описывает фигуру Король"""
    moves = ((1, 1), (-1, 1), (1, -1), (-1, -1))  # возможные ходы


class Queen(Сhessman):
    """ Описывает фигуру Ферзь"""
    name = 'Ферзь'
    moves = ((0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
             (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7),
             (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
             (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0),
             (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
             (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7),
             (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
             (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7)
             )  # возможные ходыды

    def __init__(self, position):
        self.position = position


class Rook(Сhessman):
    """ Описывает фигуру Ладья"""
    moves = ((0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
             (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7),
             (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
             (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0))  # возможные ходы


class Bishop(Сhessman):
    """ Описывает фигуру Слон"""
    moves = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
             (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7),
             (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
             (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7))  # возможные ходы


class KNight(Сhessman):
    """ Описывает фигуру Конь"""
    def __init__(self, position):
        self.position = position
        self.name = 'Конь'
        self.cost = 300
        self.color = 'white'
        self.moves = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))  # возможные ходы





h = Queen(position=(1, 1))
h.print_status()
h.moving_chessman(new_position=(2, 1))
h.print_status()
h.moving_chessman(new_position=(2, 1))
h.print_status()
