import math
import random


class Game:
    def __init__(self):
        self.game_over = None
        self.turn = None

    def win(self, board, row, column, piece):
        for c in range(column - 3):
            for r in range(row):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True

        for c in range(column):
            for r in range(row - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                    return True

        for c in range(column - 3):
            for r in range(row - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][c + 3] == piece:
                    return True

        for c in range(column - 3):
            for r in range(3, row):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][c + 3] == piece:
                    return True

    def valid(self, board, row, column):
        return board[row - 1][column] == 0

    def draw(self, board, ROW, COLUMN):
        for c in range(COLUMN):
            for r in range(ROW):
                if board[r][c] == 0:
                    return False
        return True

    def next(self, board, row, column):
        for row in range(row):
            if board[row][column] == 0:
                return row

    def score(self, board, ROW, COLUMN, piece):
        score = 0

        center_array = [int(i) for i in list(board[:, COLUMN // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        for r in range(ROW):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(COLUMN - 3):
                window = row_array[c:c + 4]
                score += self.evaluate(window, 1, 2, piece)

        for c in range(COLUMN):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(ROW - 3):
                window = col_array[r:r + 4]
                score += self.evaluate(window, 1, 2, piece)

        for r in range(ROW - 3):
            for c in range(COLUMN - 3):
                window = [board[r + i][c + i] for i in range(4)]
                score += self.evaluate(window, 1, 2, piece)

        for r in range(ROW - 3):
            for c in range(COLUMN - 3):
                window = [board[r + 3 - i][c + i] for i in range(4)]
                score += self.evaluate(window, 1, 2, piece)

        return score

    def evaluate(self, window, PLAYER, AI, piece):
        score = 0
        opp_piece = PLAYER
        if piece == PLAYER:
            opp_piece = AI

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 2
        if window.count(opp_piece) == 3 and window.count(0) == 1:
            score -= 4

        return score

    def minmax(self, board, depth, alpha, beta, maximizingPlayer, ROW, COLUMN):
        valid_locations = []
        for col in range(COLUMN):
            if self.valid(board, ROW, col):
                valid_locations.append(col)

        is_terminal = self.win(board, ROW, COLUMN, 1) or self.win(board, ROW, COLUMN, 2)

        if depth == 0 or is_terminal:
            if is_terminal:
                if self.win(board, ROW, COLUMN, 2):
                    return None, math.inf
                elif self.win(board, ROW, COLUMN, 1):
                    return None, -math.inf
                else:
                    return None, 0
            else:
                return None, self.score(board, ROW, COLUMN, 2)

        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.next(board, ROW, col)
                b_copy = board.copy()
                b_copy[row][col] = 2
                new_score = self.minmax(b_copy, depth - 1, alpha, beta, False, ROW, COLUMN)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.next(board, ROW, col)
                b_copy = board.copy()
                b_copy[row][col] = 1
                new_score = self.minmax(b_copy, depth - 1, alpha, beta, True, ROW, COLUMN)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value
