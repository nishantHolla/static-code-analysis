"""
Inventory management system for adding, removing, and tracking stock items.
"""

import json
from datetime import datetime
from typing import Dict, List


def add_item(
    stock_data: Dict[str, int],
    item: str,
    qty: int = 0,
    logs: List[str] | None = None
) -> None:
    """Add quantity of an item to stock and record it in logs."""
    if not item:
        return

    if logs is None:
        logs = []

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(stock_data: Dict[str, int], item: str, qty: int) -> None:
    """Remove quantity of an item from stock. Deletes item if quantity <= 0."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: Tried to remove '{item}' which is not in stock.")
    except TypeError:
        print(f"Error: Invalid quantity type for '{item}'. Expected integer.")


def get_qty(stock_data: Dict[str, int], item: str) -> int:
    """Return quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(filename: str = "inventory.json") -> Dict[str, int]:
    """Load stock data from a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with empty inventory.")
        return {}
    except json.JSONDecodeError:
        print(f"Error reading '{filename}'. File may be corrupted.")
        return {}


def save_data(
        stock_data: Dict[str, int],
        filename: str = "inventory.json"
        ) -> None:
    """Save current stock data to a JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=2)
    except OSError as e:
        print(f"Error saving file '{filename}': {e}")


def print_data(stock_data: Dict[str, int]) -> None:
    """Print all items in stock."""
    print("\nItems Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(
        stock_data: Dict[str, int],
        threshold: int = 5
        ) -> list[str]:
    """Return a list of items with quantity below the given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main() -> None:
    """Demonstration of inventory operations."""
    stock_data: Dict[str, int] = {}
    logs: list[str] = []

    add_item(stock_data, "apple", 10, logs)
    add_item(stock_data, "banana", -2, logs)
    add_item(stock_data, "mango", 5, logs)
    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)

    print("Apple stock:", get_qty(stock_data, "apple"))
    print("Low items:", check_low_items(stock_data))

    save_data(stock_data)
    stock_data = load_data()
    print_data(stock_data)

    print("\nActivity Log:")
    for log_entry in logs:
        print(" -", log_entry)


if __name__ == "__main__":
    main()
