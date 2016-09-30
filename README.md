Welcome to Mini Kickstarter!

You can git clone the project at: `https://github.com/antoniablair/minikickstarter.git`
cd into the directory it makes, minikickstarter
Before starting, run `pip install -r requirements.txt` for setup. You might want to create a virtualenv
first.
To run the program, type `python minikickstarter.py`

To run a few nose tests, type `nose kickstarter_tests.py` from the top-level directory.

-
I wrote Mini Kickstarter in Python mostly because I really enjoy working in Python! It's very satisfying
to work on command line interfaces.

This application takes advantage of the built-in python Cmd module to create a prompt that automatically
includes a help feature. I tried to keep the number of packages down to a minimum but did take advantage of
Capture() for node tests and added another plugin to add colors.

To allow the data to persist locally, I set up a Sqlite database, but for
a 'real' application it would need something more heavy-duty on an external server.

Next steps on the to-do list would probably be:

- DRY up the SQL methods
- Create some helper functions to display data in spreadsheets and organize it in different ways for admin
- Add ids and time created to the Projects
- Create a user model so that users can only update their own backings