# Exercise 3: String Calculator

## Overview
Build a string calculator that adds numbers contained in a string. This is a classic TDD kata that teaches incremental development.

## Requirements

Create a `StringCalculator` class with an `add` method that:

1. **Empty string**: Returns 0
   ```python
   add("")  # Returns 0
   ```

2. **Single number**: Returns that number
   ```python
   add("1")  # Returns 1
   add("5")  # Returns 5
   ```

3. **Two numbers (comma separated)**: Returns their sum
   ```python
   add("1,2")  # Returns 3
   ```

4. **Multiple numbers**: Returns the sum of all
   ```python
   add("1,2,3,4")  # Returns 10
   ```

5. **Newlines as delimiters**: Handle newlines like commas
   ```python
   add("1\n2,3")  # Returns 6
   ```

6. **Negative numbers**: Raise `ValueError` with message "negatives not allowed: {negative_numbers}"
   ```python
   add("1,-2,3")  # Raises ValueError: "negatives not allowed: -2"
   add("1,-2,-3")  # Raises ValueError: "negatives not allowed: -2, -3"
   ```

## Specifications

- Input is a string
- Output is an integer
- Invalid input (non-numeric) should raise `ValueError`
- Multiple negative numbers should all be listed in the error message

## Example Usage

```python
calc = StringCalculator()

calc.add("")           # Returns 0
calc.add("5")          # Returns 5
calc.add("1,2")        # Returns 3
calc.add("1,2,3,4,5")  # Returns 15
calc.add("1\n2,3")     # Returns 6
calc.add("-1,2")       # Raises ValueError
```

## Tips

- Build incrementally - each requirement adds complexity
- Handle edge cases (empty strings, single numbers first)
- String methods like `split()` and `replace()` will be helpful
- Think about how to detect and collect negative numbers

## Time Estimate
10-15 minutes
