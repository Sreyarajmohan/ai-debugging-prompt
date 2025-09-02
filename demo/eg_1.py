# Demo 1: Loop index bug
def buggy_function(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i+1]  # BUG: may go out of range
    return total
print("Student code output:", buggy_function([1, 2, 3]))

# AI Hint Simulation
print("\nAI Hint:")
print("- Check your loop indices. Are you accessing an element that exists?")
print("- Print 'i' and 'total' at each step to trace the error.")
print("- Remember: Python lists are 0-indexed.")
