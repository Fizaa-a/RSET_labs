# ♛ N-Queens Problem Solver in Python

This Python script solves the classic **N-Queens Problem** — placing N queens on an N×N chessboard such that no two queens attack each other. It prints **all possible solutions** using **recursive backtracking**.

---

## 💡 Problem Statement

The goal is to place N queens on an N×N chessboard so that:
- No two queens share the same row
- No two queens share the same column
- No two queens are on the same diagonal

---

## 🧠 Algorithm Overview

### Backtracking Steps:

1. Start from the first row and try placing a queen in each column.
2. Before placing, check if it's **safe**:
   - No queen in the same column
   - No queen on the same diagonal
3. If safe, place the queen and move to the next row.
4. If a solution is found (row == n), store it.
5. **Backtrack** and try the next possible column.
6. Continue until all possible placements are explored.

---
Sample:
![image](https://github.com/user-attachments/assets/f3fb03a3-7f84-4f9d-a233-fa1719b1a4fe)

