from random import random, randint, choice
import string

print(random())
print(randint(0, 1000))

def random_user_id():
    randomstr = ""
    for i in range(1, 4):
        digits = randint(0, 7)
        alphanumeric = choice(string.ascii_letters)
        randomstr += str(digits) + alphanumeric

    return randomstr

user_id = random_user_id()

# kimkimtai
# mlsn.287177aabbd1d8572a19ab7bc3ecdc56103323e6ef4ffb2eda4960fa3106e384

# pro
# mlsn.fa94f685e0a299e2fb1b74086e347b91ea9e33b1424b126a157c25def56129d2

print(user_id)



# chatgpt version

# from mailersend import emails

# # API Key from Mailersend
# api_key = "mlsn.fa94f685e0a299e2fb1b74086e347b91ea9e33b1424b126a157c25def56129d2"

# # Create a NewEmail instance
# mailer = emails.NewEmail(api_key)

# # Define an empty dict to populate with mail values
# mail_body = {}

# # Define the sender
# mail_from = {
#     "name": "Derrick Moio",
#     "email": "no-reply@trial-0r83ql31vnxgzw1j.mlsender.net",  # The verified sender email
# }

# # Define the recipient
# recipients = [
#     {
#         "name": "Derrick Moio",
#         "email": "kimtaimoiben@gmail.com",  # Recipient email
#     }
# ]

# # Optional: Define a reply-to email
# reply_to = [
#     {
#         "name": "Support",
#         "email": "support@kimtaimoiben.com",  # Replace with a valid email if needed
#     }
# ]

# # Build the email
# mailer.set_mail_from(mail_from, mail_body)
# mailer.set_mail_to(recipients, mail_body)
# mailer.set_subject("Hello from Mailersend!", mail_body)
# mailer.set_html_content("<p>This is a test email sent using Mailersend API. {}</p>", mail_body)
# mailer.set_plaintext_content("This is a test email sent using Mailersend API.", mail_body)

# # Optional: Set a reply-to address
# mailer.set_reply_to(reply_to, mail_body)

# # Send the email
# response = mailer.send(mail_body)

# # Print the response for debugging
# print(response)
