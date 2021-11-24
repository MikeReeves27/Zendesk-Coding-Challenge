import unittest

from zendesk_tickets import menu_selection, login, download_tickets

class TestZendeskTickets(unittest.TestCase):

    def test_menu_input(self):
        valid_input = ['1', '2', '3']
        user_input = menu_selection()
        self.assertIn(user_input, valid_input, 'Menu input must be an integer between 1 and 3 (inclusive)')

    def test_login_input(self):
        login_input = login()
        self.assertIn('@', login_input[0], 'Username must contain a valid email address')

    def test_list_is_empty(self):
        ticket_list = download_tickets(login())
        isEmpty = False
        if not ticket_list:
            isEmpty = True
        self.assertFalse(isEmpty, 'List of tickets is empty')

    def test_ticket_data_type(self):
        ticket_list = download_tickets(login())
        for ticket in ticket_list:
            self.assertIsInstance(ticket, dict, 'Tickets are not of type: dictionary')

    
if __name__ == '__main__':
    unittest.main()
    
