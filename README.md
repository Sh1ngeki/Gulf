# Gulf

## Importing necessary modules:
- The script imports the required modules, including time, requests, random, BeautifulSoup, csv, and sqlite3.

## URL and request parameters:
- The url variable stores the URL of the target website.
- The payload dictionary is used to specify the page number for the request.
- The h dictionary sets the 'Accept-Language' header to 'en-US' to request English content.

## Establishing a connection to the SQLite database:
- The script connects to a SQLite database file named 'Petrol.sqlite' using sqlite3.connect().
- The connection object is stored in the conn variable.
- A cursor object is created using conn.cursor() and stored in the cur variable.

## Creating a table in the database:
- The script executes a CREATE TABLE statement using cur.execute() to create a table named 'Petrol' if it doesn't already exist.
- The table has columns for date and various fuel types.

## Opening a CSV file:
- The script opens a file named 'Petrol.csv' in write mode and uses csv.writer() to create a CSV writer object named csv_obj.
- The header row is written to the file.

## Scraping data from multiple pages:
- The script enters a while loop that iterates until the 'page' value in payload reaches 6.
- Inside the loop, a GET request is sent to the target URL with the appropriate page parameter and headers.
- The response content is extracted and parsed using BeautifulSoup.
- The script finds the specific HTML elements that contain the fuel price data.
- For each row of fuel price data, the script extracts the values and assigns them to variables.
- The script attempts to convert the fuel prices from strings to floating-point numbers. If a value cannot be converted, the iteration continues.
- The data is inserted into the SQLite database using cur.execute().
- The data is also written as a row to the CSV file using csv_obj.writerow().
-The script closes the CSV file using file.close().
- Changes made to the SQLite database are committed using conn.commit().
- The connection to the SQLite database is closed using conn.close().

The code scrapes the fuel price data from the website, saves it in both a SQLite database and a CSV file, and repeats this process for multiple pages.

![g](https://github.com/Sh1ngeki/Gulf/assets/115181439/173dd5f2-2d54-4b49-895e-02ff38a74089)


