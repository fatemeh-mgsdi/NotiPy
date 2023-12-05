# NotiPy

NotiPy is a Django-based REST API that allows you to define email templates containing topic, name and message template. You can use the templates to send emails to people.
For sending an email, the whole email properties would be saved into database, and the email will be sent by django signal.

## Getting Started

### Prerequisites

Before running the project, you'll need to have the following installed on your machine:

- Python 3
- PostgreSQL
- Docker (if running with Docker)

### Environment Variables

This project uses environment variables to store sensitive information such as database credentials. To run the project, you'll need to create a `.env` file in the root directory of your project and add the required variables.

1. Create a `.env` file in the root directory of your project:

```bash
touch .env
```

2. Open the `.env.sample` file and copy its contents, paste the contents of the `.env.sample` file into the `.env` file.

3. Replace the default values of the variables with your own values.

```
POSTGRES_USER=your_postgres_username
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_database_name
POSTGRES_HOST=your_database_host
POSTGRES_PORT=your_database_port

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD= 
```

Save the `.env` file.

### Running Locally

To run the project locally, follow these steps:

1. Ensure that PostgreSQL is installed and running locally.
2. Clone the repository to your local machine:

```bash
git clone https://github.com/fatemeh-mgsdi/NotiPy.git
cd NotiPy/
```

3. Install the project's dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Create a superuser account:

````bash
python manage.py createsuperuser
````

5. Run the development server:

````bash
python manage.py runserver
````

Once the server is running, you can access the API at http://localhost:8000/.

### Running with Docker

To run the project using Docker, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/fatemeh-mgsdi/NotiPy.git
cd NotiPy/
```

2. Build and start the Docker containers:

````bash
docker-compose build
docker-compose --env-file=.env up
````

Once the containers are running, you can access the API at http://localhost:8000/.

### How to use it?

Head in to http://localhost:8000/admin/notifications/emailtemplate/, and create a new email template.
And all you need to do is to make an HTTP request:

``` bash
curl --location --request POST 'http://localhost:8000/notifications/send' \

--header 'Content-Type: application/json' \

--data-raw '{

"receiver": "some_email@gmail.com",

"template": 2,

"message":"234234"

}'
```

and then, the email would be sent.
### Defining templates

For creating a new template, you must set a name for the temlate, topic and the template of the message.
You can see examples of the templates below:

**1- Verification email with token:**
``` 
We’re excited to welcome you to our website! Before you begin your journey, we need to verify your account. This is your verification code:

{token}
  
After verification, you’ll have access to all the amazing features on our website.  
  
If you encounter any issues or have questions, our support team is here to help. Simply reply to this email.
  
Welcome aboard!
```

**2- Verification email without token:**
```
Thank you for reaching out to learn more about our company! The best way to learn more about our services as they pertain to your business is to set up a free consult call with each other. 

There will be no obligation to sign up after the call.

If you’d like to set up one of these consults, Simply reply to this email.

We look forward to hearing from you!
```















