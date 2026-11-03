
#include <iostream>
#include <vector>
using namespace std;

int N;

bool isSafe(const vector<vector<int>>& board, int row, int col) {

    // Check left side of the row
    for (int j = 0; j < col; j++) {
        if (board[row][j] == 1)
            return false;
    }

    // Check upper diagonal
    for (int i = row, j = col;
         i >= 0 && j >= 0; i--, j--) {

        if (board[i][j] == 1)
            return false;
    }

    // Check lower diagonal
    for (int i = row, j = col;
         i < N && j >= 0; i++, j--) {

        if (board[i][j] == 1)
            return false;
    }

    return true;
}


bool solve(vector<vector<int>>& board, int col) {

    if (col >= N)
        return true;

    for (int row = 0; row < N; row++) {

        if (isSafe(board, row, col)) {

            board[row][col] = 1;

            if (solve(board, col + 1))
                return true;

            board[row][col] = 0;  // Backtracking
        }
    }

    return false;
}


int main() {

    cout << "Enter number of queens (N): ";
    cin >> N;

    if (N < 4) {
        cout << "Enter N >= 4 for this fixed-first-queen example.\n";
        return 0;
    }

    vector<vector<int>> board(N, vector<int>(N, 0));

    // Fix the first queen at row 1, column 1
    board[0][0] = 1;

    if (solve(board, 1)) {

        cout << "N-Queens solution:\n";

        for (int i = 0; i < N; i++) {

            for (int j = 0; j < N; j++) {
                cout << board[i][j] << " ";
            }

            cout << '\n';
        }

    } else {

        cout << "No solution exists with the first queen fixed there.\n";
    }

    return 0;
}
