#!/usr/bin/env python3
"""
🔮 FUTURISTIC SCIENTIFIC CALCULATOR 🔮
Advanced computational device with sci-fi aesthetic interface
"""

import math
import sys
from typing import Union, Callable
from enum import Enum

class Colors:
    """Sci-fi neon color codes"""
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

class BorderStyle(Enum):
    """ASCII art border styles"""
    FUTURISTIC = "═"
    CORNER_TL = "╔"
    CORNER_TR = "╗"
    CORNER_BL = "╚"
    CORNER_BR = "╝"
    VERTICAL = "║"
    HORIZONTAL = "═"

def print_header():
    """Display the sci-fi calculator header"""
    width = 70
    header = f"""
{Colors.CYAN}{BorderStyle.CORNER_TL.value}{BorderStyle.HORIZONTAL.value * (width - 2)}{BorderStyle.CORNER_TR.value}{Colors.RESET}
{Colors.MAGENTA}{BorderStyle.VERTICAL.value}{Colors.CYAN}{' ' * (width - 2)}{Colors.MAGENTA}{BorderStyle.VERTICAL.value}{Colors.RESET}
{Colors.MAGENTA}{BorderStyle.VERTICAL.value}{Colors.YELLOW}{Colors.BOLD}🔮 FUTURISTIC SCIENTIFIC CALCULATOR 🔮{Colors.RESET}{Colors.MAGENTA}{' ' * 22}{BorderStyle.VERTICAL.value}{Colors.RESET}
{Colors.MAGENTA}{BorderStyle.VERTICAL.value}{Colors.BLUE}{Colors.DIM}>>> Advanced Computational Interface <<<{Colors.RESET}{Colors.MAGENTA}{' ' * 24}{BorderStyle.VERTICAL.value}{Colors.RESET}
{Colors.MAGENTA}{BorderStyle.VERTICAL.value}{Colors.CYAN}{' ' * (width - 2)}{Colors.MAGENTA}{BorderStyle.VERTICAL.value}{Colors.RESET}
{Colors.CYAN}{BorderStyle.CORNER_BL.value}{BorderStyle.HORIZONTAL.value * (width - 2)}{BorderStyle.CORNER_BR.value}{Colors.RESET}
"""
    print(header)

def print_menu():
    """Display available operations"""
    menu = f"""
{Colors.GREEN}{'=' * 70}{Colors.RESET}
{Colors.YELLOW}{Colors.BOLD}[BASIC OPERATIONS]{Colors.RESET}
{Colors.CYAN}  1: Addition (+)        2: Subtraction (-)     3: Multiplication (*)
  4: Division (/)         5: Exponentiation (**)    6: Modulo (%)
  7: Floor Division (//)

{Colors.YELLOW}{Colors.BOLD}[TRIGONOMETRIC]{Colors.RESET}
{Colors.CYAN}  8: Sine (sin)          9: Cosine (cos)        10: Tangent (tan)
  11: Arcsine (asin)      12: Arccosine (acos)    13: Arctangent (atan)

{Colors.YELLOW}{Colors.BOLD}[LOGARITHMIC & POWER]{Colors.RESET}
{Colors.CYAN}  14: Natural Log (ln)    15: Log Base 10        16: Log Base 2
  17: Square Root         18: Cube Root           19: Power/Exponent

{Colors.YELLOW}{Colors.BOLD}[CONSTANTS & UTILITIES]{Colors.RESET}
{Colors.CYAN}  20: Pi (π)              21: Euler (e)          22: Absolute Value
  23: Factorial           24: Degrees to Radians  25: Radians to Degrees

{Colors.YELLOW}{Colors.BOLD}[ADVANCED]{Colors.RESET}
{Colors.CYAN}  26: Hyperbolic Sine     27: Hyperbolic Cosine  28: Hyperbolic Tangent
  29: Combination (nCr)   30: Permutation (nPr)   31: GCD
  32: LCM

{Colors.MAGENTA}{Colors.BOLD}  0: EXIT{Colors.RESET}
{Colors.GREEN}{'=' * 70}{Colors.RESET}
"""
    print(menu)

def validate_input(prompt: str, input_type: type = float) -> Union[int, float]:
    """Safely get numeric input from user"""
    while True:
        try:
            user_input = input(f"{Colors.CYAN}{prompt}{Colors.RESET}")
            return input_type(user_input)
        except ValueError:
            print(f"{Colors.RED}⚠ Invalid input! Please enter a valid number.{Colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}Shutting down calculator...{Colors.RESET}")
            sys.exit(0)

def two_operand_operation(op: Callable, op_name: str) -> None:
    """Handle operations requiring two operands"""
    try:
        a = validate_input(f"Enter first number: ")
        b = validate_input(f"Enter second number: ")
        result = op(a, b)
        print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}{Colors.RESET}\n")
    except Exception as e:
        print(f"{Colors.RED}⚠ Error in {op_name}: {str(e)}{Colors.RESET}\n")

def single_operand_operation(op: Callable, op_name: str, radians: bool = False) -> None:
    """Handle operations requiring one operand"""
    try:
        value = validate_input(f"Enter number: ")
        if radians:
            result = op(math.radians(value))
        else:
            result = op(value)
        print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}{Colors.RESET}\n")
    except Exception as e:
        print(f"{Colors.RED}⚠ Error in {op_name}: {str(e)}{Colors.RESET}\n")

def gcd(a: int, b: int) -> int:
    """Calculate Greatest Common Divisor"""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    """Calculate Least Common Multiple"""
    return abs(a * b) // gcd(a, b)

def combination(n: int, r: int) -> int:
    """Calculate nCr"""
    if r > n:
        raise ValueError("r must be <= n")
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def permutation(n: int, r: int) -> int:
    """Calculate nPr"""
    if r > n:
        raise ValueError("r must be <= n")
    return math.factorial(n) // math.factorial(n - r)

def main():
    """Main calculator loop"""
    print_header()
    
    while True:
        print_menu()
        
        try:
            choice = input(f"{Colors.MAGENTA}Enter operation (0-32): {Colors.RESET}").strip()
            
            # Basic Operations
            if choice == "1":
                two_operand_operation(lambda a, b: a + b, "Addition")
            elif choice == "2":
                two_operand_operation(lambda a, b: a - b, "Subtraction")
            elif choice == "3":
                two_operand_operation(lambda a, b: a * b, "Multiplication")
            elif choice == "4":
                b = validate_input("Enter divisor: ")
                if b == 0:
                    print(f"{Colors.RED}⚠ Cannot divide by zero!{Colors.RESET}\n")
                else:
                    a = validate_input("Enter dividend: ")
                    result = a / b
                    print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}{Colors.RESET}\n")
            elif choice == "5":
                two_operand_operation(lambda a, b: a ** b, "Exponentiation")
            elif choice == "6":
                two_operand_operation(lambda a, b: a % b, "Modulo")
            elif choice == "7":
                two_operand_operation(lambda a, b: a // b, "Floor Division")
            
            # Trigonometric
            elif choice == "8":
                single_operand_operation(math.sin, "Sine", radians=True)
            elif choice == "9":
                single_operand_operation(math.cos, "Cosine", radians=True)
            elif choice == "10":
                single_operand_operation(math.tan, "Tangent", radians=True)
            elif choice == "11":
                value = validate_input("Enter number (-1 to 1): ")
                if -1 <= value <= 1:
                    result = math.degrees(math.asin(value))
                    print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}°{Colors.RESET}\n")
                else:
                    print(f"{Colors.RED}⚠ Input must be between -1 and 1{Colors.RESET}\n")
            elif choice == "12":
                value = validate_input("Enter number (-1 to 1): ")
                if -1 <= value <= 1:
                    result = math.degrees(math.acos(value))
                    print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}°{Colors.RESET}\n")
                else:
                    print(f"{Colors.RED}⚠ Input must be between -1 and 1{Colors.RESET}\n")
            elif choice == "13":
                value = validate_input("Enter number: ")
                result = math.degrees(math.atan(value))
                print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}°{Colors.RESET}\n")
            
            # Logarithmic & Power
            elif choice == "14":
                value = validate_input("Enter number (> 0): ")
                if value > 0:
                    result = math.log(value)
                    print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}{Colors.RESET}\n")
                else:
                    print(f"{Colors.RED}⚠ Must be positive{Colors.RESET}\n")
            elif choice == "15":
                value = validate_input("Enter number (> 0): ")
                if value > 0:
                    result = math.log10(value)
                    print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}{Colors.RESET}\n")
                else:
                    print(f"{Colors.RED}⚠ Must be positive{Colors.RESET}\n")
            elif choice == "16":
                value = validate_input("Enter number (> 0): ")
                if value > 0:
                    result = math.log2(value)
                    print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}{Colors.RESET}\n")
                else:
                    print(f"{Colors.RED}⚠ Must be positive{Colors.RESET}\n")
            elif choice == "17":
                value = validate_input("Enter number (≥ 0): ")
                if value >= 0:
                    result = math.sqrt(value)
                    print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}{Colors.RESET}\n")
                else:
                    print(f"{Colors.RED}⚠ Must be non-negative{Colors.RESET}\n")
            elif choice == "18":
                value = validate_input("Enter number: ")
                result = round(value ** (1/3), 10)
                print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}{Colors.RESET}\n")
            elif choice == "19":
                two_operand_operation(lambda a, b: a ** b, "Power")
            
            # Constants & Utilities
            elif choice == "20":
                print(f"{Colors.GREEN}{Colors.BOLD}✓ Pi (π) = {math.pi}{Colors.RESET}\n")
            elif choice == "21":
                print(f"{Colors.GREEN}{Colors.BOLD}✓ Euler (e) = {math.e}{Colors.RESET}\n")
            elif choice == "22":
                value = validate_input("Enter number: ")
                result = abs(value)
                print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}{Colors.RESET}\n")
            elif choice == "23":
                n = validate_input("Enter number (≥ 0): ", int)
                if n >= 0:
                    result = math.factorial(n)
                    print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}{Colors.RESET}\n")
                else:
                    print(f"{Colors.RED}⚠ Must be non-negative{Colors.RESET}\n")
            elif choice == "24":
                degrees = validate_input("Enter degrees: ")
                result = math.radians(degrees)
                print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result} radians{Colors.RESET}\n")
            elif choice == "25":
                radians = validate_input("Enter radians: ")
                result = math.degrees(radians)
                print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}°{Colors.RESET}\n")
            
            # Advanced
            elif choice == "26":
                value = validate_input("Enter number: ")
                result = math.sinh(value)
                print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}{Colors.RESET}\n")
            elif choice == "27":
                value = validate_input("Enter number: ")
                result = math.cosh(value)
                print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}{Colors.RESET}\n")
            elif choice == "28":
                value = validate_input("Enter number: ")
                result = math.tanh(value)
                print(f"{Colors.GREEN}{Colors.BOLD}✓ Result: {result}{Colors.RESET}\n")
            elif choice == "29":
                n = validate_input("Enter n: ", int)
                r = validate_input("Enter r: ", int)
                try:
                    result = combination(n, r)
                    print(f"{Colors.GREEN}{Colors.BOLD}✓ C({n},{r}) = {result}{Colors.RESET}\n")
                except ValueError as e:
                    print(f"{Colors.RED}⚠ Error: {str(e)}{Colors.RESET}\n")
            elif choice == "30":
                n = validate_input("Enter n: ", int)
                r = validate_input("Enter r: ", int)
                try:
                    result = permutation(n, r)
                    print(f"{Colors.GREEN}{Colors.BOLD}✓ P({n},{r}) = {result}{Colors.RESET}\n")
                except ValueError as e:
                    print(f"{Colors.RED}⚠ Error: {str(e)}{Colors.RESET}\n")
            elif choice == "31":
                a = validate_input("Enter first number: ", int)
                b = validate_input("Enter second number: ", int)
                result = gcd(a, b)
                print(f"{Colors.GREEN}{Colors.BOLD}✓ GCD = {result}{Colors.RESET}\n")
            elif choice == "32":
                a = validate_input("Enter first number: ", int)
                b = validate_input("Enter second number: ", int)
                result = lcm(a, b)
                print(f"{Colors.GREEN}{Colors.BOLD}✓ LCM = {result}{Colors.RESET}\n")
            
            # Exit
            elif choice == "0":
                print(f"\n{Colors.MAGENTA}🔮 Powering down calculator...{Colors.RESET}")
                print(f"{Colors.CYAN}Thank you for using Futuristic Scientific Calculator!{Colors.RESET}\n")
                break
            else:
                print(f"{Colors.RED}⚠ Invalid choice. Please enter 0-32.{Colors.RESET}\n")
        
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}Shutting down calculator...{Colors.RESET}")
            break

if __name__ == "__main__":
    main()
