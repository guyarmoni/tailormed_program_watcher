# TailorMed Assistance Program Watcher

## Entry Points
**Scraper.py**: Creates a DB entity for Assistance Programs, or updates the DB if exists; updates the relevant assistance programs using a scraper on the foundation’s website.

**App.py**: Creates a UI view that contains the most updated assistance programs, and their status, available for the patients at all times.

## Files
### parse_utils.py
Contains parsing-related functions.

**Technologies:**
- Uses *urlib.request* module for opening and reading URLs.
- Uses *Beautiful Soup* library for parsing the HTML scraped from the website.

### query_utils.py
Contains query and DB-related functions.

**Technologies:**
- Uses *sqlite3* module for creating, filling and updating the DB.

### app.py
Application for the UI presenting the information from the DB.

**Technologies:**
- Uses *Flask* web framework.

### assistance_program.py
Contains the AssistanceProgram class, used for creating instances of assistance programs scraped from the website. Each instance holds all the relevant information of the specific program it represents.
