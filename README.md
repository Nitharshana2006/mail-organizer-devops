Mail Organizer DevOps Pipeline Project



Build Status: Passing (see GitHub Actions tab for live status)



A simple mail categorization app used as a demo project to showcase a full DevOps CI/CD pipeline using Git, GitHub, GitHub Actions, and automated artifact packaging.



What it does:

Sorts sample emails into categories such as Work, Finance, Personal, Spam, and General using keyword matching.



DevOps Tools Used:

Git and GitHub for version control and remote repository

GitHub Actions for CI/CD pipeline automation

Automated testing with pytest

Automated build packaging and artifact upload



Pipeline Stages:

1\. Checkout code from GitHub

2\. Set up Python environment

3\. Install dependencies

4\. Run automated tests with pytest

5\. Run the application

6\. Package the application into a release folder

7\. Upload the packaged build as a downloadable artifact



How the pipeline works:

Every time code is pushed to the main branch, GitHub Actions automatically triggers the pipeline defined in .github/workflows/ci.yml. If all tests pass, the application is packaged and made available as a downloadable build artifact. This demonstrates a complete Continuous Integration and Continuous Deployment workflow without requiring any local installation.

