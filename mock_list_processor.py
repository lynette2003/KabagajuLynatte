"""
The "List-Processor" Web Scraper (Mock)
Focus: List Comprehensions, Lambda Functions, and map/filter/reduce
No Pandas allowed — pure Python lists & dicts only.
"""

import csv
from functools import reduce


# ---------------------------------------------------------
# Person 1: Load the CSV into a list of dictionaries
# ---------------------------------------------------------
def load_data(filepath):
    """Reads the CSV and returns a list of dicts, one per row.
    Casts Age -> int and Purchase_Amount -> float since CSV values
    come in as strings by default."""
    with open(filepath, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            row['Age'] = int(row['Age'])
            row['Purchase_Amount'] = float(row['Purchase_Amount'])
            data.append(row)
    return data


# ---------------------------------------------------------
# Person 2: filter() + map() -> users over 30 who spent > $100
# ---------------------------------------------------------
def get_high_value_older_users(data):
    filtered = list(filter(
        lambda user: user['Age'] > 30 and user['Purchase_Amount'] > 100,
        data
    ))
    emails = list(map(lambda user: user['Email'], filtered))
    return filtered, emails


# ---------------------------------------------------------
# Person 3: List comprehension -> "Name: Age" for New York users
# ---------------------------------------------------------
def get_new_york_users(data):
    return [f"{user['Name']}: {user['Age']}" for user in data if user['City'] == 'New York']


# ---------------------------------------------------------
# Person 4: reduce() for total purchases + sort for top 5 oldest
# ---------------------------------------------------------
def get_total_purchases(data):
    return reduce(lambda total, user: total + user['Purchase_Amount'], data, 0)


def get_top_5_oldest(data):
    sorted_users = sorted(data, key=lambda user: user['Age'], reverse=True)
    return sorted_users[:5]


# ---------------------------------------------------------
# Person 5: Integrator — runs everything, formats output
# ---------------------------------------------------------
def main():
    data = load_data("C:/Users/LINET/Desktop/RECESS/KabagajuLynatte/user_data.csv")
    print(f"Loaded {len(data)} rows from user_data.csv\n")
    print("=" * 50)

    # Requirement 1 & 2: filter + map
    high_value_users, emails = get_high_value_older_users(data)
    print(f"\n[1] Users over 30 who spent > $100: {len(high_value_users)}")
    print(f"    First 5 emails: {emails[:5]}")

    # Requirement 3: list comprehension
    ny_users = get_new_york_users(data)
    print(f"\n[2] New York users: {len(ny_users)}")
    for line in ny_users[:5]:
        print(f"    {line}")
    if len(ny_users) > 5:
        print(f"    ... and {len(ny_users) - 5} more")

    # Requirement 4: reduce
    total = get_total_purchases(data)
    print(f"\n[3] Total purchase amount (all {len(data)} users): ${total:,.2f}")

    # Requirement 5: sorting
    top_5 = get_top_5_oldest(data)
    print(f"\n[4] Top 5 oldest users:")
    for user in top_5:
        print(f"    {user['Name']} (Age {user['Age']}) - {user['City']}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()