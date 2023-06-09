# news_reporter

Every company needs to stay updated with the recent news and developments about their rivals. To speed up the process it
would be very helpful if their exists a web scraper along with an application that scrapes the web for the recent news, maintains a 
database for the news and the application which provides company wise news datewise.

## The project has 2 components.
### 1.

The first component scrapes the web, collects them and stores it in a mongodb database. It keeps track of every time the scraper is run 
as a batch job along with the scraped news in different collections.

### 2.

A Django rest framework has been set up which allows API calls for the scraper to directly update the news database. It also helps in
running the application by support GET requests to display company wise news according to the date range selected.
