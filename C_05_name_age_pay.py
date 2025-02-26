# Functions go here
def int_checker(question):
    """Check users enter an integer"""

    error = "Oops - please enter an integer"

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank.  Please try again. \n")


def string_check(question, valid_ans_list, num_letters):
    """Checks that users enter the full word
    or the 'n' letters/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")



# Main routine goes here

# initialise varoiables / non-default options for string checker
payment_ans = ('cash', 'credit')

# loop for testing purposes...
while True:
    print()

    # ask users for their name (and check it's not blank)
    name = not_blank("name: ")

    # Ask for their age and check it's between 12 and 120
    age = int_checker("Age: ")

    # Output errorn message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    # ask users for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} has bought a ticket ({pay_method})")