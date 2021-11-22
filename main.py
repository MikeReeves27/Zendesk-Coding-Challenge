import requests
import getpass

# Prompt user to enter their username and password in order to log on
username = input('Please enter your username: ')
password = getpass.getpass(prompt = 'Please enter your password (input hidden for privacy): ')
credentials = username, password

# Start new session and assign login credentials
session = requests.Session()
session.auth = credentials

# Set subdomain
zendesk = 'https://zccmichaelreeves.zendesk.com'

# Declare url for tickets.json file
url = f'{zendesk}/api/v2/tickets.json'

# Declare empty list for storing all ticket values
ticket_list = []

# Run loop to retrieve all tickets in the subdomain
while url:

    # Run validation on subdomain session. If any code other than 200 is returned,
    # display error code, prompt user to log in again, and exit program
    response = session.get(url)
    if response.status_code != 200:
        print(f'Error {response.status_code}: {response.reason}')
        print('Sorry, we are unable to connect to the Ticket Viewer at this time')
        print('Please check your login credentials and try again')
        exit()

    # Store json contents in nested dictionary and then store 'ticket' dictionary in list.
    # Set url to next page in the paginated json file
    data = response.json()
    ticket_list.extend(data['tickets'])
    url = data['next_page']

print('Welcome to the Ticket Viewer, v1.0')


# Declare function for displaying all tickets in json file
def displayAllTickets():

    # Set ticket_index to 0
    ticket_index = 0;

    # Run loop for as long as the ticket_index is less than the number of total tickets in the list
    while ticket_index < len(ticket_list):

        # Print ticket title header
        print()
        print('TICKET #\tPRIORITY\tSTATUS\t\tTIME CREATED\t\t\tREQUESTER ID\t\tSUBJECT')
        print('--------\t--------\t------\t\t------------\t\t\t------------\t\t-------')

        # Run loop in 25-ticket increments to keep in line with pagination style guidelines (25 tickets per page)
        for ticket in range(ticket_index, ticket_index + 25):

            # Print the contents of the ticket, namely: 'id' (ticket ID), 'priority' (ticket priority), 'status' (current status), 
            # 'created_at' (date/time of ticket creation), 'requester_id' (ID of the user who submitted the ticket), 'subject' (subject/title of the ticket)
            print(str(ticket_list[ticket]['id']) + '\t\t' + str(ticket_list[ticket]['priority']) + '\t\t' + ticket_list[ticket]['status'] + '\t\t' + ticket_list[ticket]['created_at'] + '\t\t' + str(ticket_list[ticket]['requester_id']) + '\t\t' + ticket_list[ticket]['subject'])

        # Increment ticket_index by 25
        ticket_index += 25

        # After printing each page, print the number of remaining tickets and prompt the user if they want to print next page
        if ticket_index < len(ticket_list):
            print()
            tickets_remaining = len(ticket_list) - ticket_index
            continue_printing = input(f'There are {tickets_remaining} records remaining in this list. Display next page? (Y/N)\n').lower()

            # Run loop to perform validation on user input
            while True:

                # If user has entered a 'y' or an 'n', validation is complete
                if continue_printing == 'y' or continue_printing == 'n':
                    break

                # If not, prompt user to enter input again
                continue_printing = input('Invalid input! Please type Y or N\n').lower()

            # If user entered a 'y', continue to next page of ticket_list. Otherwise, return to main menu
            if continue_printing == 'y':
                continue
            else:
                break

    # Display message saying how many tickets were printed in total
    print()
    print(f'Successfully displayed {ticket_index} of {len(ticket_list)} records')


# Declare function for searching for an individual ticket number
def searchForTicket():

    # Prompt user to enter a ticket number
    ticket_number = input('Please enter a ticket number:\n')

    # Perform input validation. If input is a number, cast it as an integer so that it can match an actual ticket number's data type
    if ticket_number.isdigit():
        ticket_number = int(ticket_number)

    # Otherwise, print error message and return to main menu
    else:
        print('Invalid input! Ticket number must be numeric')
        return

    # Set a boolean for if the ticket exists in the list. Set to False by default
    ticket_exists = False

    # Run loop to check each ticket in the ticket_list
    for ticket in ticket_list:

        # If the ticket number exists in the list and is paired with a ticket id (that is, the value the user inputs is not
        # coincidentally a matching value for a different key), print the relevent fields. Set ticket_exists boolean to true and break loop
        if ('id', ticket_number) in ticket.items():
            print()
            print('TICKET #\tPRIORITY\tSTATUS\t\tTIME CREATED\t\t\tREQUESTER ID\t\tSUBJECT')
            print('--------\t--------\t------\t\t------------\t\t\t------------\t\t-------')
            print(str(ticket['id']) + '\t\t' + str(ticket['priority']) + '\t\t' + ticket['status'] + '\t\t' + ticket['created_at'] + '\t\t' + str(ticket['requester_id']) + '\t\t' + ticket['subject'])
            ticket_exists = True
            break

    # If the ticket is not in the list, print message for user
    if not ticket_exists:
        print('Ticket number not found')
    

# Main menu
# Run loop so that user can run program as long as they need
while True:

    # Print menu selection options
    print()
    print('Please make a selection from the menu:')
    print('-- Type 1 to view all tickets')
    print('-- Type 2 to search for a ticket')
    print('-- Type 3 to exit the Ticket Viewer')
    print()

    # Prompt user to enter their selection (between 1 and 3)
    menu_selection = input('Selection: ')
    print()

    # If user enters 1, display all tickets
    if menu_selection == '1':
        displayAllTickets()

    # If user enters 2, search for a ticket
    elif menu_selection == '2':
        searchForTicket()

    # If user enters 3, exit program
    elif menu_selection == '3':
        print('Thank you for using the Ticket Viewer!')
        exit()

    # If user enters anything else, display error and run loop again
    else:
        print('Invalid selection! Please type 1, 2, or 3')


