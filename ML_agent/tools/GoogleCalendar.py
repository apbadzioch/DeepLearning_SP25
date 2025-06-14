import os


class GoogleCalendarTool:
    """
    A class to interact with Google Calendar API.
    """
    
    def __init__(self, credentials_file='credentials.json'):
        """
        Initializes the Google Calendar API client.
        """
        self.credentials_file = credentials_file
        self.service = self.authenticate()

    def authenticate(self):
        """
        Authenticates the user and returns the Google Calendar service.
        """
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request

        SCOPES = ['https://www.googleapis.com/auth/calendar']

        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        return build('calendar', 'v3', credentials=creds)

