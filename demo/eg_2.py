# Demo 2: Logic bug in conditional

def is_even(n):
    if n % 2 == 1:  # BUG: incorrect check
        return True
    else:
        return False

print("Student code output:", is_even(4))

# AI Hint Simulation
print("\nAI Hint:")
print("- Check what your condition is testing. Does n % 2 == 1 mean even?")
print("- Test your function with small numbers: 0, 1, 2, 3.")
print("- Think about the remainder when dividing by 2.")
