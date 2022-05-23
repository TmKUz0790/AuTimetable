from googleapiclient.discovery import build
from datetime import datetime

from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1z20YDk7qpRijn3jkCGQx65u_1OsFB43Fn2iJaCtfjcY'
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range="sales!A1:B10").execute()
values = result.get('values',[])
aoa = [["1/1/2022",4000],["4/4/2022",3000],["7/12/2022",7000]]
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheets2!B2",
                                valueInputOption="USER_ENTERED" , body={"values":aoa})
result = service.spreadsheets().values().get(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range="sales!A1:A6").execute()
rows = result.get('values', [])
result2 = service.spreadsheets().values().get(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range="sales!B1:B5").execute()
rows2 = result2.get('values', [])
print("                     TODAYS TIMETBLE")
match datetime.today().isoweekday():
    case 1 :
        print(" | ".join( [x[0] for x in rows ] ))
        # print(rows)
a = input("If you wanna see an other day ps enter day name: ")
match a:
    case "Monday":
        print(a)