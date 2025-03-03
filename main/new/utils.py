from django.core.mail import EmailMessage
import os 

class Utils:
    @staticmethod
    def send_email(data):
        try:
            email = EmailMessage(
                subject=data.get('subject', 'No Subject'), 
                body=data.get('body', ''),  
                from_email=os.environ.get('EMAIL_FROM'),
                to=[data.get('to_email')],
            )
            email.send(fail_silently=True)
            print("Email sent successfully")
        except Exception as e:
            print(f"Error sending email: {e}")
