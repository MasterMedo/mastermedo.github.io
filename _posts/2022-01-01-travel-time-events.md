---
category: projects
github: https://github.com/MasterMedo/travel-time-events
---
## Short description
Travel Time Events is a Google Calendar Add-on application that creates travelling events between two calendar events that have a location.
It calculates travel time from the origin location to the destination location by utilising the Google Maps API and creates a travel event in the "Travel time" calendar.

## Detailed description
Travel Time Events creates a user calendar by the name "Travel time".
On every calendar change (edit or create event), the application gets all
events from all of the user's calendars from yesterday to two weeks in the
future. The events are ordered and a timeline of location changes is
constructed. Between every location change, a Travel Time event is created
in the Travel Time Calendar. The Travel Time event duration is calculated
by using the Google Maps API to calculate the commute/travel time between
two locations using the preferred means of transport.

Google Maps executed query results are saved in the user cache to reduce
the number of calls to the API. Travel Time events are tied to real events
in the user's calendars. That allows the user to change the original event,
and Travel Time events are going to be updated automatically.

# How does it work?
The user creates two events less than 4 hours apart with different locations.
On every calendar update, the application calculates the duration of the trip using the Google Maps API and creates Travel Time events in the Travel Time Calendar.

# Privacy policy
User data is not shared. The application has no external dependencies, and
does not use any external APIs. The only APIs used by the application are
Google Cache service, Maps API and Calendar API.

# Pricing
The application is free.

# OAuth Scopes
"https://www.googleapis.com/auth/calendar"
Explanation of the requirements of the application:
- get all user's calendars
- get all calendar events
- create "Travel time" calendar
- create events in "Travel time" calendar
- edit events in "Travel time" calendar
- delete events in "Travel time" calendar
