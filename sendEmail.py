import smtplib
import yaml

def sendEmail(license_quantity, code) :
    with open("mail.yaml", "r") as yaml_file:
        documents = yaml.safe_load_all(yaml_file)

        for document in documents:
            if "LOGIN_INFO" in document:
                login_info = document["LOGIN_INFO"]
                LOGINMAIL = login_info["EMAIL"]
                LOGINPASS = login_info["PASSWORD"]

            if "RECEIVER_EMAIL" in document:
                receiver_email = document["RECEIVER_EMAIL"]
                RECEIVERMAIL = receiver_email["EMAIL"]

    if code == 404 :
        message = "No se pudo iniciar sesion a PayTrigger, en 1 hora se intentara nuevamente."
        subject = "No se pudo iniciar sesion en PayTrigger."
    elif code == None :
        message = f"Las licencias de PayTrigger estan a punto de agotar. Cantidad restante de licencias: {license_quantity}"
        subject = "Licencias PayTrigger estan a punto de agotar"

    email_body = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()

    server.login(LOGINMAIL, LOGINPASS)
    server.sendmail(LOGINMAIL, RECEIVERMAIL, email_body)

    server.quit()
