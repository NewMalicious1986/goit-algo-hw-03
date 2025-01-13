def solve_hanoi(disks, start, temp, end, rods):
    if disks == 1:
        rods[end].append(rods[start].pop())
        print(f"Move disk from {start} to {end}: {rods[end][-1]}")
        print(f"Current state: {rods}")
    else:
        solve_hanoi(disks - 1, start, end, temp, rods)
        rods[end].append(rods[start].pop())
        print(f"Move disk from {start} to {end}: {rods[end][-1]}")
        print(f"Current state: {rods}")
        solve_hanoi(disks - 1, temp, start, end, rods)

if __name__ == "__main__":
    try:
        num_disks = int(input("Enter the number of disks: "))
        if num_disks < 1:
            print("Number of disks must be a positive integer.")
        else:
            rods = {
                "A": list(range(num_disks, 0, -1)),
                "B": [],
                "C": []
            }
            print(f"Starting state: {rods}")
            solve_hanoi(num_disks, "A", "B", "C", rods)
            print(f"Final state: {rods}")
    except ValueError:
        print("Invalid input! Please enter a positive integer.")