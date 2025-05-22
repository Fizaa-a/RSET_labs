# ⭐ A* Pathfinding Algorithm in Python

This project demonstrates the **A\* (A-star) search algorithm** — a powerful and widely used pathfinding and graph traversal algorithm. It's often used in routing, games, AI, and robotics.

---

## 🧠 How A* Algorithm Works

A* finds the shortest path from a **start node** to a **target node** using:

- `g(n)`: Actual cost from start to node `n`
- `h(n)`: Estimated cost from `n` to goal (heuristic)
- `f(n) = g(n) + h(n)`: Total cost function

It uses both **actual distance** and **estimated cost** to make efficient decisions.

---

## 📌 Algorithm Steps

1. Initialize:
   - `open_set`: Set of discovered but unvisited nodes
   - `closed_set`: Set of visited nodes
   - `g`: Distance from start to current node
   - `parents`: To reconstruct the path

2. Loop until `open_set` is empty:
   - Pick the node with the lowest `f(n)`
   - If it's the goal, return the reconstructed path
   - Else, for each neighbor:
     - If it's in the closed set, skip
     - If new path to neighbor is better:
       - Update g and parent
       - Add to open set

3. If goal isn't reached, return `None`

---
##Sample:
![image](https://github.com/user-attachments/assets/adbfe554-c7eb-4d9c-8968-8b5b8ee33120)

