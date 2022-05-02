from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

def main():

    github_repo = "tbd"

    ##  GET INFO FROM .env FILE  ##
    load_dotenv()
    email = os.environ.get("EMAIL")
    password = os.environ.get("PASS")
    receiver = os.environ.get("TO")

    database = open('./resources/database', 'r')
    jokes = open('./resources/jokes', 'r')
    lines = jokes.readlines()
    count = int (database.readline())
    msg = MIMEMultipart()

    joke_message = "\nYour Personal Knock-Knock Joke for " + datetime.today().strftime('%A') + " is:\n\n"

    ## GET JOKE ##
    for i in range(count, count+5):
        joke_message = joke_message + lines[i]

    joke_message = joke_message + "\n\nTo cancel your subscription to the knock-knock joke bot, please contact its creator.\n" \
                                  "To view the source code for the bot, visit this github repo:\n"  + github_repo + "\n"

    msg['From'] = email
    msg['To'] = receiver
    msg['Subject'] = "Knock Knock Joke for: " + datetime.today().strftime("%m/%d/%Y")
    msg.attach(MIMEText(joke_message))


    ##   LOGIN TO MAIL SERVER   ##
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email, password)
        smtp.sendmail(email,receiver,msg.as_string())
        smtp.quit()


    ## UPDATE DATABASE ##
    with open("./resources/database") as f:
        lines = f.readlines()

    count += 6
    lines[0] = str(count)
    with open("./resources/database", "w") as f:
        f.writelines(lines)



    print("Sent:\n" + joke_message)




if __name__ == "__main__":
    main()