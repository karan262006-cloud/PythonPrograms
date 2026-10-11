
def find_duplicates(numbers):
    duplicates = []
    seen = set()

    for number in numbers:
        if number in seen:
            if number not in duplicates:
                duplicates.append(number)
        else:
            seen.add(number)

    return duplicates
