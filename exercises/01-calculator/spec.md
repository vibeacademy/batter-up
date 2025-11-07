# Exercise 1: Calculator

## Overview
Build a simple calculator that can perform basic arithmetic operations on two numbers.

## Requirements

Your calculator should support the following operations:

1. **Addition**: Add two numbers together
2. **Subtraction**: Subtract the second number from the first
3. **Multiplication**: Multiply two numbers
4. **Division**: Divide the first number by the second

## Specifications

- The calculator should have separate methods for each operation
- All methods should accept two numbers as parameters
- All methods should return the result as a number
- Division by zero should raise a `ValueError` with an appropriate message

## Example Usage

```python
calc = Calculator()

# Addition
calc.add(5, 3)  # Returns 8

# Subtraction
calc.subtract(10, 4)  # Returns 6

# Multiplication
calc.multiply(6, 7)  # Returns 42

# Division
calc.divide(15, 3)  # Returns 5.0
calc.divide(10, 0)  # Raises ValueError
```

## Tips

- Start simple: get one operation working at a time
- Run tests frequently to see your progress
- Read error messages carefully - they guide you to what needs fixing
- Don't worry about advanced features - focus on making the tests pass

## Time Estimate
10-15 minutes
