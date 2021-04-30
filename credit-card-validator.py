card_number = input("Please enter the card number: ").strip().replace(" ", "")
card_number = list(card_number)
checking_digit = int(card_number.pop()) #removes last element and mutates the list.
card_number.reverse()
processed_card_number = []
for index, digit in enumerate(card_number): #Adds index to list elements in the form of tuple.
    if index % 2 == 0:
        doubled_digit = int(digit) * 2
        if doubled_digit > 9:
            doubled_digit = doubled_digit - 9
        processed_card_number.append(doubled_digit)
    else:
        processed_card_number.append(int(digit))

total = checking_digit + sum(processed_card_number)
if total % 10 == 0:
    print("Card number is valid")
else:
    print("Card number is invalid")
