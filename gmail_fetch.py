# gmail_fetch.py - Fetch real emails from Gmail and organize them

import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from app import categorize_email

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def get_gmail_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)

def fetch_recent_emails(service, max_results=10):
    results = service.users().messages().list(userId="me", maxResults=max_results).execute()
    messages = results.get("messages", [])

    emails = []
    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"], format="metadata",
                                                    metadataHeaders=["Subject"]).execute()
        headers = msg_data.get("payload", {}).get("headers", [])
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "(No Subject)")
        snippet = msg_data.get("snippet", "")
        emails.append({"subject": subject, "body": snippet})

    return emails

if __name__ == "__main__":
    service = get_gmail_service()
    emails = fetch_recent_emails(service, max_results=10)

    print(f"Fetched {len(emails)} recent emails.\n")

    organized = {}
    for email in emails:
        category = categorize_email(email["subject"], email["body"])
        organized.setdefault(category, []).append(email["subject"])

    for category, subjects in organized.items():
        print(f"\n[{category}]")
        for s in subjects:
            print(f"  - {s}")
