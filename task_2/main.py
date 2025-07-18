import re
from typing import Callable


def generator_numbers(text: str):
    pattern = r"\b\d+\.\d+\b" 
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    total = sum(
        func(text)
    ) 
    return total


text = "The employee's total income consists of several parts: 1000.01 as the main income, supplemented by additional income of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
