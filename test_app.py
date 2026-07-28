from app import categorize_email, organize_emails

def test_work_email():
    assert categorize_email("Project deadline reminder", "The report is due Friday") == "Work"

def test_finance_email():
    assert categorize_email("Your invoice is ready", "Payment due in 7 days") == "Finance"

def test_personal_email():
    assert categorize_email("Happy Birthday!", "Hope you have a great day with family") == "Personal"

def test_spam_email():
    assert categorize_email("You are a WINNER", "Click here to claim your free money") == "Spam"

def test_general_email():
    assert categorize_email("Random subject", "Nothing relevant here") == "General"

def test_organize_emails():
    emails = [
        {"subject": "Project deadline reminder", "body": "The report is due Friday"},
        {"subject": "Your invoice is ready", "body": "Payment due in 7 days"},
    ]
    result = organize_emails(emails)
    assert "Work" in result
    assert "Finance" in result