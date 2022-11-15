import smtplib
import requests
import time

# Set up the send account and general email details
gmail_user = "XXXXXXXXX@gmail.com"
gmail_password = "XXXXXXXXXX"
sent_from = gmail_user
to = ["XXXXXXXXXXX@gmail.com", "XXXXXXXXX@gmail.com"]
subject = "outdoor-classroom Change Detected"
urls = [
    "https://rockevents.ca/event/outdoor-classroom/",
    "https://www.google.com"
]
# Start a loop where every min we check the site again
while True:
    time.sleep(60)
    urls_with_issue = []
    for url in urls:
        resp = requests.get(url)
        print(url, resp.status_code)
        if resp.status_code != 200:
            urls_with_issue.append(url)
    if urls_with_issue:
        body = "Issue with the sites:" + ", ".join(urls)
        email_text = """\
        From: %s
        To: %s
        Subject: %s
        %s
        """ % (
            sent_from,
            ", ".join(to),
            subject,
            body,
        )
        try:
            # SEND THE EMAIL!!!!
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
        except Exception as e:
            print("Something went wrong...", e)