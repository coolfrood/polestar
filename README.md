## What is this?

This is an inventory tracker for Polestar. This is based off
of [PolAPI](https://github.com/motoridersd/PolAPI). It downloads
inventory information from Polestar's API and updates the information
in a Google spreadsheet

## Configuration

1. Create a new spreadsheet in Google docs, get its ID from the URL
2. Follow Google Cloud documentation [here](https://developers.google.com/workspace/guides/create-project).
   Create and download new credentials into `creds.json`
3. Create a `config.json` file with following contents:

```
{
    "spreadsheet_id": "<ID from step 1>"
}
```

4. Install Google client library with instructions [here](https://developers.google.com/sheets/api/quickstart/python).
5. Run `./update_sheet.py`
