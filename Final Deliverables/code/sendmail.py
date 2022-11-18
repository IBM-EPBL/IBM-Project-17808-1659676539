from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

def send_mail(mail_id,income):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'

    income = str(income)
    
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = "the budget reached"
    html_content = "<html><body><h3>This Mail is to inform you that your expenses have reached the budget of "+income+" !!!</h3></body></html>"
    sender = {"name":"Admin-Expense tracker","email":"ganeshganzz01@gmail.com"}
    to = [{"email":mail_id,"name":"member"}]
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to,html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)


