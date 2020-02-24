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

    def _find_player():
        for line, line_content in enumerate(grid):
            for square, square_content in enumerate(line_content):
                if square_content == (consts.PLAYER or
                               consts.PLAYER_ON_STORAGE_LOCATION):
                    return line, square, square_content
        raise RuntimeError('Player not found!')

    def _whats_at(line, square, move):
        try:
            if move == consts.UP:
                return int(line - 1), int(square), grid[line - 1][square]
            elif move == consts.DOWN:
                return int(line + 1), int(square), grid[line + 1][square]
            elif move == consts.LEFT:
                return int(line), int(square - 1), grid[line][square - 1]
            elif move == consts.RIGHT:
                return int(line), int(square + 1), grid[line][square + 1]
        except IndexError:
            return -1, -1, -1

    def _whats_at(line, square):
        try:
            return grid(line, square)
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

    def _move(from_line, from_square, move):

        to_line, to_square = _get_coords(from_line, from_square, move)

        try:
            if _whats_at(to_line, to_square) == consts.WALL:
                return False
        except IndexError:
            return False

        if _whats_at(from_line, from_square) == (consts.PLAYER_ON_STORAGE_LOCATION or consts.BOX_ON_STORAGE_LOCATION):
            from_content = consts.STORAGE_LOCATION
        else:
            from_content = consts.EMPTY
        if _whats_at(to_line, to_square) == (consts.BOX or consts.BOX_ON_STORAGE_LOCATION):
            _move(to_line, to_square, move)

    grid = _board_as_grid(board)

    try:
        player_line, player_square, player_square_content = _find_player()
    except RuntimeError:
        print('Player not found!')
        return False

    target_line, target_square, target_content = _whats_at(player_line, player_square, move)

    if target_content == consts.WALL:
        return board

    if target_content == consts.BOX:
        passed_box_line, passed_box_square, passed_box_content = _whats_at(target_line, target_square, move)
        if passed_box_content == consts.WALL:
            return board

        if passed_box_content == consts.EMPTY:
            _write(passed_box_line, passed_box_square, consts.BOX)
            _write(target_line, target_square, consts.PLAYER)
            _write(player_line, player_square, consts.EMPTY)
        elif passed_box_content == consts.STORAGE_LOCATION:
            _write(passed_box_line, passed_box_square, consts.BOX_ON_STORAGE_LOCATION)
            _write(target_line, target_square, consts.PLAYER)
            _write(player_line, player_square, consts.EMPTY)
        return _grid_as_board(grid)

    if target_content == consts.STORAGE_LOCATION:
        _move_player()

    if target_content == consts.EMPTY:
        grid[target_line][target_square] = consts.PLAYER
    elif target_content == consts.STORAGE_LOCATION:
        grid[target_line][target_square] = consts.PLAYER_ON_STORAGE_LOCATION

    if grid[player_line][player_square] == consts.PLAYER:
        grid[player_line][player_square] = consts.EMPTY
    elif grid[player_line][player_square] == consts.PLAYER_ON_STORAGE_LOCATION:
        grid[player_line][player_square] = consts.PLAYER_ON_STORAGE_LOCATION

    return _grid_as_board(grid)

