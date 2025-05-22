# 🔍 Breadth-First Search (BFS) in Python

A simple and beginner-friendly Python implementation of the **Breadth-First Search (BFS)** algorithm for traversing graphs.

---

## 📘 What is BFS?

Breadth-First Search is a graph traversal technique that explores nodes level by level. It uses a **queue** data structure and is ideal for:
- Finding the shortest path in an unweighted graph
- Level-order traversal in trees

---

## 🧠 Algorithm Steps

1. Initialize a `queue` with the starting node.
2. Mark the node as **visited**.
3. While the queue is not empty:
   - Dequeue a node
   - Print or process it
   - Add all unvisited adjacent nodes to the queue and mark them visited
4. Repeat until all reachable nodes are visited.

---

## 💡 Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

SAMPLE OUTPUT:
![image](https://github.com/user-attachments/assets/607328c0-2295-4bfe-9474-77e2bed6f4d1)
