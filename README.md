Mail Organizer DevOps Pipeline Project

Build Status: Passing (see GitHub Actions tab for live status)

A mail categorization app used as a demo project to showcase a full DevOps CI/CD pipeline using Git, GitHub, GitHub Actions, and automated artifact packaging. Includes real Gmail API integration to categorize live inbox emails.

What it does:
Sorts emails into categories such as Work, Finance, Personal, Academic, Security, Motivation, and Spam using keyword matching. Can run on either sample data or a real Gmail inbox.

Files:
app.py - Core categorization logic, runs on sample data
gmail_fetch.py - Connects to real Gmail account using OAuth and categorizes live inbox emails
test_app.py - Automated pytest test suite
requirements.txt - Python dependencies
Dockerfile - Container definition for the app
credentials.json and token.json - Personal Gmail OAuth files, excluded from version control via gitignore for security

DevOps Tools Used:
Git and GitHub for version control and remote repository
GitHub Actions for CI/CD pipeline automation
Automated testing with pytest
Automated build packaging and artifact upload

Pipeline Stages:
1. Checkout code from GitHub
2. Set up Python environment
3. Install dependencies
4. Run automated tests with pytest
5. Run the application on sample data
6. Package the application into a release folder
7. Upload the packaged build as a downloadable artifact

How the pipeline works:
Every time code is pushed to the main branch, GitHub Actions automatically triggers the pipeline defined in .github/workflows/ci.yml. If all tests pass, the application is packaged and made available as a downloadable build artifact.

Note on Gmail integration and CI:
The CI pipeline runs and tests the core categorization logic using sample data only. It does not run gmail_fetch.py, because automated CI environments cannot perform interactive Google OAuth logins. This is standard practice in real-world DevOps pipelines, where live third-party integrations are typically tested locally or with mocked responses, while CI focuses on validating application logic.
