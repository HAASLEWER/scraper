// Inject pace
$(document).ajaxStart(function() { Pace.restart(); });

$(document).ready(function() {
	// Use ajax to request the scrape from the Pyramid backend
	$("#search_form").submit(function(e) {	
		// Define our scrape route
	    var url = "/scraper";
	    // Create our payload with the url entered in the search bar, 
	    // All validation occurs in pyramid
	    var payload = JSON.stringify({url: $("#search").val()});	    

	    // Send our request
	    $.ajax({
			type: "POST",
			contentType: "application/json",
			url: url,
			data: payload,
			success: function(data) { // Table of contents found, let's display it.		
				// Display the Table of Contents
				$('.dynamic_content').html('<div class="center-align">' + data + '</div>');
			},
			error: function(data) { // An error occurred, inform the user
				// Parse the json response so that we can use it as an object
				data = JSON.parse(data.responseText);
				// Display the error
				$('.dynamic_content').html('<h4 class="center-align">Error: ' + data.error + '</h4>');
			}	           
	    });

	    e.preventDefault(); // Prevent the page from reloading after the submit, because ajax ;-)
	});
});