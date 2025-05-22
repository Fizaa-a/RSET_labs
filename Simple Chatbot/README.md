# 🤖 Simple Python Chatbot

A beginner-friendly **Python chatbot** that interacts via the terminal using predefined responses and basic pattern matching.

---

## 🧠 Algorithm (How It Works)

1. Define a dictionary of **keyword-based responses**.
2. Display a welcome message.
3. Continuously:
   - Take user input
   - Normalize it (lowercase, strip spaces)
   - If input is `"bye"`, exit with a goodbye message
   - Else, check:
     - If the exact input exists in `responses`, reply with the matched value
     - Else, look for keywords in the input
     - If no match, reply with a fallback message
4. Repeat until the user types `"bye"`

---

## 💡 Example Interaction
![image](https://github.com/user-attachments/assets/460900b3-a4c7-4140-830b-b4a3516d0e5c)
