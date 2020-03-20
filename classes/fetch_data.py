from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class post:
    timestamp: str
    poster: str
    subject: str
    post_type: str
    message: str

    def __init__(self, timestamp, poster, subject, post_type, message):
        self.timestamp = timestamp
        self.poster = poster
        self.subject = subject
        self.post_type = post_type
        self.message = message

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
CMS_SPREADSHEET = '1o83U8PHM4Hz7J8hlz28fMXLfp4ulrqNEnYVgkC8E5DI'
POST_RANGE = 'Posts!A2:E'

def set_up():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('classes/token.pickle'):
        with open('classes/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'classes/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
        
    service = build('sheets', 'v4', credentials=creds)

    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=CMS_SPREADSHEET,
                                range=POST_RANGE).execute()
    values = result.get('values', [])
    posts = []

    if not values:
        print('No data found.')
    else:
        for row in values:
            new_post = post(timestamp = row[0], poster = row[4], subject = row[1], post_type=row[2], message=row[3])
            posts.append(new_post)
        return posts