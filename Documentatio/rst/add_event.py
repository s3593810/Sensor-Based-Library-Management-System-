# pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client httplib2
# python3 add_event.py --noauth_local_webserver

# Reference: https://developers.google.com/calendar/quickstart/python
# Documentation: https://developers.google.com/calendar/overview

# Be sure to enable the Google Calendar API on your Google account by following the reference link above and
# download the credentials.json file and place it in the same directory as this file.

# from __future__ import print_function
# from datetime import datetime
# from datetime import timedelta
# from googleapiclient.discovery import build
# from httplib2 import Http
# from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = "https://www.googleapis.com/auth/calendar"
# store = file.Storage("token.json")
# creds = store.get()
# if(not creds or creds.invalid):
#     flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
#     creds = tools.run_flow(flow, store)
# service = build("calendar", "v3", http=creds.authorize(Http()))

class Add_event:

    """
    This class helps creating google calender events upon
    borrowing a book from the library and removes the event 
    upon returning it.
    ...

    Methods
    -------
    list_events()
        This method shows all the events in google calender.
    
    insert(name , bookid, status , date, book, lmsid)
        This method helps creating an event upon reciving
        the parameters as name, bookid, status, date, book and lmdid.


    """
     
    def list_event(self):
        """
        Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user"s calendar.
        """

        # Call the Calendar API.
        # now = datetime.utcnow().isoformat() + "Z" # "Z" indicates UTC time.
        print("Getting the upcoming 10 events.")
        # events_result = service.events().list(calendarId = "primary", timeMin = now,
            # maxResults = 10, singleEvents = True, orderBy = "startTime").execute()
        # events = events_result.get("items", [])

        # if(not events):
            # print("No upcoming events found.")
        # for event in events:
            # start = event["id"].get()
            # print(start)

    def insert(self, name , bookid, status , date, book, lmsid):
        """
        name: str
            persons name.
        bookid: int
            id number of the book.
        status: str
            Current status of the book.
        date: str
            Date the book was taken
        
        book: str
            name of the book.
        lmsid: int
            Auto generated id.

        """
        print(date)
        print(book[0][0])
        #boo = book.fetchone()
        # borrow_date = datetime.strptime(date,"%Y-%m-%d %H:%M:%S")
        # print(borrow_date)
        # return_date = (borrow_date + timedelta(days = 10)).strftime("%Y-%m-%d")
        # print(return_date)
        borrow_date = borrow_date.strftime("%Y-%m-%d")
        print(borrow_date)
        print(name )
        email = "suneeth.g.s@gmail.com"
        time_start = "{}T06:00:00+10:00".format(borrow_date)
        # time_end = "{}T07:00:00+10:00".format(return_date)
        event = {
            "id":"As",
            "summary": book[0][1]+ " - " +book[0][2],
            "location": "State Library Victoria",
            # "description": "Library - Book Borrowed - Return Date = "+return_date,
            "start": {
                # "dateTime": time_end,
                "timeZone": "Australia/Melbourne",
            },
            "ogranizer": {
                "id": lmsid,
                "email": email,
                "displayName": name[0][0]+ " "+name[0][1],
                "self": True,
            },
            "end": {
                # "dateTime": time_end,
                "timeZone": "Australia/Melbourne",
            },
            "reminders": {
                "useDefault": False,
                "overrides": [
                    { "method": "email", "minutes": 5 },
                    { "method": "popup", "minutes": 10 },
                ],
            }
        }

        # event = service.events().insert(calendarId = "primary", body = event).execute()
        self.list_event()
        print("Event created: {}".format(event.get("htmlLink")))


