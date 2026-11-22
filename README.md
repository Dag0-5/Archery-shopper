# Archery Shopper

This is a shopping tool designed to help me find the best prices on archery gear. 
It works by checking certain websites found in the archery urls file for the closest match to the name and type of the item and returning related information.
It either checks the sites by searching their sitemaps or, when none is found, searching the site itself.

## Project Setup

Use the run.ps1 file to install the requirements and run the system. This should present a link to a localhost address.
Press this link to be taken to the site.

## Future developments

This project may be expanded and moved to its own server instead of using localhost.

## Known issues

#### Sometimes prices will display £0.00 even thought the site is found. 
This is usually due to being rate limited. Wait and then try again

#### A product is shown that has no relation to the item searched for. 
This is usually due to a search stopping early due to no match being found.
Try again with a more detailed name. Some sites may not stock the item being searched for. 