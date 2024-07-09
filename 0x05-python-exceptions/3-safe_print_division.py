#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides and prints the result"""
    try:
        result = a / b
        return (result)
    except ZeroDivisionError:
        result = None
        return (result)
    finally:
        print(f"Inside result: {result}")
