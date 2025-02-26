# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decortion
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_ans_list=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid response"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:
            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")



def instructions():
    make_statement("Discipline", "😊")

    print('''
    
For each ticket holder enter..)
- Their mame
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the
ticket cost (and the profit)

Once you have either sold all of the tickets or entered the
exit code ('xxx'), the program will display the ticket
sales information and write the data to a text file

It will also choose one lucky ticket holder who wins the 
draw (their ticket is free).

    ''')
