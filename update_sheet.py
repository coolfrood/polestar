#!/usr/bin/env python3

import os
from googleapiclient.discovery import build

from datetime import date
from google.oauth2.credentials import Credentials
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import json

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_creds():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('creds.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def update_sheet():
    config = json.loads(open('config.json').read())
    credentials = get_creds()
    spreadsheet_id = config['spreadsheet_id']
    API = build('sheets', 'v4', credentials=credentials)
    today = date.today().strftime('%Y-%m-%d')
    sheet = API.spreadsheets()
    body = {
        'requests': [
            {'addSheet': {'properties': {'title': today }}}
        ]
    }
    request = sheet.batchUpdate(spreadsheetId=spreadsheet_id, body=body)
    response = request.execute()
    #print(response)
    sheet_id = response['replies'][0]['addSheet']['properties']['sheetId']

    paste_data = {
        'requests': [
            {'pasteData': {
                'coordinate': {
                    'sheetId': sheet_id,
                    'rowIndex': '0',
                    'columnIndex': '0'
                },
                'data': open('cars.csv').read(),
                'type': 'PASTE_NORMAL',
                'delimiter': ','
            }}
        ]
    }
    request = sheet.batchUpdate(spreadsheetId=spreadsheet_id, body=paste_data)
    response = request.execute()
    print(response)

if __name__ == '__main__':
    update_sheet() 
