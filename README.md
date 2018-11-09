# read-all-about-it
Simple, configurable command line news aggregator. Allows users to favourite 
news outlets, whose current headlines are displayed when the app is run.

### Commands
Please use ```help``` for a full list of commands, and help <some command> to 
get a detailed description.
preview: Displays a short preview of a particular story.
open: Opens a particular story in the systems default web browser.
add: adds a news source to the users preferences so news from this agency is displayed on startup.
remove: removes a news source from the users preferences.
sps: Standing for 'stories per source', allows the user to specify the number of headlines to
display per news source.
random: Fetches a random headline from a random news source.
refresh: displays current headlines

To try out the software, or setup the project to work on the code, follow the steps below.

## Setup
First, check you have python 3.7 installed by opening a terminal and entering:
```
python3 --version
``` 
If you haven't got it, grab it <a href="https://www.python.org/downloads/">here</a>.
Next, check if you have pip installed. Enter:
```
pip --version
```
If you haven't got it, grab it <a href="https://pip.pypa.io/en/stable/installing/">here</a>
Now check if you've got pipenv (a python package manager) installed by entering:
```
pipenv --version
```
If not, grab it by entering:
```
pip install --user pipenv
```

##Installation
Get an API key from https://newsapi.org.
Download the source from this repository.
In a terminal, navigate to the directory containing the source and enter:
```
pipenv install
```
to install dependencies. Now rename example-config.json to config.json,
enter your own API key and save the file. With the terminal in your project 
directory, enter:
```
pipenv run main.py
```
On sucess, you should be greeted with "Welcome to the news!"

