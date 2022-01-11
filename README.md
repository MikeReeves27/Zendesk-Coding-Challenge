# Zendesk Coding Challenge
This program was created as part of a coding challenge for a **Zendesk Software Engineering internship**. 
The program prompts the user to log in with their credentials (username and password), then retrieves a list of Zendesk tickets from a json file stored in the user's account's subdomain. 
The program then becomes an interactive CLI application in which the user can view and search for tickets.


# Technologies used
- Python 3.9


# How to run
### Installing Python

1. Navigate to the system's Command Line and check to see if Python is already installed with the below command. If a Python version number appears, it is already installed on the system.

<pre><code>python --version</code></pre>

2. If no such version number is given, Python will need to be installed. It can be downloaded [here](https://www.python.org/downloads/)
3. Once Python installation is finished, install the *Requests* library for Python via the Command Line:

<pre><code> python -m pip install requests </code></pre>

*Note that the pip function is included with Python 3.4 and above. Previous versions may require an external download*

### Installing Git

1. To download this code repository, Git will need to be installed on the system. The below command can be used to check if Git is already installed. If a Git version number appears, it is already installed on the system.

<pre><code>git --version</code></pre>

2. If no such version number is given, Git will need to be installed. It can be downloaded [here](https://git-scm.com/downloads)

### Running the Ticket Viewer

1. Once both Python and Git are installed, download the code repository via the Command Line:

<pre><code> git clone https://github.com/MikeReeves27/Zendesk-Coding-Challenge </code></pre>

2. To start the main program, navigate to the destination folder on computer and run the following code:

<pre><code> zendesk_tickets.py </code></pre>

### Running the Unit Tests

- To run full tests, run the following code on the Command Line:

<pre><code> test_zendesk_tickets.py </code></pre>

- To run tests on individual functions, run the following code on the Command Line:

<pre><code> python -m unittest test_zendesk_tickets.TestZendeskTickets.<b><i>function_name</i></b> </code></pre>

Replace the <b><i>function_name</i></b> with any of the following unit test functions:

<code>test_menu_input<p>
test_login_input<p>
test_list_is_empty<p>
test_ticket_data_type</code>

# What the Ticket Viewer does
The Ticket Viewer is a program that connects to a user's Zendesk account. It's assumed the user will have already created an account. Upon running the program, the user will be
prompted to enter their username and password. If these are correct, the program will connect to the Zendesk subdomain and extract the tickets.json file. This file contains
all of the user's tickets in a nested dictionary. The program stores each individual ticket dictionary in a list. After this is complete, the user will be presented with a menu
that lets them choose one of three options. The first option is to display all tickets by printing relevent ticket information to the console. Tickets are displayed in rows
of 25 to keep in line with pagination guidelines. The second option is to search for an individual ticket, which takes input from the user. The third option is
to exit the program.

# What the Unit Test Cases check for
There are four unit test functions in this program:

1. <code>test_menu_input</code> checks that the user's input in the menu is a valid integer between 1 and 3 (exclusive). Examples of incorrect input: -1, X
2. <code>test_login_input</code> checks that the user's username input is a valid email address by containing an @ character. Example of incorrect input: test.test.com
3. <code>test_list_is_empty</code> checks the list in which the dictionaries are stored is not empty.
4. <code>test_ticket_data_type</code> checks that the values inside the list are indeed dictionaries.
