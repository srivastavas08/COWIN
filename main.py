import os

from cowin_api import CoWinAPI
import pandas as pd
import datetime
import pywhatkit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


district_id = '670'
# date = '10-07-2021'  # Optional. Takes today's date by default
# min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit
today = datetime.date.today() + datetime.timedelta(days=1)
today = today.strftime("%d-%m-%Y")
dict={'name':[], 'address':[], 'block_name':[], 'pincode':[], 'fee_type':[], 'vaccine':[], 'min_age_limit':[], 'allow_all_age':[], 'available_capacity':[], 'dose1':[], 'dose2':[]  }
Message = []
cowin = CoWinAPI()
available_centers = cowin.get_availability_by_district(district_id)
length_value = len(available_centers['centers'])

temp = []
for i in range(length_value):
    text = "Name = " + str(sorted(available_centers.values())[0][i]['name']) + "\n"
    dict['name'].append(sorted(available_centers.values())[0][i]['name'])
    text = text + "Address = " + str(sorted(available_centers.values())[0][i]['address']) + "\n"
    dict['address'].append(sorted(available_centers.values())[0][i]['address'])
    text = text + "Block Name = " + str(sorted(available_centers.values())[0][i]['block_name']) + "\n"
    dict['block_name'].append(sorted(available_centers.values())[0][i]['block_name'])
    text = text + "Pincode = " + str(sorted(available_centers.values())[0][i]['pincode']) + "\n"
    dict['pincode'].append(sorted(available_centers.values())[0][i]['pincode'])
    text = text + "Fee Type = " + str(sorted(available_centers.values())[0][i]['fee_type']) + "\n"
    dict['fee_type'].append(sorted(available_centers.values())[0][i]['fee_type'])
    text = text + "Vaccine = " + str(sorted(available_centers.values())[0][i]['sessions'][0]['vaccine']) + "\n"
    dict['vaccine'].append(sorted(available_centers.values())[0][i]['sessions'][0]['vaccine'])
    text = text + "Minimum Age Limit = " + str(sorted(available_centers.values())[0][i]['sessions'][0]['min_age_limit']) + "\n"
    dict['min_age_limit'].append(sorted(available_centers.values())[0][i]['sessions'][0]['min_age_limit'])
    dict['allow_all_age'].append(sorted(available_centers.values())[0][i]['sessions'][0]['allow_all_age'])
    text = text + "Dose 1 Available Slots = " + str(sorted(available_centers.values())[0][i]['sessions'][0]['available_capacity_dose1']) + "\n"
    dict['dose1'].append(sorted(available_centers.values())[0][i]['sessions'][0]['available_capacity_dose1'])
    text = text + "Dose 2 Available Slots = " + str(sorted(available_centers.values())[0][i]['sessions'][0]['available_capacity_dose2']) + "\n"
    dict['dose2'].append(sorted(available_centers.values())[0][i]['sessions'][0]['available_capacity_dose2'])
    Message.append(text)
file_name = datetime.date.today()
file_name = file_name.strftime("%d-%m-%Y")
centers = pd.DataFrame.from_dict(dict, orient='index')
centers = centers.transpose()
centers.to_html(f'{file_name}.html')
# centers.to_csv(f'{file_name}.csv')
# print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# print("                                     Slots Available Today:")
# print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#
# # with open("test.txt", "w") as file:
# #     file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# #     file.write("                                     Slots Available Today:")
# #     file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# #
# with open(f"{datetime.date.today()}.txt", "a") as file:
#     file.truncate(0)
#
# for i in Message:
#     print(i)
#     print("------------xxxx------------")
#     with open(f"{file_name}.txt", "a") as file:
#         file.write(f"{i} \n \n")
#
#
# print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# print("                                     Slots Available tomorrow")
# print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")

dict={'name':[], 'address':[], 'block_name':[], 'pincode':[], 'fee_type':[], 'vaccine':[], 'min_age_limit':[], 'allow_all_age':[], 'available_capacity':[], 'dose1':[], 'dose2':[]  }
Message1 = []
cowin = CoWinAPI()
available_centers = cowin.get_availability_by_district(district_id, today)
length_value = len(available_centers['centers'])

temp = []
for i in range(length_value):
    text = "Name = " + str(sorted(available_centers.values())[0][i]['name']) + "\n"
    dict['name'].append(sorted(available_centers.values())[0][i]['name'])
    text = text + "Address = " + str(sorted(available_centers.values())[0][i]['address']) + "\n"
    dict['address'].append(sorted(available_centers.values())[0][i]['address'])
    text = text + "Block Name = " + str(sorted(available_centers.values())[0][i]['block_name']) + "\n"
    dict['block_name'].append(sorted(available_centers.values())[0][i]['block_name'])
    text = text + "Pincode = " + str(sorted(available_centers.values())[0][i]['pincode']) + "\n"
    dict['pincode'].append(sorted(available_centers.values())[0][i]['pincode'])
    text = text + "Fee Type = " + str(sorted(available_centers.values())[0][i]['fee_type']) + "\n"
    dict['fee_type'].append(sorted(available_centers.values())[0][i]['fee_type'])
    text = text + "Vaccine = " + str(sorted(available_centers.values())[0][i]['sessions'][0]['vaccine']) + "\n"
    dict['vaccine'].append(sorted(available_centers.values())[0][i]['sessions'][0]['vaccine'])
    text = text + "Minimum Age Limit = " + str(sorted(available_centers.values())[0][i]['sessions'][0]['min_age_limit']) + "\n"
    dict['min_age_limit'].append(sorted(available_centers.values())[0][i]['sessions'][0]['min_age_limit'])
    dict['allow_all_age'].append(sorted(available_centers.values())[0][i]['sessions'][0]['allow_all_age'])
    text = text + "Dose 1 Available Slots = " + str(sorted(available_centers.values())[0][i]['sessions'][0]['available_capacity_dose1']) + "\n"
    dict['dose1'].append(sorted(available_centers.values())[0][i]['sessions'][0]['available_capacity_dose1'])
    text = text + "Dose 2 Available Slots = " + str(sorted(available_centers.values())[0][i]['sessions'][0]['available_capacity_dose2']) + "\n"
    dict['dose2'].append(sorted(available_centers.values())[0][i]['sessions'][0]['available_capacity_dose2'])
    Message1.append(text)

centers = pd.DataFrame.from_dict(dict, orient='index')
centers = centers.transpose()
# centers.to_html(f'{today}.html')
centers.to_csv(f'{today}.csv')
#
# with open(f"{today}.txt", "a") as file:
#     file.truncate(0)
#
# for i in Message1:
#     print(i)
#     print("------------xxxx------------")
#     with open(f"{today}.txt", "a") as file:
#         file.write(f"{i} \n \n")
#
































#
# mail_content = f'''Hello,
# Please find the attached Document.
# This mail is attached with the latest info of the vaccine slots available as on date {file_name}
# Thank You
# Shivam Srivastava
# '''
#
#
# sender_address = 'mongoengine@gmail.com'
# sender_pass =
# receiver_address = 'mongoengine@gmail.com'
# #Setup the MIME
# message = MIMEMultipart()
# message['From'] = sender_address
# message['To'] = receiver_address
# message['Subject'] = f'COWIN SLOTS UPDATE as on {file_name}'
# #The subject line
# #The body and the attachments for the mail
# message.attach(MIMEText(mail_content, 'plain'))
# attach_file_name = f'{file_name}.csv'
# attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
# payload = MIMEBase('application', 'octate-stream')
# payload.set_payload((attach_file).read())
# encoders.encode_base64(payload) #encode the attachment
# #add payload header with filename
# payload.add_header('Content-Decomposition', "attachment; filename= %s" % attach_file_name)
# message.attach(payload)
# #Create SMTP session for sending the mail
# session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
# session.starttls() #enable security
# session.login(sender_address, sender_pass) #login with mail_id and password
# text = message.as_string()
# session.sendmail(sender_address, receiver_address, text)
# session.quit()
# print('Mail Sent')
#
# mail_content = f'''Hello,
# Please find the attached Document.
# This mail is attached with the latest info of the vaccine slots available as on date {today}
# Thank You
# Shivam Srivastava
# '''
#
#
# sender_address = 'mongoengine@gmail.com'
# sender_pass = 'SHIvam7426'
# receiver_address = 'mongoengine@gmail.com'
# #Setup the MIME
# message = MIMEMultipart()
# message['From'] = sender_address
# message['To'] = receiver_address
# message['Subject'] = f'COWIN SLOTS UPDATE as on {today}'
# #The subject line
# #The body and the attachments for the mail
# message.attach(MIMEText(mail_content, 'plain'))
# attach_file_name = f'{today}.txt'
# attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
# payload = MIMEBase('application', 'octate-stream')
# payload.set_payload((attach_file).read())
# encoders.encode_base64(payload) #encode the attachment
# #add payload header with filename
# payload.add_header('Content-Decomposition', 'attachment', filename=f"{attach_file_name}.html")
# message.attach(payload)
# #Create SMTP session for sending the mail
# session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
# session.starttls() #enable security
# session.login(sender_address, sender_pass) #login with mail_id and password
# text = message.as_string()
# session.sendmail(sender_address, receiver_address, text)
# session.quit()
# print('Mail Sent')