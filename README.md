<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div>
<div align="center" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:center; vertical-align: middle; padding:40px 0;">
  <a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74">
    <img src="tc_site/static/assets/landing/navbar/logo.png" alt="Logo" width="auto" height="80">
  </a>

  <h3 align="center">QuickTerms</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://obiajuluezike.slite.com/p/LeWE1nW8ZC8iPM/QuickTerms-Technical-Documentation"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://quickTerms.herokuapp.com">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/issues">Request Feature</a>
  </p>
</div>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About QuickTerms</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](/tc_site/static/assets/landing/hero/hero.png)

This software is a web application that basically allows the generation of personalized terms and conditions and privacy policy documents. It is completely free and always will be. It will however, require the user to signup on our platform

Why is it relevant:
* Terms and Conditions and Privacy Policies are important legal documents required by businesses
* These documents are typically very long and are time consuming or expensive to write 
* QuickTerms offers a free solution to the above problems :smile:

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This project is built with the following technologies, frameworks and languages

* [![Django][Django]][Django-url]
* [![Javascript][Javascript]][Javascript-url]
* [![Python][Python]][Python-url]
* [![CSS3][CSS3]][CSS3-url]
* [![HTML5][HTML5]][HTML5-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The steps below consist of instructions to get this project up and running on your local system

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip
  ```sh
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  ```
  ```sh
  python get-pip.py
  ```
* virtualenv
  ```sh
  pip install virtualenv
  ```


### Installation

Now you would want to install all the projects dependencies

1. Create and activate a virtual environment
    ```sh
    python3 -m virtualenv “your environment name”
    ```
    ```sh
    source <path to virtual environment folder just created>/bin/activate
    ```
    <p align="center">OR</p>

    ```sh
    <path to virtual environment folder just created>\Scripts\activate
    ```
2. Clone the repo
     ```sh
     git clone https://github.com/zuri-training/Proj-T_C_Gen-Team-74.git
     ```
3. Install dependencies
     ```sh
     pip install -r requirements.txt
     ```
4. Generate Django secret key
    - Start up a python shell from the terminal using the code
       ```sh
       python3 manage.py shell
       ```
    - Inside the shell that opens in the terminal type the following:
       ```py
       from django.core.management.utils import get_random_secret_key
       print(get_random_secret_key())
       ```
    - Copy the generated output
5.  Define your django secret key using the environment variable DJANGO_SECRET_KEY in a  .env file at the root of the project.
    ```
    DJANGO_SECRET_KEY='generated secret'
    ```
6.  Run the command `python3 manage.py migrate` to start up your database
7.  Run the command `python3 manage.py runserver` to startup your server

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Feature exmaples -->
## Features

Our project provides these basic functionalities:
1.  Ability to preview one of our templates as an unauthenticated user
2.  Ability to generate either Terms and Conditions or Privacy Policy (For authenticated users)
3.  Ability to export generated document as PDF or .docx  (For authenticated users)
4.  Ability to embed generated document into a user's website  (For authenticated users)
5.  Ability to share generated documents via custom generated link  (For authenticated users)
6.  Ability to view all generated documents  (For authenticated users)

## Todo
- Send emails to users on request after document generation
- Accepting user feedback after succesful document generation.

_For more examples, please refer to the [Documentation](https://obiajuluezike.slite.com/p/LeWE1nW8ZC8iPM/QuickTerms-Technical-Documentation)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Setup project Skeleton (Ensuring modular file structure)
- [x] Assign tasks to developers and designers
- [x] Design the site
- [x] Implement designs
- [x] Implement fundamental backend functionalities
    - [x] Authentication
    - [x] File Generation
    - [x] Embed
    - [x] Export
    - [x] Share
- [x] Deploy on heroku
- [ ] Save and Continue later
- [ ] E-mail users after file generation


See the [open issues](https://github.com/zuri-training/Proj-T_C_Gen-Team-74/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact
For more information about this project you can contact [@De_marauder](https://twitter.com/@De_marauder) on twitter or [github](https://github.com/de-marauder) or [linkedin](https://linkedin.com/in/obiajulu-ezike)

Project Link: [https://github.com/zuri-training/Proj-T_C_Gen-Team-74](https://github.com/zuri-training/Proj-T_C_Gen-Team-74)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [I4GxZuri](https://training.zuri.team/)
* [Img Shields](https://shields.io)
* [Heroku](https://heroku.com)
* [Font Awesome](https://fontawesome.com)
* [Bootstrap5](https://getbootstrap.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## All Contributors Table

<div align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2gHxbT2i7oibeTlMbT53Fh9Ae0QCQoLRlexkvjNAaMEfNeK8bAIXD-0-CZD_-_nB0NZc&usqp=CAU" alt="All Contributors Table Screenshot" width="800px" />
</div>

## Contributors ✨

Thanks go to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

[**de-marauder**](https://github.com/de-marauder) and [**labodinho**](https://github.com/labodinho) will be handling the main branch and merging of feature branches so you can perform your task in your own dedicated branches

### Thank you everyone!

<hr>

<table>
  <tr>
    <td align="center"><a href="https://github.com/de-marauder"><img src="https://avatars.githubusercontent.com/de-marauder?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Ezike Obiajulu</b></sub></a><br /><a href="#question-de_marauder" title="Answering Questions">💬</a> <a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=de-marauder" title="Documentation">📖</a><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=de-marauder" title="Code">💻</a><br/> <a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/pulls?q=is%3Apr+reviewed-by%3Ade-marauder" title="Reviewed Pull Requests">👀</a> <a href="#talk-de_marauder" title="Talks">📢</a><a href="#maintenance-de_marauder" title="Maintenance">🚧</a></td>
    <td align="center"><a href="https://github.com/labodinho"><img src="https://avatars.githubusercontent.com/labodinho?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Olabode Oritogun</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=labodinho" title="Code">📖</a> <a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/pulls?q=is%3Apr+reviewed-by%3Alabodinho" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://github.com/ogunkapc"><img src="https://avatars2.githubusercontent.com/ogunkapc?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ogunka Promise</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=ogunkapc" title="Code">📖</a></td>
    <td align="center"><a href="https://github.com/Obianuju007"><img src="https://avatars2.githubusercontent.com/Obianuju007?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Obianuju Esther Onwuasoanya </b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Obianuju007" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/archolisa"><img src="https://avatars0.githubusercontent.com/archolisa?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nwankwo Akaolisa John</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=archolisa" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/taiwoak"><img src="https://avatars0.githubusercontent.com/taiwoak?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Taiwo Akerele</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=taiwoak" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Dev-KceeDan"><img src="https://avatars0.githubusercontent.com/Dev-KceeDan?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Wellington Chinechem</b></sub></a><br /> <a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Dev-KceeDan" title="Code">💻</a> </td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/lteTraveller"><img src="https://avatars1.githubusercontent.com/lteTraveller?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sodiq Ayobami Zubair</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=lteTraveller" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/davizzle"><img src="https://avatars2.githubusercontent.com/davizzle?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Victor Ihetu</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=davizzle" title="Code">📖</a> </td>
    <td align="center"><a href="https://github.com/davizzle"><img src="https://avatars2.githubusercontent.com/Oluengine1?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rasheed Olumide Elebute</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Oluengine1" title="Code">📖</a> </td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/Enomfon-Obot"><img src="https://avatars.githubusercontent.com/Enomfon-Obot?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Enomfon Obot</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Enomfon-Obot" title="Designer">💬</a></td>
    <td align="center"><a href="https://github.com/Omolahrah"><img src="https://avatars.githubusercontent.com/Omolahrah?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Omolara Akinbola</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Omolahrah" title="Designer">💬</a></td>
    <td align="center"><a href="https://github.com/Damilola-designer"><img src="https://avatars2.githubusercontent.com/Damilola-designer?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Damilola Akinwunmi</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Damilola-designer" title="Designer">💬</a></td>
    <td align="center"><a href="https://github.com/Alqaasimy1"><img src="https://avatars2.githubusercontent.com/Alqaasimy1?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Quazeem Tiamiyu</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Alqaasimy1" title="Designer">💬</a></td>
     <td align="center"><a href="https://github.com/Irene4215"><img src="https://avatars2.githubusercontent.com/Irene4215?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Irene Jilmari Stephen</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Irene4215" title="Designer">💬</a></td>
     <td align="center"><a href="https://github.com/Zooneey"><img src="https://avatars2.githubusercontent.com/Zooneey?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Omolade Odewunmi</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Zooneey" title="Designer">💬</a></td>
     <td align="center"><a href="https://github.com/VictoryOkelue"><img src="https://avatars2.githubusercontent.com/VictoryOkelue?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Victory Okelue</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=VictoryOkelue" title="Designer">💬</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/Minahgee"><img src="https://avatars.githubusercontent.com/Minahgee?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Ibimina Georgewill</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Minahgee" title="Designer">💬</a></td>
    <td align="center"><a href="https://github.com/Jadedigba"><img src="https://avatars.githubusercontent.com/Jadedigba?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Janet Oluwadamilola Adedigba</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Jadedigba" title="Designer">💬</a></td>
    <td align="center"><a href="https://github.com/JhayEchenim"><img src="https://avatars2.githubusercontent.com/JhayEchenim?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Echenim Joy Chinyere</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=JhayEchenim" title="Designer">💬</a></td>
     <td align="center"><a href="https://github.com/Drkeyz"><img src="https://avatars2.githubusercontent.com/Drkeyz?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Adebiyi Oladimeji</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Drkeyz" title="Designer">💬</a></td>
     <td align="center"><a href="https://github.com/Damola150"><img src="https://avatars2.githubusercontent.com/Damola150?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Damola Olufowokan</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Damola150" title="Designer">💬</a></td>
     <td align="center"><a href="https://github.com/Estheragboola"><img src="https://avatars2.githubusercontent.com/Estheragboola?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Agboola Esther Oreoluwa</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=Estheragboola" title="Designer">💬</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://allcontributors.org) specification.
Contributions of any kind are welcome!

## Relevant links
  - [Live site](https://quickterms.herokuapp.com/)
  - [UX Research documention](https://docs.google.com/document/d/1T4SFiEQCYYrOaHTu2laP7x9L5mTi5jr42VCgjAVX7rI/edit?usp=sharing)
  - [Technical documentation](https://obiajuluezike.slite.com/p/LeWE1nW8ZC8iPM/QuickTerms-Technical-Documentation)
  - [Contributors details and their tasks](https://docs.google.com/spreadsheets/d/11xXrf_8M0h4MvW9oLjhe1myAj8swJUplk9y0fm1J2YQ/edit?usp=sharing)
  - [Database Schema](https://drive.google.com/file/d/1-TfYdHR8ApGuiqzOfBnUK4ddSRsvrybG/view?usp=sharing)

<!-- LICENSE -->
## LICENSE

Distributed under the MIT License. See `LICENSE.txt` for more information.

[MIT](LICENSE)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/zuri-training/Proj-T_C_Gen-Team-74.svg?style=for-the-badge
[contributors-url]: https://github.com/zuri-training/Proj-T_C_Gen-Team-74/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/zuri-training/Proj-T_C_Gen-Team-74.svg?style=for-the-badge
[forks-url]: https://github.com/zuri-training/Proj-T_C_Gen-Team-74/network/members
[stars-shield]: https://img.shields.io/github/stars/zuri-training/Proj-T_C_Gen-Team-74.svg?style=for-the-badge
[stars-url]: https://github.com/zuri-training/Proj-T_C_Gen-Team-74/stargazers
[issues-shield]: https://img.shields.io/github/issues/zuri-training/Proj-T_C_Gen-Team-74.svg?style=for-the-badge
[issues-url]: https://github.com/zuri-training/Proj-T_C_Gen-Team-74/issues
[license-shield]: https://img.shields.io/github/license/zuri-training/Proj-T_C_Gen-Team-74.svg?style=for-the-badge
[license-url]: https://github.com/zuri-training/Proj-T_C_Gen-Team-74/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/obiajulu-ezike
[product-screenshot]: /tc_site/static/assets/landing/hero/hero.png

[Django]: https://img.shields.io/badge/django-000000?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://docs.djangoproject.com/
[Javascript]: https://img.shields.io/badge/Js-20232A?style=for-the-badge&logo=javascript&logoColor=61DAFB
[Javascript-url]: https://www.javascript.com/
[Python]: https://img.shields.io/badge/Python-35495E?style=for-the-badge&logo=python&logoColor=4FC08D
[Python-url]: https://www.python.org/
[CSS3]: https://img.shields.io/badge/CSS-4A4A55?style=for-the-badge&logo=css3&logoColor=FF3E00
[CSS3-url]: https://www.w3.org/Style/CSS/Overview.en.html
[HTML5]: https://img.shields.io/badge/html-FF2D20?style=for-the-badge&logo=html5&logoColor=white
[HTML5-url]: https://html5.org/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

