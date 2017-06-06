from pyramid.response import Response
from pyramid.view import view_config
import requests
from bs4 import BeautifulSoup
import json
from pyramid.httpexceptions import HTTPBadRequest
import validators
from tld import get_tld

# Serves the home page template, which is the user interface for the application
@view_config(route_name='home', renderer='templates/mytemplate.pt')
def home(request):
    return {'project': 'scraper'}

# The scraper route
# Takes a json object with a wikipedia URL submitted via post
# The URL will then be validated, if validation passes
# The wikipedia page will be scraped for a Table of Contents and
# Returned to the calling client
@view_config(route_name='scraper', renderer='json')
def scraper(request):
	# Get the posted URL
    url = request.json_body['url'] 

    # Verify that the URL is valid  
    if not validators.url(url):
    	request.response.status = 400
    	return {'error': 'Invalid URL.'}

    # Verify that that the URL points to the wikipedia domain
    parsed_url = get_tld(url, as_object=True)
    if parsed_url.domain != "wikipedia":
    	request.response.status = 400
    	return {'error': 'Only wikipedia URLs are allowed.'}    	

    # Get the page using the posted url
    page = requests.get(url)
    # Intansiate beautiful soup with the html content
    soup = BeautifulSoup(page.content, 'html.parser')
    # Attenmpt to find a table of contents(toc) id
    toc = soup.find(id="toc")

    # Check if a toc could be found
    if (str(toc) == "None"):
    	request.response.status = 400
    	return {'error': 'Table of Contents could not be found.'}     	
    else:	
        # return the toc
        return Response(str(toc))
