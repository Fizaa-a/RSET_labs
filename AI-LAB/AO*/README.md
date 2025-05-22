# 🌟 AO* (AND-OR Star) Algorithm in Python

A Python implementation of the **AO\* search algorithm**, used for solving problems represented as AND-OR graphs — where solutions may require satisfying multiple conditions (AND) or choosing among alternatives (OR).

---

## 🧠 How AO* Works

The AO\* algorithm is designed to navigate **AND-OR graphs**, typically used in problem-solving domains like **expert systems**, **planning**, and **decision trees**.

### Key Concepts

- **OR node**: Selects the child with the least cost.
- **AND node**: Requires satisfying all children.
- Uses **heuristics** to estimate cost.
- Maintains **open_set** (unexplored) and **closed_set** (explored).

---

## 🔁 Algorithm Steps

1. Initialize `open_set` with start node.
2. Repeat:
   - Choose node `n` with lowest `g(n) + h(n)`
   - If `n` is goal, reconstruct and return path.
   - For each AND/OR child:
     - Update cost `g` and `parents`
     - Add child to `open_set`
3. If goal is unreachable, return `None`.

---
SAMPLE:
![image](https://github.com/user-attachments/assets/6dc568f0-2271-401a-9d24-b510e29260a5)
