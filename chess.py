from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        """
        Vrací možné tahy pěšáka.
        Bílý pěšák postupuje nahoru, černý dolů, pouze dopředu.
        """
        row, col = self.position
        moves = []
        if self.color == 'white':
            forward = (row + 1, col)
        else:  # self.color == 'black'
            forward = (row - 1, col)

        if self.is_position_on_board(forward):
            moves.append(forward)

        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce (diagonální pohyby).
        """
        row, col = self.position
        moves = []
        # Diagonální směry: (1, 1), (1, -1), (-1, 1), (-1, -1)
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            for step in range(1, 8):
                move = (row + dr * step, col + dc * step)
                if self.is_position_on_board(move):
                    moves.append(move)
                else:
                    break

        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy věže (horizontální a vertikální pohyby).
        """
        row, col = self.position
        moves = []
        # Směry: (1, 0), (-1, 0), (0, 1), (0, -1)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            for step in range(1, 8):
                move = (row + dr * step, col + dc * step)
                if self.is_position_on_board(move):
                    moves.append(move)
                else:
                    break

        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy královny (kombinace věže a střelce).
        """
        row, col = self.position
        moves = []
        # Kombinuje směry věže a střelce
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1),
                      (1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            for step in range(1, 8):
                move = (row + dr * step, col + dc * step)
                if self.is_position_on_board(move):
                    moves.append(move)
                else:
                    break

        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále (pohyb o jedno políčko v jakémkoliv směru).
        """
        row, col = self.position
        moves = [
            (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1)
        ]
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    # Testování figur
    pieces = [
        Pawn("white", (2, 2)),
        Pawn("black", (7, 2)),
        Knight("white", (4, 4)),
        Bishop("black", (3, 3)),
        Rook("white", (1, 1)),
        Queen("black", (4, 4)),
        King("white", (5, 5)),
    ]

    for piece in pieces:
        print(piece)
        print("Possible moves:", piece.possible_moves())
        print()
