def n_queens(n):
    solutions = 0
    columns = set()
    main_diagonals = set()
    side_diagonals = set()

    def place(row):
        nonlocal solutions

        if row == n:
            solutions += 1
            return

        for column in range(n):
            main = row + column
            side = row - column

            if column in columns or main in main_diagonals or side in side_diagonals:
                continue

            columns.add(column)
            main_diagonals.add(main)
            side_diagonals.add(side)

            place(row + 1)

            columns.remove(column)
            main_diagonals.remove(main)
            side_diagonals.remove(side)

    place(0)
    return solutions


if __name__ == "__main__":
    print(n_queens(1))   # 1
    print(n_queens(2))   # 0
    print(n_queens(4))   # 2
    print(n_queens(8))   # 92
