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
                                 range="SE21-03!A1:B10").execute()
values = result.get('values',[])
aoa = [["1/1/2022",4000],["4/4/2022",3000],["7/12/2022",7000]]
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheets2!B2",
                                valueInputOption="USER_ENTERED" , body={"values":aoa})
result = service.spreadsheets().values().get(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range="SE21-03!A1:A3").execute()
rows = result.get('values', [])
result2 = service.spreadsheets().values().get(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range="SE21-03!B1:B3").execute()
rows2 = result2.get('values', [])
w_result = service.spreadsheets().values().get(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range="SE21-03!C1:C3").execute()
w_rows = w_result.get('values', [])
t_result = service.spreadsheets().values().get(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range="SE21-03!D1:D3").execute()
t_rows = t_result.get('values', [])
f_result = service.spreadsheets().values().get(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range="SE21-03!E1:E3").execute()
f_rows = f_result.get('values', [])

group = input("Enter your group:  ")
match group:
 case "21SE04":
    print("                     TODAYS TIMETBLE")
    match datetime.today().isoweekday():
        case 1:
            print(" | ".join([x[0] for x in rows]))
        case 2:
            print(" | ".join([x[0] for x in rows2]))
        case 3:
            print(" | ".join([x[0] for x in w_rows]))
        case 4:
            print(" | ".join([x[0] for x in t_rows]))
        case 5:
            print(" | ".join([x[0] for x in f_rows]))
        case 6 :
            print("Today is day off!!!")
        case 7 :
            print("Today is day off!!!")

    a = input("If you wanna see an other day ps enter day name: ")
    match a.upper():
        case "MONDAY":
          print(" | ".join([x[0] for x in rows]))

        case "TUESDAY":
          print(" | ".join([x[0] for x in rows2]))
        case "WEDNESDAY":
          print(" | ".join([x[0] for x in w_rows]))
        case "THURSDAY":
          print(" | ".join([x[0] for x in t_rows]))
        case "FRIDAY":
          print(" | ".join([x[0] for x in f_rows]))

 case "21SE03":
     match datetime.today().isoweekday():
         case 1 :
          print(" | ".join([x[0] for x in rows]))
