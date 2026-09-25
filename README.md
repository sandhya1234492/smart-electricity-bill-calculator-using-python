# Smart Electricity Bill Calculator

This beginner-friendly Python console program collects customer details, calculates an electricity bill, and displays a formatted bill.

## How to run

Make sure Python 3 is installed, then run:

```text
python smart_electricity_bill.py
```

## Program flow

1. `get_customer_details()` asks for the customer name, customer ID, and units consumed.
2. The units are converted from text to an integer.
3. Negative units are rejected, and the user is asked to enter them again.
4. `calculate_bill()` applies the progressive energy slabs:
	- First 100 units: 2 per unit
	- Units 101 to 200: 4 per unit
	- Units 201 to 500: 6 per unit
	- Units above 500: 8 per unit
5. A fixed service charge of `$100` is added.
6. `display_bill()` prints the customer details, units consumed, energy charge, service charge, and final amount.

## Example calculation

For 250 units:

- First 100 units: `100 * 2 = 200`
- Next 100 units: `100 * 4 = 400`
- Remaining 50 units: `50 * 6 = 300`
- Energy charge: `900`
- Service charge: `100`
- Final amount: `1000`

The program uses variables, strings, integers, floats, functions, parameters, return values, input, type conversion, comparison operators, conditional statements, loops, and formatted output. It does not use a database, files, APIs, external libraries, or classes.