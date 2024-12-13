import smtplib

my_email = "place_holder"
my_password = "place_holder"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(
    from_addr=my_email, 
    to_addrs="place_holder",
    msg="Subject:Hello\n\nThis is the content"
)