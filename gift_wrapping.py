import re
import sys


def get_user_input():
    print("Paste your puzzle input below, and end with an empty line to start the execution of the program.")
    lines = []

    while True:
        line = input()

        if line:
            lines.append(line)
        else:
            break

    return '\n'.join(lines)


def get_tablet_format(user_input):
    match = re.search(r"Tablet\s(\d+)x(\d+)x(\d+)", user_input)

    if match is None or len(match.groups()) is not 3:
        return None

    return [int(format) for format in match.groups()]


def get_phone_format(user_input):
    match = re.search(r"Phone\s(\d+)x(\d+)x(\d+)", user_input)

    if match is None or len(match.groups()) is not 3:
        return None

    return [int(format) for format in match.groups()]


def get_total_tablets(user_input):
    match = re.findall(r"(\d+) tablets", user_input)

    if match is None:
        return None

    # We need to cast our entire tablet_count list to integers before
    # we can invoke the sum, thus we do that with an inline for-loop
    return sum([int(tablet_count) for tablet_count in match])


def get_total_phones(user_input):
    match = re.findall(r"(\d+) phones", user_input)

    if match is None:
        return None

    # We need to cast our entire phone_count list to integers before
    # we can invoke the sum, thus we do that with an inline for-loop
    return sum([int(phone_count) for phone_count in match])


def calculate_packaging_paper_required_in_meter(product_format, amount):
    product_format.sort()

    # We only need the 2 smallest sizes, since the width didn't matter.
    # Also we must not forget to multiply by 2 since we need to cover both sides
    outline = (product_format[0] + product_format[1]) * 2
    outline *= 1.05

    # Lastly divide by 100 to make sure that we get the total value in meters (and not
    # in centimeters)
    return (outline * amount) / 100


if __name__ == "__main__":
    user_input = get_user_input()

    tablet_format = get_tablet_format(user_input)
    phone_format = get_phone_format(user_input)

    amount_of_tablets = get_total_tablets(user_input)
    amount_of_phones = get_total_phones(user_input)

    if tablet_format is None or phone_format is None or amount_of_tablets is None or amount_of_phones is None:
        sys.exit("Wasn't able to fully process the given input, terminating the script.")

    tablet_packaging_paper_required = calculate_packaging_paper_required_in_meter(tablet_format, amount_of_tablets)
    phone_packaging_paper_required = calculate_packaging_paper_required_in_meter(phone_format, amount_of_phones)

    total_amount_of_packaging_paper_required = tablet_packaging_paper_required + phone_packaging_paper_required

    print("Total amount of packaging paper required: {0}m".format(total_amount_of_packaging_paper_required))
