# Team 74 Terms & Conditions Generator Project Skeleton

# How to use

<hr>

  1.  Create a virtual environment on your system using the command `python3 -m virtualenv “environment name”` or `python3 -m venv “environment name” `
  2.  Activate it using the command `source <path to environment variables>/bin/activate` on linux machines or `source <path to environment variables>/Scripts/activate` on windows
  3.  Run the command, `pip install -r requirements.txt` to install all dependencies in the virtual environment
  4.  Update your requirements.txt file using the command `pip freeze > requirements.txt`
  5.  Fork or clone this repository
  6.  Generate your django secret key by doing the following:
  7.  Run the command `python3 manage.py shell`
  8.  Inside the shell that opens in the terminal type the following:
      - `from django.core.management.utils import get_random_secret_key`
      - `print(get_random_secret_key())`
      - Copy the generated key
      - You can also follow this simple tutorial

  9.  Define your django secret key using the environment variable `DJANGO_SECRET_KEY` in a `.env` file at the root of the project.
  10. Run the command `python3 manage.py migrate` to start up your database
  11. Run the command `python3 manage.py runserver` to startup your server



# Requirements

  - Python
  - virtualenv or venv
  - pip
  - python-dotenv

  Check the requirements.txt file for a more comprehensive list.

# Frontend Guys
  - Create your own css and js files in the static folder
  - We shall come up with a naming convention for our styles so that we don't overwrite each others styles.

<br>
<hr>

[**de-marauder**](https://github.com/de-marauder) and [**labodinho**](https://github.com/labodinho) will be handling the main branch and merging of feature branches so you can perform your task in your own dedicated branches

### Good luck everyone!

<br>
<hr>

## Relevant links
  - UX Research documention: https://docs.google.com/document/d/1T4SFiEQCYYrOaHTu2laP7x9L5mTi5jr42VCgjAVX7rI/edit?usp=sharing
  - Technical documentation: https://docs.google.com/document/d/1nvtH6D1MPTVXxoJBVj0Ln0Znj64kLaKMG5RNimM2Aq4/edit?usp=sharing
  - Contributors details and their tasks: https://docs.google.com/spreadsheets/d/11xXrf_8M0h4MvW9oLjhe1myAj8swJUplk9y0fm1J2YQ/edit?usp=sharing
  - Database Schema: https://drive.google.com/file/d/1-TfYdHR8ApGuiqzOfBnUK4ddSRsvrybG/view?usp=sharing
