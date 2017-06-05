# scraper
a Wikipedia table of contents scraper, built using Pyramid.  Insert a link to a Wikipedia article into the search box at the top and if there is a table of contents the page will be scraped and the table displayed.<br />
<br />
# Dependencies
Python 2.7
pip

# Installation
Installation instructions tested on Ubuntu 16.04 please visit the following link for instructions for other operating systems: http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/install.html
Installation performed on a virtual environment
sudo apt-get update
sudo apt-get install python3-dev python3-setuptools




sudo apt-get update
sudo apt-get install python-pyramid
sudo pip install chameleon
sudo apt install python-pytest
sudo pip install requests
sudo pip install beautifulsoup
sudo pip install validators
sudo pip install tld

# Setup
git clone git@github.com:HAASLEWER/scraper.git
cd scraper
pip install -e .
pserve development.ini --reload