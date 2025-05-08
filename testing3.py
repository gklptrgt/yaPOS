import math

def convert_and_round(tl_amount, exchange_rate):
    # Convert TL to EUR
    raw_euro = tl_amount / exchange_rate
    print(raw_euro)

    # Round up to nearest 0.25
    rounded_euro = math.ceil(raw_euro * 4) / 4

    return round(rounded_euro, 2)



exchange_rate = 43.29  # TL per 1 EUR
tl = 250

euro = convert_and_round(tl, exchange_rate)
print("Converted and Rounded:", euro)