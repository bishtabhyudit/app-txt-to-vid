import os
import requests
import json
import os
import sys
import subprocess


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import imaplib
import email
from email.header import decode_header
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium.webdriver.chrome.service import Service


os.makedirs('/tmp/downloaded')
temp_dir = '/tmp/downloaded'
# Define the URL to download ChromeDriver
chrome_driver_url = "https://storage.googleapis.com/chrome-for-testing-public/121.0.6167.184/linux64/chrome-linux64.zip"

# Define the file name for ChromeDriver
chrome_driver_file = os.path.join(temp_dir, "chromedriver_linux64.zip")

# Download ChromeDriver
response = requests.get(chrome_driver_url)
with open(chrome_driver_file, "wb") as file:
    file.write(response.content)

# Extract ChromeDriver from the ZIP file
import zipfile
with zipfile.ZipFile(chrome_driver_file, 'r') as zip_ref:
    zip_ref.extractall()

# Remove the ZIP file
os.remove(chrome_driver_file)

# Path to the ChromeDriver executable file
chrome_driver_path = os.path.abspath("chromedriver.exe")

prompt = event['queryStringParameter']['prompt']
# prompt = """
# a tiktok style video for a new gym clothing line for men and women. 
# This product line uses latest technology fabrics which is best in class for fitness and workouts."""

receiver_email = event['queryStringParameter']['receiver_email']
# receiver_email = 'abhyudit12bisht@gmail.com'

url = "https://ai.invideo.io/login"

options = Options()
# options.add_argument("--headless")  # Add this line if you want to run in headless mode
# options.add_argument("--window-size=1200,768")

driver = webdriver.Chrome(options = options)

chrome_version = driver.capabilities['chrome']['chromedriverVersion']

# Print the ChromeDriver version
print("ChromeDriver Version:", chrome_version)


time.sleep(2)
driver.get(url)


time.sleep(2)
xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[4]/form/div/input"
elem = driver.find_element(By.XPATH, xpath)
elem.send_keys("hackathonbots@gmail.com")


time.sleep(2)
xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[4]/form/button"
elem = driver.find_element(By.XPATH, xpath)
elem.click()


time.sleep(20)

# Function to decode email subject
def decode_subject(subject):
    decoded = decode_header(subject)[0]
    if decoded[1] is not None:
        return decoded[0].decode(decoded[1])
    else:
        return decoded[0]

# Gmail IMAP server and credentials
IMAP_SERVER = 'imap.gmail.com'
EMAIL = 'hackathonbots@gmail.com'
PASSWORD = 'euxa cxhe icqa jnam'

# Connect to Gmail IMAP server
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')

# Search for latest email
result, data = mail.search(None, 'ALL')
latest_email_id = data[0].split()[-1]

# Fetch the latest email
result, data = mail.fetch(latest_email_id, '(RFC822)')
raw_email = data[0][1]

# Parse the raw email
msg = email.message_from_bytes(raw_email)

# Extract email details
email_subject = decode_subject(msg['subject'])
email_from = msg['from']

# Initialize email body variable
email_body = ""

def is_from_invideo_ai(msg):
    sender_name = decode_header(msg['From'])[0][0]
    if sender_name == "invideo AI":
        return True
    return False


# Extract email body only if it's from "invideo AI"
if is_from_invideo_ai(msg):
    # Extract email body
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            # Ignore any attachments
            if "attachment" not in content_disposition:
                body = str(part.get_payload(decode=True))
                email_body += body
    else:
        email_body = msg.get_payload(decode=True).decode()

# Close the connection
mail.logout()



time.sleep(2)

# Define the regular expression pattern to match numbers
pattern = r'\d+'
# Use re.findall() to find all matches of the pattern in the string
numbers = re.findall(pattern, email_subject)[0]

time.sleep(2)
xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[4]/div[1]/form/input"
elem = driver.find_element(By.XPATH, xpath)
elem.send_keys(numbers)


time.sleep(2)
xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[4]/div[1]/form/button"
elem = driver.find_element(By.XPATH, xpath)
elem.click()


time.sleep(2)
xpath = "/html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[1]/div[1]/div/form/div[1]/textarea"
elem = driver.find_element(By.XPATH, xpath)
elem.send_keys(prompt)


time.sleep(2)
xpath = "/html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[1]/div[1]/div/form/div[2]/button/div"
elem = driver.find_element(By.XPATH, xpath)
elem.click()


time.sleep(120)
xpath = "/html/body/div/div[1]/div/div[3]/div/div[3]/div/div/div/div/div[2]/div/div[5]/button[2]/p"
elem = driver.find_element(By.XPATH, xpath)
elem.click()
time.sleep(120)



button_list = ['/html/body/div/div[1]/div/div[3]/div/div[3]/div/div/div/div[5]/div/div[1]/div/div[2]/button[2]/p',
'/html/body/div/div[1]/div/div[3]/div/div[3]/div/div/div/div[5]/div/div[1]/div/div[2]/div[2]/div/div/div',
'/html/body/div[3]/div/div[3]/div/div[1]/div[1]/button[1]/p',
'/html/body/div[3]/div/div[3]/div/div[2]/div[1]/button[1]/p',
'/html/body/div[3]/div/div[5]/div[2]/button/p']

for elem in button_list:
    elem = driver.find_element(By.XPATH, elem)
    elem.click()
    time.sleep(2)


time.sleep(30)
xpath ='/html/body/div/div[1]/div/div[3]/div/div/div[1]/div[2]/div[2]/button[1]/p'
elem = driver.find_element(By.XPATH, xpath)
elem.click()


xpath = "/html/body/div[2]/div/div[2]/div[3]/div/p"
elem = driver.find_element(By.XPATH, xpath)
element_text = elem.text

video_link = element_text


# Email configuration
sender_email = "hackathonbots@gmail.com"
receiver_email = receiver_email
password = 'euxa cxhe icqa jnam'

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Your text to video link is ready!"

# Create the body of the message (a plain-text and an HTML version).
text = "Checkout your AI generated video here: {}".format(video_link)
html = """\
<html>
  <body>
    <p>
    {text}
    </p>
  </body>
</html>
""".format(text=text)

# Attach both plain text and HTML versions
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

# Create SMTP session
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()  # Secure the connection
    # Login to the SMTP server
    server.login(sender_email, password)
    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")


return {
    'statusCode': 200,
    'body': json.dumps('Request will be completed shortly.')
}
