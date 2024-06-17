def cash_up_till(till):
    denominations = {
        '1p': 0.01,
        '2p': 0.02,
        '5p': 0.05,
        '10p': 0.10,
        '20p': 0.20,
        '50p': 0.50,
        '£1': 1.00,
        '£2': 2.00,
        '£5': 5.00,
        '£10': 10.00,
        '£20': 20.00,
        '£50': 50.00
    }

    total = sum(quantity * denominations[denomination] for denomination, quantity in till.items())
    return f"£{total:.2f}"

# Example usage:
till = {
    '1p': 100,
    '2p': 50,
    '5p': 20,
    '10p': 10,
    '20p': 5,
    '50p': 2,
    '£1': 1,
    '£2': 0,
    '£5': 0,
    '£10': 0,
    '£20': 0,
    '£50': 0
}

print(cash_up_till(till))  # Outputs: ££3.70