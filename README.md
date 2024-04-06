# Health Monitoring Django App

![Django](https://img.shields.io/badge/Django-3.2-green)
![Python](https://img.shields.io/badge/Python-3.9-blue)
![License](https://img.shields.io/github/license/yourusername/health-monitoring-django-app)

This is a Django application which will give you  health-related data according to your BMI. It will give you steps to be taken for healthy lifestyle according to your BMI category.

## Features

- Health Plan will be sent to your e-mail automatically when you register to our portal.
- After User creation it will give you health plan like diet and exercises which you need to be taken according to BMI which will be calculated accordingly.
- There are different plans for male and female category.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/health-monitoring-django-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd health-monitoring-django-app
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv env
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        env\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source env/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run migrations:

    ```bash
    python manage.py migrate
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage

- Create a new user by filling up the form to check its BMI and steps to be taken.
- Once user is created, user can see its details and health plan on display tab.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on 
<a href="mailto:ashishkalwar03@gmail.com">email</a> or 
<a href="https://www.linkedin.com/in/ashish-kalwar/" target="_blank">LinkedIn</a>
