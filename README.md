🪨 Rock Paper Scissors Game (Python)

This is a simple Rock–Paper–Scissors game written in Python.
The player plays against the computer for 6 rounds.

📌 How the Game Works

The player enters their choice using:

r → Rock

p → Paper

s → Scissors

The computer randomly chooses between:

Rock

Paper

Scissors

The winner is decided based on standard rules:

Rock beats Scissors

Scissors beats Paper

Paper beats Rock

If both choose the same option, the round is a tie.

🛠 Requirements

Python 3.x

No external libraries required (only random, which is built-in)

▶️ How to Run

Save the file as game.py

Open terminal / command prompt

Run:

python game.py

🎮 Sample Input
Enter your choice (r,p,s): r

🖥 Sample Output
Round 1
Computer chose: paper
YourChoice: rock
computer win

📂 Code Structure

d → Dictionary mapping short inputs to full names

options → List for computer’s random choice

game() → Function that runs one round

Loop runs the game 6 times

❗ Notes

Enter only r, p, or s

Any other input will be treated as invalid

✨ Possible Improvements

Add score tracking

Ask user to continue instead of fixed rounds

Handle invalid input before accessing dictionary
## 👤 Author
Vasudev******

Made for learning Python basics, conditions, and random module.
