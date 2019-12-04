from collections import defaultdict


def check_password(password: int):
    # Assume it matches
    increase = True
    double = False

    # Convert to a string to make it easier to walk
    pword = str(password)

    # Save the previous digit. At the start, that's zero
    prev_digit = 0
    for i in range(len(pword)):
        # Check if the current digit is larger or the same as previous
        # If anything drops, it's no bueno, hence the `and`
        increase = increase and (int(pword[i]) >= prev_digit)

        # Check if there is a double in there
        # Any two digits can be a double, hend the `or`
        double = double or (int(pword[i]) == prev_digit)

        # Next time around, this will be the previous digit
        prev_digit = int(pword[i])

    # If both are true, we have a match!
    return increase and double


def check_doubles(password: int):

    # Set up a dictionary to hold digit counts
    digit_count = defaultdict(int)

    # For each digit we find, add one to the count
    for digit in str(password):
        digit_count[digit] += 1

    # Assume we don't have a double
    has_double = False

    # Check every value in the dictionary for a double
    # We just need one, hence the `or`
    for k, v in digit_count.items():
        has_double = has_double or (v == 2)

    return has_double


if __name__ == "__main__":
    # The low and hi ends of our range
    lo, hi = 156218, 652527

    # Collection of passwords that fit
    passwords = []

    # Check each one for validity
    for i in range(lo, hi + 1):
        if check_password(i):
            passwords.append(i)

    print(f"Number of matching passwords: {len(passwords)}")

    # We only need to check the valid passwrods for the additional criterion[s]
    good_passwords = []
    for pword in passwords:
        if check_doubles(pword):
            good_passwords.append(pword)

    print(f"Number of good passwords: {len(good_passwords)}")
