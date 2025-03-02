# Import the 'dis' module, which is used to analyze and disassemble Python bytecode
import dis  

# Define a simple function that adds two numbers
def add_numbers(a, b):
    return a + b  # Perform addition and return the result

# Print a message indicating that the bytecode of the function will be displayed
print("CPython Bytecode for add_numbers function:")

# Use the 'dis' module to disassemble the function and display its bytecode
dis.dis(add_numbers)
