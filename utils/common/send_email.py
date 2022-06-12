import smtplib


def mail_send(name, email, phone, message):
    with smtplib.SMTP('mail.bluetreeconcepts.com', 587) as smtp:
        notify_list = ['domerackimark@gmail.com', 'itcfl@yahoo.com', 'mark.domeracki@bluetreeconcepts.com']
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('info@bluetreeconcepts.com', 'Usmc9423#')

        msg = f"""From: info@bluetreeconcepts.com\nSubject: test subject\n\n 
        {name}
        {email}
        {phone}
        {message}
        """

        smtp.sendmail('info@bluetreeconcepts.com', notify_list, msg)
        print('sent')
