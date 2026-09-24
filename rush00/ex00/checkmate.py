def checkmate(board_str):
    if not isinstance(board_str, str) or not board_str:
        return

    board = [list(row) for row in board_str.splitlines()]
    rows = len(board)

    if rows == 0:
        return

    for row in board:
        if len(row) != rows:
            return

    king_pos = None
    king_count = 0

    for r in range(rows):
        for c in range(rows):
            if board[r][c] == 'K':
                king_pos = (r, c)
                king_count += 1

    if king_count != 1:
        return

    kr, kc = king_pos

    def is_threat_in_direction(dr, dc, valid_pieces):
        r, c = kr + dr, kc + dc

        while 0 <= r < rows and 0 <= c < rows:
            piece = board[r][c]

            if piece in "PBRQK":
                return piece in valid_pieces

            r += dr
            c += dc

        return False

    pawn_threats = [
        (kr + 1, kc - 1),
        (kr + 1, kc + 1)
    ]

    for pr, pc in pawn_threats:
        if 0 <= pr < rows and 0 <= pc < rows:
            if board[pr][pc] == 'P':
                print("Success")
                return

    straight_directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in straight_directions:
        if is_threat_in_direction(dr, dc, ['R', 'Q']):
            print("Success")
            return

    diagonal_directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in diagonal_directions:
        if is_threat_in_direction(dr, dc, ['B', 'Q']):
            print("Success")
            return

    print("Fail")