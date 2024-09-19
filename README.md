# Fermat's Last Theorem Near Miss Search

## Description

This program searches for "near misses" of Fermat's Last Theorem in the form of \(x^n + y^n ≠ z^n\), where:
- `x`, `y`, `z` are natural numbers.
- `n` is a natural number such that `2 < n < 12`.
- `x` and `y` are integers between 10 and `k` (inclusive), where `k` is a user-specified value.
- The program calculates the smallest relative miss for each combination of \(x^n + y^n\) and its closest value of \(z^n\).

The program iterates through all possible combinations of `x` and `y`, finds the closest `z` that approximates the sum \(x^n + y^n\), and calculates the relative miss. It displays the smallest miss found.

## How to Run the Program

### Option 1: Using the Executable (.exe) File

1. Download the executable file (`assignment1.exe`) from the GitHub repository.
2. Place the executable in any directory you choose.
3. Open a terminal or command prompt in the directory where the executable is located.
4. Run the program using the following command:

   ```bash
   ./assignment1.exe
5. The program will prompt you for two inputs:

  n: The power for Fermat's Last Theorem, where 2 < n < 12.
  k: The upper limit for x and y, where k > 10.
6. The program will compute and display near misses, printing each time it finds a new smallest relative miss. The smallest miss found will be displayed at the end.


### Option 2: Using the Python Script

1. If you prefer running the source code directly, you can use the Python script:

2. Ensure you have Python installed. If not, download and install the latest version of Python from here.

3. Clone the repository or download the assignment1.py file.

4. Open a terminal or command prompt in the directory where assignment1.py is located.

5. Run the program using the following command:

```bash
python assignment1.py
