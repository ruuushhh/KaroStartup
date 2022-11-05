from google_auth_oauthlib.flow import InstalledAppFlow


scopes =['https://www.googleapis.com/auth/calendar']

def GoogleLogin():
    flow = InstalledAppFlow.from_client_secrets_file('webapp\keys\secret.json', scopes=scopes, redirect_uri='http://localhost:8000')
    credentials = flow.run_local_server(host='localhost',
                                        port=8080,
                                        success_message='The auth flow is complete; you may close this window.',
                                        open_browser=True)
    return credentials
