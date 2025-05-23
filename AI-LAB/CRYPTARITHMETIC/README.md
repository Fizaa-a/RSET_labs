# 🔢 Cryptarithmetic Puzzle Solver in Python

A Python program to solve **cryptarithmetic puzzles** such as `SEND + MORE = MONEY`, where each letter represents a unique digit from 0 to 9.

---

## 🧩 What is a Cryptarithmetic Puzzle?

Cryptarithmetic puzzles are mathematical puzzles in which:
- Letters are substituted by digits (0–9)
- Each letter represents a **unique digit**
- No number begins with the digit **0**
- The arithmetic equation must be **valid**

---

## 🧠 Algorithm Overview

1. Combine all letters from the three words (`word1 + word2 = result`)
2. Ensure there are at most 10 unique letters (as only digits 0–9 can be used)
3. Use **`itertools.permutations`** to generate all digit combinations
4. For each combination:
   - Check that no word starts with `0`
   - Convert each word to a number
   - Check if `num1 + num2 == num3`
5. Return the first valid solution (if any)

---
Sample:
When you run the script, input the three words:
First word: SEND
Second word: MORE
Third word: MONEY
(9567, 1085, 10652
SEND = 9567
MORE = 1085
MONEY = 10652
