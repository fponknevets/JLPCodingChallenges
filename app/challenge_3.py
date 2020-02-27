from app import challenge_3_constants as consts


def process_sokoban_move(board=None, move=None):

    def _board_as_grid(board):
        grid = []
        for line, line_content in enumerate(board):
            grid.append([])
            for square_content in line_content:
                grid[line].append(square_content)
        return grid

    def _grid_as_board(grid):
        board = []
        for line in grid:
            line_content = ''
            for square in line:
                line_content += square
            board.append(line_content)
        return board

    def _whats_at(line, square):
        try:
            return grid[line][square]
        except IndexError:
            raise IndexError('Out of bounds! Square at line {}, square {} does not exists'.format(line, square))

    def _write(line, square, character):
        grid[line][square] = character

    def _get_coords(line, square, move):
        new_line = line
        new_square = square
        if move == consts.UP:
            new_line = line -1
        elif move == consts.DOWN:
            new_line = line + 1
        elif move == consts.LEFT:
            new_square = square - 1
        elif move == consts.RIGHT:
            new_square = square + 1
        return new_line, new_square

    def _get_locations():
        for line, line_content in enumerate(grid):
            for square, square_content in enumerate(line_content):
                if square_content in (consts.PLAYER, consts.PLAYER_ON_STORAGE_LOCATION):
                    player_location = [line, square]
                if square_content in (consts.BOX_ON_STORAGE_LOCATION, consts.PLAYER_ON_STORAGE_LOCATION, consts.STORAGE_LOCATION):
                    storage_locations.append([line, square])
        return player_location, storage_locations

    def _store(char):
        return chr(ord(char) - 32)

    def _unstore(char):
        return chr(ord(char) + 32)

    def _is_storage(line, square):
        return [line, square] in storage_locations

    def _move(from_line, from_square, direction):
        to_line, to_square = _get_coords(from_line, from_square, direction)
        try:
            # if the target location is wall
            if _whats_at(to_line, to_square) == consts.WALL:
                return False

            # if the target location is box (or box on storage)
            if _whats_at(to_line, to_square) in [consts.BOX, consts.BOX_ON_STORAGE_LOCATION]:
                if not _move(to_line, to_square, direction):
                    return False

            # if target location is vacant storage
            if _whats_at(to_line, to_square) == consts.STORAGE_LOCATION:
                if _whats_at(from_line, from_square) in [consts.PLAYER, consts.BOX]:
                    _write(to_line, to_square, _store(grid[from_line][from_square]))
                else:
                    _write(to_line, to_square, grid[from_line][from_square])

            # if target location is empty
            if _whats_at(to_line, to_square) == consts.EMPTY:
                if _whats_at(from_line, from_square) in (consts.PLAYER_ON_STORAGE_LOCATION, consts.BOX_ON_STORAGE_LOCATION):
                    _write(to_line, to_square, _unstore(grid[from_line][from_square]))
                else:
                    _write(to_line, to_square, grid[from_line][from_square])

            # finally update the source location
            if [from_line, from_square] in storage_locations:
                _write(from_line, from_square, consts.STORAGE_LOCATION)
            else:
                _write(from_line, from_square, consts.EMPTY)

        except IndexError:
            # scenario - we are trying to move to a non-existent square
            return False

        return True

    grid = _board_as_grid(board)

    player_location = []
    storage_locations = []

    player_location, storage_locations = _get_locations()
    if not player_location:
        return board

    if _move(player_location[consts.LINE], player_location[consts.SQUARE], move):
        return _grid_as_board(grid)
    else:
        return board


