import requests

credentials = '---', '---'
session = requests.Session()
session.auth = credentials
zendesk = 'https://zccmichaelreeves.zendesk.com'

url = f'{zendesk}/api/v2/tickets.json'

ticket_list = []

while url:
    response = session.get(url)
    if response.status_code != 200:
        print(f'Error {response.status_code}: {response.reason}')
        print('Sorry, we are unable to connect to the Ticket Viewer at this time')
        print('Please check your login credentials and try again')
    data = response.json()
    ticket_list.extend(data['tickets'])
    url = data['next_page']




def displayAllTickets():
    start = 0;

    print('Ticket #' + '\tTime created' + '\t\t\tRequester ID' + '\t\tSubject')
    while start < len(ticket_list):
        for x in range(start, start + 25):
            print(str(ticket_list[x]['id']) + '\t\t' + ticket_list[x]['created_at'] + '\t\t' + str(ticket_list[x]['requester_id']) + '\t\t' + ticket_list[x]['subject'])
        start += 25
        if start < len(ticket_list):
            user_continue = input('There are ' + str(len(ticket_list) - start) + ' records remaining in this list. Display next page? (Y/N)\n').lower()
            while True:
                
                if user_continue == 'y' or user_continue == 'n':
                    break
                user_continue = input('Invalid input! Please type Y or N\n').lower()
            
            if user_continue == 'y':
                continue
            else:
                break

displayAllTickets()
