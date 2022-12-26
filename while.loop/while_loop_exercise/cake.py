height = int(input())
length = int(input())
total_pieces = height * length
piece = int(input())
pieces_left = 0
while piece != "STOP":
    piece = int(piece)

    pieces_left += piece

    if pieces_left >= total_pieces:
        break

    piece = input()

diff = abs(total_pieces - pieces_left)
if piece == "STOP":
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")
