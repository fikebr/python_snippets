from google.oauth2 import service_account
from googleapiclient.discovery import build
import config

# https://developers.google.com/sheets/api/guides/values#python
# range_name can be a whole sheet name, a A1:C3 range or sheet1!B1:E1

def gsheet_get_data(range_name):
    try:
        creds = service_account.Credentials.from_service_account_file(
            config.KEY_FILE, scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=config.SPREADSHEET_ID, range=range_name)
            .execute()
        )
        return result.get("values", [])
    except Exception as e:
        logging.error(f"gsheet_get_data : {range_name} : {e}")
        return None

def gsheets_set_data(spreadsheet_id, range_name, value_input_option, values):
    try:
        credentials = service_account.Credentials.from_service_account_file(
            config.KEY_FILE, scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        service = build("sheets", "v4", credentials=credentials)

        body = {"values": values}

        result = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body,
            )
            .execute()
        )
        print(f"{result.get('updatedCells')} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def gsheets_append_data(spreadsheet_id, range_name, value_input_option, values):

    try:
        creds = service_account.Credentials.from_service_account_file(
            config.KEY_FILE, scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )

        service = build("sheets", "v4", credentials=creds)

        body = {"values": values}
        result = (
            service.spreadsheets()
            .values()
            .append(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body,
            )
            .execute()
        )
        print(f"{(result.get('updates').get('updatedCells'))} cells appended.")
        return result

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error



if __name__ == "__main__":
    gsheets_set_data(
        "1CM29gwKIzeXsAppeNwrc8lbYaVMmUclprLuLYuHog4k",
        "A1:C2",
        "USER_ENTERED",
        [["A", "B"], ["C", "D"]],
    )

    gsheets_append_data(
        "1CM29gwKIzeXsAppeNwrc8lbYaVMmUclprLuLYuHog4k",
        "A1:C2",
        "USER_ENTERED",
        [["F", "B"], ["C", "D"]],
    )
