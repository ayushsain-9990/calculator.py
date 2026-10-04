def print_board(board, N):
    print("\nChessboard Solution:")
    for row in board:
        print(" ".join("👑" if cell == 1 else "⬛" for cell in row))
    print()

def is_safe(board, row, col, N):
    # Check left side of this row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, N, solutions):
    if col >= N:
        # Solution found, store a copy of the board
        solution = [row[:] for row in board]
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, N, solutions)
            board[i][col] = 0  # Backtrack

def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)

    if not solutions:
        print(f"❌ No solution exists for N = {N}")
        return

    print(f"✅ Found {len(solutions)} solution(s) for {N}-Queens Problem!\n")
    print("Showing First Solution:")
    print_board(solutions[0], N)

if __name__ == "__main__":
    print("===== N-QUEENS SOLVER =====")
    try:
        n = int(input("Enter number of Queens (N) [e.g. 4, 8]: "))
        if n <= 0:
            print("❌ N must be greater than 0.")
        else:
            solve_n_queens(n)
    except ValueError:
        print("❌ Invalid input! Enter an integer.")