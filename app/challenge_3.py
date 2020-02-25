from app import challenge_3_constants as consts


def process_sokoban_move(board=None, move=None):

    def _board_as_grid(board):
        grid = []
        for line, line_content in enumerate(board):
            grid.append([])
            for square, square_content in enumerate(line_content):
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

    def _move(from_line, from_square, move):
        to_line, to_square = _get_coords(from_line, from_square, move)
        try:
            # what should we write in the square we are moving from once we move
            if _whats_at(from_line, from_square) in (consts.PLAYER_ON_STORAGE_LOCATION, consts.BOX_ON_STORAGE_LOCATION):
                from_content_to_write = consts.STORAGE_LOCATION
            else:
                from_content_to_write = consts.EMPTY

            # scenario - we are trying to move to a wall
            if _whats_at(to_line, to_square) == consts.WALL:
                return False

            # scenario - we are trying to move to a box
            if _whats_at(to_line, to_square) in (consts.BOX, consts.BOX_ON_STORAGE_LOCATION):
                if not _move(to_line, to_square, move):
                    return False

            # scenario - we are trying to move to a storage location
            if [to_line, to_square] in storage_locations:
                if _whats_at(from_line, from_square) == consts.PLAYER:
                    _write(to_line, to_square, consts.PLAYER_ON_STORAGE_LOCATION)
                    _write(from_line, from_square, consts.EMPTY)
                if _whats_at(from_line, from_square) == consts.PLAYER_ON_STORAGE_LOCATION:
                    _write(to_line, to_square, consts.PLAYER_ON_STORAGE_LOCATION)
                    _write(from_line, from_square, consts.STORAGE_LOCATION)
                if _whats_at(from_line, from_square) == consts.BOX:
                    _write(to_line, to_square, consts.BOX_ON_STORAGE_LOCATION)
                    _write(from_line, from_square, consts.EMPTY)
                if _whats_at(from_line, from_square) == consts.BOX_ON_STORAGE_LOCATION:
                    _write(to_line, to_square, consts.BOX_ON_STORAGE_LOCATION)
                    _write(from_line, from_square, consts.STORAGE_LOCATION)

            # scenario - we are trying to move to a place that is empty
            if _whats_at(to_line, to_square) == consts.EMPTY:
                _write(to_line, to_square, grid[from_line][from_square])
                _write(from_line, from_square, from_content_to_write)

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


