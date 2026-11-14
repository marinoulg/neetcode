from string import ascii_lowercase

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        def is_in_array(array, string, count):
            for elem in array:
                if string == elem:
                    if string not in count:
                        count[string] = 1
                    else : count[string] += 1
            return count

        def check_array(board):
            # initially: array --> line = board[i]
            # but can work for squares of sudoku, too

            for i in range(len(board)):
                count = {}
                array = board[i]
                for elem in range(1,10):
                    count = is_in_array(array, str(elem), count)
                if max(list(count.values())) != 1:
                    return False
                else: return True

        def get_columns(board):
            columns = []
            for i in range(len(board)):
                tmp = []
                for j in range(len(board[i])):
                    tmp.append(board[j][i])
                columns.append(tmp)
            return columns

        columns = get_columns(board)

        def printing_board():
            for j in range(len(board)):
                line = board[j]
                print(line)
            print()

        def replacing_points_by_IDs(board):
            count=0
            for j in range(len(board)):
                line = board[j]
                for i in range(len(line)):
                    if line[i] == '.':
                        if count in range(26):
                            line[i] = ascii_lowercase[count]
                            c = 0
                        elif count in range(26,52):
                            line[i] = ascii_lowercase[c]*2
                            c += 1
                            cc = 0
                        else:
                            line[i] = ascii_lowercase[cc]*3
                            cc += 1
                        count+=1
            return board

        printing_board()
        replacing_points_by_IDs(board)

        # print()
        # j'ai un 1er square, il faut trouver les autres now
        board_copy = []
        square = []
        for j in range(len(board)):
            line = board[j]
            line_copy = line.copy()
            print(line)
            for i in range(len(line)):
                # square = []
                if i in range(3) :
                    if j in range(3):
                        square.append(line[i])
                        # print(line[i])
                        line_copy.remove(line_copy[i])
                        # board_copy.append(line_copy)
                    elif j in range(2,6):
                        square.append(line[i])
                        line_copy.remove(line_copy[i])
                        # board_copy.append(line_copy)
                        # board_copy.remove(board_copy[j][i])
                    else:
                        square.append(line[i])
                        line_copy.remove(line_copy[i])
            board_copy.append(line_copy)
                        # board_copy.remove(board_copy[j][i])

                # elif i in range(4,7):
                #     print(line[j])
                #     if j <=2:
                #         square.append(line[i])
                #     elif j in range(2,6):
                #         square.append(line[i])
                #     else:
                #         square.append(line[i])

        print()
        first_square_col = []
        start = 0
        for i in range(len(square)):
            if i%9 == 0:
                first_square_col.append(square[start:i])
                start = i
        first_square_col.append(square[start:])
        print(first_square_col[1:])
        # print()
        # print("bc",board_copy)






        # ----- Result -----

        print(check_array(board)) # for lines
        print(check_array(columns)) # for columns
        # print(check_array(squares)) # for squares










board =[
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
    ]

Solution().isValidSudoku(board)
