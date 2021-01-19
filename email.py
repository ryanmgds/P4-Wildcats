import copy
import random
import smtplib
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText
# from email.MIMEBase import MIMEBase
# from email import encoders

names = ['Charles','Sabrina','Brianna',
         'Tommy', 'Jared', 'Brent',
         'Derek', 'Chase', 'Bryce']
emails = ['charles.abadie@gmail.com','sabrina.criner@gmail.com','brianna.abadie@gmail.com',
          'tommyjcriner@gmail.com','jmodugno26@gmail.com','modugnob88@gmail.com',
          'dmod129@gmail.com', 'chase.modugno@gmail.com','bmodugno1000@gmail.com']

gmail_user = 'jmodugno26@gmail.com'
gmail_password = ''
sent_from = gmail_user
subject = 'SECRET SANTA ABADIE/CRINER/MODUGNO 2020'

def secret_santa(names):
    my_list = names
    choose = copy.copy(my_list)
    result = []
    for i in my_list:
        names = copy.copy(my_list)
        # removes people from the list. If you are spouce OR
        # you had them last year. (need to have it so it is a list and i
        # dont have to edit every year. (work in progress))

        # should also make it so i get sent a list of names and who they got
        if i == 'Brianna':
            names.pop(names.index('Charles'))
        elif i == 'Sabrina':
            names.pop(names.index('Tommy'))
            names.pop(names.index('Chase'))
        elif i == 'Tommy':
            names.pop(names.index('Sabrina'))
            names.pop(names.index('Derek'))
        elif i == 'Charles':
            names.pop(names.index('Brianna'))
            names.pop(names.index('Bryce'))
        elif i == 'Brent':
            names.pop(names.index('Tommy'))
        elif i == 'Derek':
            names.pop(names.index('Jared'))
        elif i == 'Chase':
            names.pop(names.index('Sabrina'))
        elif i == 'Jared':
            names.pop(names.index('Brianna'))
        elif i == 'Bryce':
            names.pop(names.index('Brent'))
        names.pop(names.index(i))
        chosen = random.choice(list(set(choose)&set(names)))
        result.append((i,chosen))
        choose.pop(choose.index(chosen))
    return result

ss_result = secret_santa(names)
final = zip(ss_result,emails)

for x in final:
    fromaddr = "jmodugno26@gmail.com"
    to = x[1]
    # msg = MIMEMultipart()
    # msg['From'] = fromaddr
    # msg['To'] = toaddr
    # msg['Subject'] = "SECRET EMAIL FOR SECRET SANTA!"

    body1 = "Keep it secret, keep it safe.\n" + str(x[0][0]) + ", your secret santa is......\n\n " +str(x[0][1]) + "!!!"
    body2 = "\n\n We will get together on the 24th through duo! \n\n There is a $20 limit this year.\n You shouldn't get the same person as last year or your spouce this year.\n\n Happy Secret Santa-ing!"
    body = body1+body2
    email_text = 'Subject: {}\n\n{}'.format(subject, body)
    # email_text = """\
    # From: %s
    # To: %s
    # Subject: %s
    #
    # %s
    # """ % (sent_from, ", ".join(to), subject, body)

    # filename = "The image file you put in the same directory with this file"
    # attachment = open("The image file you put in the same directory with this file(ex: xxxx.jpg)", "rb")
    #
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    #
    # msg.attach(part)


    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.starttls()
    # server.login(fromaddr, "1Ggojira1$")
    # msg = msg.as_string()
    # server.sendmail(sent_from, to, email_text)
    # server.quit()


    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print ("mail sent to",x[1])