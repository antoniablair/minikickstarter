# Mini Kickstarter

You can git clone the project at: `https://github.com/antoniablair/minikickstarter.git`

To get started, cd into the directory it makes, `minikickstarter`
Run `pip install -r requirements.txt` for setup. You might want to create a virtualenv
first. To run the program, type `python minikickstarter.py`

To run a few nose tests, type `nose kickstarter_tests.py` from the top-level directory.

-
I wrote Mini Kickstarter in Python because I really enjoy working in Python, and I also felt
like it would lend itself well to a CLI application. It's very satisfying to work on an app that's purely focused on code!

This application takes advantage of the built-in python Cmd module to create a prompt for user input, which also automatically
includes a help feature. I tried to keep the number of packages down to a minimum but did take advantage of using Capture() for node tests and added another plugin, `paint`, to add colors. I tried to keep everything organized in a modular fashion. 

To allow the data to persist locally, I set up a Sqlite database, but for a 'real' application I would pick something more heavy-duty on an external server.

Next steps on the to-do list would probably be:

- My functions could definitely be optimized, so I'll be looking to DRY them out some more and make the SQL-related queries better
- These sort of apps seem ideal for quickly grabbing data. Maybe create some helper functions to output data to a spreadsheet and organize it in different ways.
- Add some more fun ways to sort projects and backings, such as by Most Popular, Cheapest, Biggest Backer, etc
- Add Ids and the DateTime created to the Projects
- Create a user model so that there can be admin and users
