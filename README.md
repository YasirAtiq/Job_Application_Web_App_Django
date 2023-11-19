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

## Dependencies:
- Django==4.2.6
- asgiref==3.7.2
- sqlparse==0.4.4
- tzdata==2023.3
