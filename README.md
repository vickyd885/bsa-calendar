# BSA Events Calendar

A simple web scrapped that scrapes the BSA website and populates a calendar
with all the events.

Users can then subscribe to the calendar etc than having to refer to the
hard to find events page constantly.

Public URL to calendar: `https://calendar.google.com/calendar/embed?src=bjbks99te6h18vdpdkkq9mqp4g%40group.calendar.google.com&ctz=Europe%2FLondon`

Public address in iCal format: `https://calendar.google.com/calendar/ical/bjbks99te6h18vdpdkkq9mqp4g%40group.calendar.google.com/public/basic.ics`

## Folder Structure

`bsa_scraper` is a module which returns a list of events scraped and cleaned from the BSA website. This will be used for an
API in the future.

Also planning to add support for local support groups

`gcal_api` is a module which provides access to the gcal functionality. To update the calendar, just call `python gcal_api/update_calendar.py`

## Installation & Use

```shell
pip install -r requirements.txt
# Update the calendar with events
python gcal_api/update_calendar.py
```
