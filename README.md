# scraper
a Wikipedia table of contents scraper, built using Pyramid.  Insert a link to a Wikipedia article into the search box at the top and if there is a table of contents the page will be scraped and the table displayed.<br />
<br />
# Dependencies
Python 2.7<br />
pip<br />
<br />
# Setup
git clone git@github.com:HAASLEWER/scraper.git<br />
cd scraper<br />
pip install -e . <br />
py.test scraper/tests.py -q<br />
pserve development.ini --reload<br />