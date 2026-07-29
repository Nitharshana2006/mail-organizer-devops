# app.py - Simple Mail Organizer (Demo App for DevOps Pipeline)

CATEGORIES = {
    "Work": ["meeting", "project", "deadline", "report", "client", "invitation", "connect"],
    "Finance": ["invoice", "payment", "bank", "salary", "bill"],
    "Personal": ["family", "friend", "birthday", "vacation"],
    "Academic": ["exam", "result", "weekend exam", "marks", "grade", "hall ticket"],
    "Security": ["security alert", "sign-in", "login", "password", "verify"],
    "Motivation": ["goals", "reset", "reminder", "tip"],
    "Spam": ["lottery", "winner", "free money", "click here"],
}

def categorize_email(subject: str, body: str) -> str:
    text = (subject + " " + body).lower()
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in text:
                return category
    return "General"

def organize_emails(emails: list) -> dict:
    organized = {}
    for email in emails:
        category = categorize_email(email["subject"], email["body"])
        organized.setdefault(category, []).append(email["subject"])
    return organized

if __name__ == "__main__":
    sample_emails = [
        {"subject": "Project deadline reminder", "body": "The report is due Friday"},
        {"subject": "Your invoice is ready", "body": "Payment due in 7 days"},
        {"subject": "Happy Birthday!", "body": "Hope you have a great day with family"},
        {"subject": "You are a WINNER", "body": "Click here to claim your free money"},
    ]

    result = organize_emails(sample_emails)
    for category, subjects in result.items():
        print(f"\n[{category}]")
        for s in subjects:
            print(f"  - {s}")