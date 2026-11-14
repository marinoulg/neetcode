from string import ascii_lowercase
from pprint import pprint

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        def is_in_array(array, string, count):
            for elem in array:
                if string == elem:
                    if string not in count:
                        count[string] = 1
                    else : count[string] += 1
            return count

        def build_dict(array):
            total_counts = []
            for i in range(len(array)):
                count = {}
                # print(array[i])
                for num in range(1,10):
                    count = (is_in_array(array[i], str(num), count))
                total_counts.append(count)

            return(total_counts)

        def get_columns(board):
            columns = []
            for i in range(len(board)):
                tmp = []
                for j in range(len(board[i])):
                    tmp.append(board[j][i])
                columns.append(tmp)
            return columns

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

        def create_cols(board):
            col1 = []
            col2 = []
            col3 = []
            for j in range(len(board)):
                line = board[j]
                for _ in range(len(line)):
                    col1.append(','.join(line[:3]))
                    col2.append(','.join(line[3:6]))
                    col3.append(','.join(line[6:]))
                    break
            return col1, col2, col3

        def agg_squares(col):
            agg_squares_per_col = []
            start = 0
            for mini_array in range(len(col)):
                if mini_array%3 == 0:
                    agg_squares_per_col.append(','.join(col[start:mini_array]).split(","))
                    start = mini_array
            agg_squares_per_col.append(','.join(col[start:]).split(","))
            return (agg_squares_per_col[1:])

        def all_aggs(board):
            col1, col2, col3 = create_cols(board)
            all_agg_squares = agg_squares(col1)
            for i in range(3):
                all_agg_squares.append(agg_squares(col2)[i])
            for i in range(3):
                all_agg_squares.append(agg_squares(col3)[i])
            return all_agg_squares

        def check_array(check_lines):
            for item in check_lines:
                for v in item.values():
                    if v >1:
                        return(False)
            else:
                return(True)

        def result(board):
            print("initial board")
            printing_board()

            columns = get_columns(board)
            all_agg_squares = all_aggs(board)

            check_lines = (build_dict(board))
            check_cols = (build_dict(columns))
            check_squares = (build_dict(all_agg_squares))

            if (check_array(check_lines)) == True and (check_array(check_cols)) == True and (check_array(check_squares)) == True:
                return True
            else: return False


        # ----- Result -----
        print(result(board))

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

board2 =[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Solution().isValidSudoku(board2)
