from typing import List, Tuple, Dict


class Deck:
    def __init__(self, row: int, column: int,
                 is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive

class Ship:
    def __init__(self, start: Tuple[int, int], end: Tuple[int, int],
                 is_drowned: bool = False) -> None:
        self.decks: List[Deck] = []
        self.is_drowned = is_drowned
        self.create_decks(start, end)

    def create_decks(self, start: Tuple[int, int],
                     end: Tuple[int, int]) -> None:
        start_row, start_col = start
        end_row, end_col = end
        if start_row == end_row:
            for col in range(start_col, end_col + 1):
                self.decks.append(Deck(start_row, col))
        elif start_col == end_col:
            for row in range(start_row, end_row + 1):
                self.decks.append(Deck(row, start_col))

    def get_deck(self, row: int, column: int) -> Deck:
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return deck
        return None

    def fire(self, row: int, column: int) -> bool:
        deck = self.get_deck(row, column)
        if deck and deck.is_alive:
            deck.is_alive = False
        if all(not d.is_alive for d in self.decks):
            self.is_drowned = True
            return True
        return False

class Battleship:
    def __init__(self, ships):
        # Create a dict `self.field`.
        # Its keys are tuples - the coordinates of the non-empty cells,
        # A value for each cell is a reference to the ship
        # which is located in it
        pass

    def fire(self, location: tuple):
        # This function should check whether the location
        # is a key in the `self.field`
        # If it is, then it should check if this cell is the last alive
        # in the ship or not.
        pass
