# Takes in a URL, sends a GET request to the URL and display response body of a 200 status code response
curl -sfL "$1" -X GET
