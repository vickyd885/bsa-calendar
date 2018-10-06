import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import gcal_api
import bsa_scraper

if __name__ == '__main__':
    events = bsa_scraper.events_scraper.scrape_for_events()
    print("Number of events scrapped: ", len(events))
    gcal_api.gcal_api.manipulate_events(events)
