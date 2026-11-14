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


        # j'ai un 1er square, il faut trouver les autres now
        square = []
        for j in range(len(board)):
            line = board[j]
            print(line)
            for i in range(len(line)):
                # square = []
                if i<=2 :
                    if j <=2:
                        square.append(line[i])
                    elif j in range(2,6):
                        square.append(line[i])
                    else:
                        square.append(line[i])

        first_square_col = []
        start = 0
        for i in range(len(square)):
            if i%9 == 0:
                first_square_col.append(square[start:i])
                start = i
        first_square_col.append(square[start:])
        print(first_square_col[1:])
            # print()
        # print(square)

        # square = []
        # for j in range(3, len(board)):
        #     line = board[j]
        #     print(line)
        #     for i in range(2, len(line)):
        #         if 2<i<=4 and 2<j<=4:
        #             square.append(line[i])
        # print(square)






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
