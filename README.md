# The App
## Description
This app is an example job application app built with Python. The app uses the Django web framework, the most powerful in Python yet.
It contains 4 fields and 4 options for your occupation:
- Student
- Self-Employed
- Unemployed
- Employed

After this form is submitted, an email will be sent telling that the job application form has been submitted. Then, this data goes to the admin interface where
the admins can edit the date or delete the record.

## What happens if a record is edited or deleted?
Then the application sends an email. In case of a record being edited, meaning the interview date is postponed or preponed, then 
the application sends an email saying that the interview date has changed. If the record is deleted, we send an email that the interview has been cancelled.

## Blogs
I have added another app to this website, if you click on the blogs section of the nav bar, you will see a list of blogs, it will show it's thumbnail picture, and its description in bold. If you click on any of these blogs, it will redirect you to the actual blogs where the title, its content and the pictures will be shown in this order (I did not know any better way of doing this).

## Dependencies:
- Django==4.2.6
- asgiref==3.7.2
- Pillow==10.1.0
- sqlparse==0.4.4
- tzdata==2023.3

Assuming that you have cloned the git repo and are in that repo folder, you can install these by the command:
```
pip install -r requirements.txt
```

## Environment Variables:
I have used environment variables for the username and password of the email sender.
Variable | Value 
--- | --- 
USERNAME_1 | Your email which will be used for sending the email
PASSWORD | The app password for that email. Go to (Your Account > Security > 2-Step Verification > App Password) for google.