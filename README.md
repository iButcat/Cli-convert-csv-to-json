the cli app look for csv from https://www.football-data.co.uk and
convert it into Json data. It also print all the data in the terminal

Install a virtual env using python by running the command:

python3 -m venv /path/to/new/virtual/environment

when it's done run "source venv/bin/activate"

then you need to install some dependency:

pip3 install requests pandas python-csv

when all the step above are finished, run:

Python3 main.py

The cli will ask you for the url with the .csv extension
