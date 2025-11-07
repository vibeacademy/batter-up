# Exercise 2: Temperature Converter

## Overview
Build a temperature converter that converts between Celsius, Fahrenheit, and Kelvin.

## Requirements

Your converter should support these conversions:

1. **Celsius to Fahrenheit**: °F = (°C × 9/5) + 32
2. **Fahrenheit to Celsius**: °C = (°F - 32) × 5/9
3. **Celsius to Kelvin**: K = °C + 273.15
4. **Kelvin to Celsius**: °C = K - 273.15

## Specifications

- Create methods for each conversion direction
- Accept numeric input (int or float)
- Return a float rounded to 2 decimal places
- Kelvin values below 0 should raise a `ValueError` (absolute zero is 0K)
- Method names should be clear: `celsius_to_fahrenheit`, `fahrenheit_to_celsius`, etc.

## Example Usage

```python
converter = TemperatureConverter()

# Celsius to Fahrenheit
converter.celsius_to_fahrenheit(0)     # Returns 32.0
converter.celsius_to_fahrenheit(100)   # Returns 212.0

# Fahrenheit to Celsius
converter.fahrenheit_to_celsius(32)    # Returns 0.0
converter.fahrenheit_to_celsius(212)   # Returns 100.0

# Celsius to Kelvin
converter.celsius_to_kelvin(0)         # Returns 273.15

# Kelvin to Celsius
converter.kelvin_to_celsius(273.15)    # Returns 0.0
converter.kelvin_to_celsius(-1)        # Raises ValueError
```

## Tips

- Remember to round to 2 decimal places
- Physics fact: 0 Kelvin is absolute zero (coldest possible temperature)
- Test edge cases like freezing/boiling points of water

## Time Estimate
10-15 minutes
