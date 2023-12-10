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

## Dockerizing this Project
In this repository, you can find 3 files related to dockerizing this project; "Dockerfile", ".dockerignore" and "docker-compose.yaml". Docker is a DevOp tool where a certain task with a program is done in many isolated 'containers'. Docker helps to check if a program is functioning outside of your system etc. So, to run this, you can either:
* Use the image: 'yasiratiq/job-application-app:latest' or simply 'yasiratiq/job-application-app' to run this with docker:
  ```bash
   docker run -e USERNAME_1=your_gmail_account -e PASSWORD=app_password_to_USERNAME_1 -p 8000:8000 yasiratiq/job-application-app
  ```
* Make a separate image with the Dockerfile provided with:
    ```bash
    docker build --tag=name_of_your_image:latest .
    ```
* Make an image or use my image then supply that in the 'docker-compose.yaml' file then run:
    ```bash
    docker-compose up -d --build
    ```
## Blogs
I have added another app to this website, if you click on the blogs section of the nav bar, you will see a list of blogs, it will show it's thumbnail picture, and its description in bold. If you click on any of these blogs, it will redirect you to the actual blogs where the title, its content and the pictures will be shown in this order (I did not know any better way of doing this). I ran into an error where if I ran this website on a docker container, it won't have any static files. For this I had to make a static folder which would hold all the static files in /static/ url. I had to run this with DEBUG being True. If anyone knows a better solution please tell me.

## Dependencies:
- Django==4.2.6
- asgiref==3.7.2
- Pillow==10.1.0
- sqlparse==0.4.4
- tzdata==2023.3

Assuming that you have cloned the git repo and are in that repo folder, you can install these by the command:
```bash
pip install -r requirements.txt
```

## Environment Variables:
I have used environment variables for the username and password of the email sender. Here are the environment variables:

| Variable   | Value                                                                                                             |
|------------|-------------------------------------------------------------------------------------------------------------------|
| USERNAME_1 | Your email which will be used for sending the email                                                               |
| PASSWORD   | The app password for that email. Go to (Your Account > Security > 2-Step Verification > App Password) for google. |