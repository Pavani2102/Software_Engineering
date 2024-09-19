import math

# Fermat's Last Theorem Near Miss Search Program
# File Name:assignment1.py
# External Files: None
# External Files Created: None
# Programmers: Pavani,Vineela (Group 4)
# Email: (pavanipullela@lewisu.edu)(vineelayadagiri@lewisu.edu)
# Course: Software Engineering(cpsc 60500)
# Date: 09/18/2024
# Resources Used: https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem, 
# Description: This program searches for "near misses" of Fermat's Last Theorem in the form of (x^n + y^n ≠ z^n),
#              where 2 < n < 12, and x, y are integers in the range [10, k], and z is the closest integer 
#              that approximates the sum of x^n and y^n.

def find_near_misses(n, k):
    """
    This function searches for near misses of Fermat's Last Theorem.
    It iterates over x and y in the range [10, k], and calculates the sum of x^n + y^n.
    It then finds the nearest z such that z^n approximates the sum, and calculates the miss value.
    
    Args:
        n (int): The exponent in the equation (2 < n < 12).
        k (int): The upper limit for x and y (k > 10).
    """
    smallest_miss = None  # Holds the smallest miss found
    best_x, best_y, best_z = 0, 0, 0  # Holds the best x, y, z values corresponding to the smallest miss

    # Iterate through all combinations of x and y
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            # Calculate x^n + y^n
            sum_of_powers = x ** n + y ** n

            # Find the closest z where z^n <= x^n + y^n
            z = int(math.pow(sum_of_powers, 1/n))

            # Calculate the miss values
            miss1 = abs(sum_of_powers - z ** n)
            miss2 = abs((z + 1) ** n - sum_of_powers)

            # Determine the smallest miss
            miss = min(miss1, miss2)

            # Calculate the relative miss
            relative_miss = miss / sum_of_powers

            # Keep track of the smallest relative miss
            if smallest_miss is None or relative_miss < smallest_miss:
                smallest_miss = relative_miss
                best_x, best_y, best_z = x, y, z
                print(f"New smallest miss found: x={x}, y={y}, z={z}")
                print(f"Miss (absolute): {miss}, Relative miss: {relative_miss:.10f}\n")

    # Output the final smallest miss
    print("\nFinal Result:")
    print(f"Smallest miss occurs with: x={best_x}, y={best_y}, z={best_z}")
    print(f"Relative miss: {smallest_miss:.10f}")

def main():
    """
    The main function that takes input from the user and runs the near miss search.
    """
    # Get user input for n and k
    try:
        n = int(input("Enter the value for n (2 < n < 12): "))
        if not (2 < n < 12):
            print("Error: n must be greater than 2 and less than 12.")
            return
    except ValueError:
        print("Error: Please enter a valid integer for n.")
        return

    try:
        k = int(input("Enter the value for k (k > 10): "))
        if k <= 10:
            print("Error: k must be greater than 10.")
            return
    except ValueError:
        print("Error: Please enter a valid integer for k.")
        return

    # Call the function to find near misses
    find_near_misses(n, k)

if __name__ == "__main__":
    main()
