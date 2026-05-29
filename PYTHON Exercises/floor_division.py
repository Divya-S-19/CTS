def split_bill(total_bill, people):
    if total_bill <= 0:
        return "Invalid bill amount"

    if people <= 0:
        return "Invalid number of people"

    share = total_bill // people

    return f"Individual Share: {share}"


total_bill = 1250
people = 4

result = split_bill(total_bill, people)
print(result)