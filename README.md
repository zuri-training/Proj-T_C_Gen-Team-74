<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



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
<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:center; vertical-align: middle; padding:40px 0;">
<div align="center">
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

[![Product Name Screen Shot][product-screenshot]](https://drive.google.com/file/d/1urjsylAbPbuq1dzW0Bh-rKslK_GDVDvx/view?usp=sharing)

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
- Send emails to userson request after document generation
- Accepting user feedback after succesfull document generation.

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
For moe information about this project you can contact [@De_marauder](https://twitter.com/@De_marauder) on twitter or [github](https://github.com/de-marauder)

Project Link: [https://github.com/zuri-training/Proj-T_C_Gen-Team-74](https://github.com/zuri-training/Proj-T_C_Gen-Team-74)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [ZurixI4G](https://training.zuri.team/)
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
    <td align="center"><a href="https://github.com/de-marauder"><img src="https://avatars.githubusercontent.com/de-marauder?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Ezike Obiajulu</b></sub></a><br /><a href="#question-de_marauder" title="Answering Questions">💬</a> <a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=de-marauder" title="Documentation">📖</a> <a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/pulls?q=is%3Apr+reviewed-by%3Ade-marauder" title="Reviewed Pull Requests">👀</a> <a href="#talk-de_marauder" title="Talks">📢</a><a href="#maintenance-de_marauder" title="Maintenance">🚧</a></td>
    <td align="center"><a href="https://github.com/labodinho"><img src="https://avatars.githubusercontent.com/labodinho?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Olabode Oritogun</b></sub></a><br /><a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/commits?author=labodinho" title="Documentation">📖</a> <a href="https://github.com/zuri-training/Proj-T_C_Gen-Team-74/pulls?q=is%3Apr+reviewed-by%3Alabodinho" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://github.com/ogunkapc"><img src="https://avatars2.githubusercontent.com/ogunkapc?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ogunka Promise</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=ogunkapc" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/tbenning"><img src="https://avatars2.githubusercontent.com/u/7265547?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tyler Benning</b></sub></a><br /><a href="#maintenance-tbenning" title="Maintenance">🚧</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=tbenning" title="Code">💻</a> <a href="#design-tbenning" title="Design">🎨</a></td>
    <td align="center"><a href="https://sinchang.me"><img src="https://avatars0.githubusercontent.com/u/3297859?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jeff Wen</b></sub></a><br /><a href="#maintenance-sinchang" title="Maintenance">🚧</a> <a href="https://github.com/all-contributors/all-contributors/pulls?q=is%3Apr+reviewed-by%3Asinchang" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="http://maxcubing.wordpress.com"><img src="https://avatars0.githubusercontent.com/u/8260834?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Maximilian Berkmann</b></sub></a><br /><a href="#translation-Berkmann18" title="Translation">🌍</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=Berkmann18" title="Documentation">📖</a> <a href="#maintenance-Berkmann18" title="Maintenance">🚧</a> <a href="https://github.com/all-contributors/all-contributors/pulls?q=is%3Apr+reviewed-by%3ABerkmann18" title="Reviewed Pull Requests">👀</a> <a href="#talk-Berkmann18" title="Talks">📢</a></td>
    <td align="center"><a href="http://matheu.srv.br"><img src="https://avatars0.githubusercontent.com/u/23284276?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Matheus Rocha Vieira</b></sub></a><br /><a href="#translation-MatheusRV" title="Translation">🌍</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=MatheusRV" title="Code">💻</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=MatheusRV" title="Documentation">📖</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://robertlluberes.com"><img src="https://avatars1.githubusercontent.com/u/13991439?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Robert Lluberes</b></sub></a><br /><a href="#translation-robertlluberes" title="Translation">🌍</a></td>
    <td align="center"><a href="https://jongjineee.github.io"><img src="https://avatars2.githubusercontent.com/u/26620470?v=4?s=100" width="100px;" alt=""/><br /><sub><b>이종진</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=Jongjineee" title="Documentation">📖</a> <a href="#translation-Jongjineee" title="Translation">🌍</a></td>
    <td align="center"><a href="http://marsx.vip"><img src="https://avatars2.githubusercontent.com/u/21303543?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Wenqing Xue</b></sub></a><br /><a href="#translation-MarsXue" title="Translation">🌍</a></td>
    <td align="center"><a href="http://bogas04.github.io"><img src="https://avatars.githubusercontent.com/u/6177621?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Divjot Singh</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=bogas04" title="Documentation">📖</a> <a href="https://github.com/all-contributors/all-contributors/pulls?q=is%3Apr+reviewed-by%3Abogas04" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="http://beneb.info"><img src="https://avatars.githubusercontent.com/u/1282980?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Ben Briggs</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=ben-eb" title="Documentation">📖</a> <a href="https://github.com/all-contributors/all-contributors/pulls?q=is%3Apr+reviewed-by%3Aben-eb" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://github.com/Jameskmonger"><img src="https://avatars.githubusercontent.com/u/2037007?v=3?s=100" width="100px;" alt=""/><br /><sub><b>James Monger</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=Jameskmonger" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/chrissimpkins"><img src="https://avatars.githubusercontent.com/u/4249591?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Chris Simpkins</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=chrissimpkins" title="Documentation">📖</a> <a href="https://github.com/all-contributors/all-contributors/pulls?q=is%3Apr+reviewed-by%3Achrissimpkins" title="Reviewed Pull Requests">👀</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/fhemberger"><img src="https://avatars.githubusercontent.com/u/153481?v=3?s=100" width="100px;" alt=""/><br /><sub><b>F. Hemberger</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=fhemberger" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/frigginglorious"><img src="https://avatars.githubusercontent.com/u/3982200?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Daniel Kraft</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=frigginglorious" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/mbad0la"><img src="https://avatars.githubusercontent.com/u/8503331?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Mayank Badola</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=mbad0la" title="Documentation">📖</a> <a href="#tool-mbad0la" title="Tools">🔧</a></td>
    <td align="center"><a href="https://www.marcobiedermann.com"><img src="https://avatars.githubusercontent.com/u/5244986?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Marco Biedermann</b></sub></a><br /><a href="#design-marcobiedermann" title="Design">🎨</a></td>
    <td align="center"><a href="https://github.com/itaisteinherz"><img src="https://avatars.githubusercontent.com/u/22768990?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Itai Steinherz</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=itaisteinherz" title="Documentation">📖</a></td>
    <td align="center"><a href="http://nodescription.net"><img src="https://avatars1.githubusercontent.com/u/305339?v=3?s=100" width="100px;" alt=""/><br /><sub><b>Patrick Connolly</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=patcon" title="Documentation">📖</a></td>
    <td align="center"><a href="http://nikolalsvk.github.io/"><img src="https://avatars2.githubusercontent.com/u/3028124?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nikola Đuza</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=nikolalsvk" title="Documentation">📖</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://dem.be"><img src="https://avatars2.githubusercontent.com/u/5346497?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Demian Dekoninck</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=DemianD" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/mpeyper"><img src="https://avatars0.githubusercontent.com/u/23029903?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Michael Peyper</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=mpeyper" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/The24thDS"><img src="https://avatars0.githubusercontent.com/u/26633429?v=4?s=100" width="100px;" alt=""/><br /><sub><b>David Sima</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=The24thDS" title="Documentation">📖</a> <a href="#translation-The24thDS" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/all-contributors/all-contributors-bot"><img src="https://avatars3.githubusercontent.com/u/46843839?v=4?s=100" width="100px;" alt=""/><br /><sub><b>allcontributors[bot]</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=allcontributors" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/apps/greenkeeper"><img src="https://avatars3.githubusercontent.com/in/505?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Greenkeeper[bot]</b></sub></a><br /><a href="#infra-Greenkeeper[bot]" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/maryampaz"><img src="https://avatars1.githubusercontent.com/u/30090413?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Maryam Pazirandeh</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=maryampaz" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/CassVenere"><img src="https://avatars1.githubusercontent.com/u/47280556?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Cassandra Venere</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=CassVenere" title="Documentation">📖</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.codimiracle.com"><img src="https://avatars2.githubusercontent.com/u/21952540?v=4?s=100" width="100px;" alt=""/><br /><sub><b>codimiracle</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=codimiracle" title="Documentation">📖</a></td>
    <td align="center"><a href="https://twitter.com/dance2die"><img src="https://avatars1.githubusercontent.com/u/8465237?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sung Kim</b></sub></a><br /><a href="#translation-dance2die" title="Translation">🌍</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=dance2die" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/tphbrok"><img src="https://avatars0.githubusercontent.com/u/11331876?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Thomas Brok</b></sub></a><br /><a href="#translation-tphbrok" title="Translation">🌍</a></td>
    <td align="center"><a href="https://robert.theguys.sh"><img src="https://avatars0.githubusercontent.com/u/35585466?v=4?s=100" width="100px;" alt=""/><br /><sub><b>robertgrzonka</b></sub></a><br /><a href="#translation-robertgrzonka" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/askareija"><img src="https://avatars3.githubusercontent.com/u/21377617?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Megumi Aliya</b></sub></a><br /><a href="#translation-askareija" title="Translation">🌍</a></td>
    <td align="center"><a href="https://yuhang.live"><img src="https://avatars3.githubusercontent.com/u/13712499?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Yule</b></sub></a><br /><a href="#translation-YuleYu" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/s-pace"><img src="https://avatars2.githubusercontent.com/u/32097720?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sylvain Pace</b></sub></a><br /><a href="#plugin-s-pace" title="Plugin/utility libraries">🔌</a></td>
  </tr>
  <tr>
    <td align="center"><a href="http://www.peterhuerlimann.li"><img src="https://avatars2.githubusercontent.com/u/18031711?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Peter Hürlimann</b></sub></a><br /><a href="#translation-peterhuerlimann" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/thiagodp"><img src="https://avatars3.githubusercontent.com/u/2997844?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Thiago Delgado Pinto</b></sub></a><br /><a href="#translation-thiagodp" title="Translation">🌍</a></td>
    <td align="center"><a href="https://rogeriopradoj.com"><img src="https://avatars3.githubusercontent.com/u/443391?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rogerio Prado de Jesus</b></sub></a><br /><a href="#translation-rogeriopradoj" title="Translation">🌍</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/turbolego/"><img src="https://avatars3.githubusercontent.com/u/2650749?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tobias Andersen</b></sub></a><br /><a href="#translation-turbolego" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/danielbronder"><img src="https://avatars2.githubusercontent.com/u/9819957?v=4?s=100" width="100px;" alt=""/><br /><sub><b>danielbronder</b></sub></a><br /><a href="#translation-danielbronder" title="Translation">🌍</a></td>
    <td align="center"><a href="http://lattes.cnpq.br/4287615973321905"><img src="https://avatars3.githubusercontent.com/u/28638133?v=4?s=100" width="100px;" alt=""/><br /><sub><b>João Pedro Raskopf</b></sub></a><br /><a href="#translation-jprask" title="Translation">🌍</a></td>
    <td align="center"><a href="http://edwinvargas.com.ve"><img src="https://avatars0.githubusercontent.com/u/9091905?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Edwin Vargas</b></sub></a><br /><a href="#translation-edwinvrgs" title="Translation">🌍</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://kanout.com"><img src="https://avatars0.githubusercontent.com/u/6838659?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Faisal KANOUT</b></sub></a><br /><a href="#translation-fkanout" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/johnmurphy01"><img src="https://avatars2.githubusercontent.com/u/2939548?v=4?s=100" width="100px;" alt=""/><br /><sub><b>John Murphy</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=johnmurphy01" title="Documentation">📖</a></td>
    <td align="center"><a href="https://whitakerlab.github.io"><img src="https://avatars1.githubusercontent.com/u/3626306?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kirstie Whitaker</b></sub></a><br /><a href="#ideas-KirstieJane" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/sirpeas"><img src="https://avatars3.githubusercontent.com/u/4818642?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Patryk Peas</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=sirpeas" title="Documentation">📖</a> <a href="#translation-sirpeas" title="Translation">🌍</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=sirpeas" title="Code">💻</a></td>
    <td align="center"><a href="https://almostover.ru"><img src="https://avatars2.githubusercontent.com/u/16944225?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ivan.Nginx</b></sub></a><br /><a href="#translation-ivan-nginx" title="Translation">🌍</a></td>
    <td align="center"><a href="http://levy.work"><img src="https://avatars3.githubusercontent.com/u/9384365?v=4?s=100" width="100px;" alt=""/><br /><sub><b>levy</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=levy9527" title="Documentation">📖</a></td>
    <td align="center"><a href="https://piksel.se"><img src="https://avatars2.githubusercontent.com/u/807383?v=4?s=100" width="100px;" alt=""/><br /><sub><b>nils måsén</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=piksel" title="Documentation">📖</a></td>
  </tr>
  <tr>
    <td align="center"><a href="http://uraway.hatenablog.com/"><img src="https://avatars3.githubusercontent.com/u/15242484?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Masato Urai (@uraway_)</b></sub></a><br /><a href="#translation-uraway" title="Translation">🌍</a></td>
    <td align="center"><a href="https://kylemh.com"><img src="https://avatars1.githubusercontent.com/u/9523719?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kyle Holmberg</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=kylemh" title="Documentation">📖</a></td>
    <td align="center"><a href="http://www.arcticbit.se"><img src="https://avatars0.githubusercontent.com/u/1596025?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Simon Aronsson</b></sub></a><br /><a href="#translation-simskij" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/BayCem"><img src="https://avatars0.githubusercontent.com/u/21110691?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Cem</b></sub></a><br /><a href="#translation-BayCem" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/fennecdjay"><img src="https://avatars0.githubusercontent.com/u/4943921?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jérémie Astor</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=fennecdjay" title="Documentation">📖</a></td>
    <td align="center"><a href="https://rachelcarmena.github.io"><img src="https://avatars0.githubusercontent.com/u/22792183?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rachel M. Carmena</b></sub></a><br /><a href="#translation-rachelcarmena" title="Translation">🌍</a></td>
    <td align="center"><a href="https://sno2wman.dev/"><img src="https://avatars3.githubusercontent.com/u/15155608?v=4?s=100" width="100px;" alt=""/><br /><sub><b>SnO₂WMaN</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=SnO2WMaN" title="Documentation">📖</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/cesar-richard"><img src="https://avatars0.githubusercontent.com/u/5199868?v=4?s=100" width="100px;" alt=""/><br /><sub><b>César Richard</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=cesar-richard" title="Documentation">📖</a> <a href="#userTesting-cesar-richard" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/kharaone"><img src="https://avatars1.githubusercontent.com/u/6599271?v=4?s=100" width="100px;" alt=""/><br /><sub><b>kharaone</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=kharaone" title="Documentation">📖</a></td>
    <td align="center"><a href="http://thefactsbook.com"><img src="https://avatars0.githubusercontent.com/u/24487349?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mudassar Ali</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=Mudassar045" title="Documentation">📖</a></td>
    <td align="center"><a href="https://www.andrewmason.me/"><img src="https://avatars1.githubusercontent.com/u/18423853?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Andrew Mason</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=andrewmcodes" title="Documentation">📖</a></td>
    <td align="center"><a href="https://maurom.dev"><img src="https://avatars1.githubusercontent.com/u/22800592?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mauro M.</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=MM-coder" title="Documentation">📖</a></td>
    <td align="center"><a href="https://phacks.dev/"><img src="https://avatars1.githubusercontent.com/u/2587348?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nicolas Goutay</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=phacks" title="Documentation">📖</a></td>
    <td align="center"><a href="http://phor.net"><img src="https://avatars0.githubusercontent.com/u/382183?v=4?s=100" width="100px;" alt=""/><br /><sub><b>William Entriken</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=fulldecent" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://linkedin.com/in/kytwb"><img src="https://avatars0.githubusercontent.com/u/412895?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Amine</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=kytwb" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/smoia"><img src="https://avatars3.githubusercontent.com/u/35300580?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Stefano Moia</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=smoia" title="Documentation">📖</a></td>
    <td align="center"><a href="http://adamtuttle.codes"><img src="https://avatars2.githubusercontent.com/u/46990?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Adam Tuttle</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=atuttle" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/NotMoni"><img src="https://avatars2.githubusercontent.com/u/40552237?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Moni</b></sub></a><br /><a href="#infra-NotMoni" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/ilai-deutel"><img src="https://avatars0.githubusercontent.com/u/10098207?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ilaï Deutel</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=ilai-deutel" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/nhnb"><img src="https://avatars1.githubusercontent.com/u/364184?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Hendrik Brummermann</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=nhnb" title="Documentation">📖</a></td>
    <td align="center"><a href="https://www.weareaccess.co.uk/"><img src="https://avatars0.githubusercontent.com/u/4610533?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sang Lostrie</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/issues?q=author%3Abaikho" title="Bug reports">🐛</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/xinbenlv"><img src="https://avatars2.githubusercontent.com/u/640325?v=4?s=100" width="100px;" alt=""/><br /><sub><b>xinbenlv</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=xinbenlv" title="Documentation">📖</a></td>
    <td align="center"><a href="https://paulovich.net"><img src="https://avatars3.githubusercontent.com/u/7133698?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ivan Paulovich</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=ivanpaulovich" title="Documentation">📖</a></td>
    <td align="center"><a href="https://www.jakewiesler.com"><img src="https://avatars1.githubusercontent.com/u/12075916?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jake Wiesler</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=jakewies" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/MicaelJarniac"><img src="https://avatars0.githubusercontent.com/u/19514231?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Micael Jarniac</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/issues?q=author%3AMicaelJarniac" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/mloning/"><img src="https://avatars3.githubusercontent.com/u/21020482?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Markus Löning</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=mloning" title="Documentation">📖</a></td>
    <td align="center"><a href="https://austinhuang.me"><img src="https://avatars1.githubusercontent.com/u/16656689?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Austin Huang</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=austinhuang0131" title="Documentation">📖</a></td>
    <td align="center"><a href="http://www.nils-andresen.de"><img src="https://avatars3.githubusercontent.com/u/349188?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nils Andresen</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=nils-a" title="Documentation">📖</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/LaChapeliere"><img src="https://avatars2.githubusercontent.com/u/7062546?v=4?s=100" width="100px;" alt=""/><br /><sub><b>LaChapeliere</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=LaChapeliere" title="Documentation">📖</a></td>
    <td align="center"><a href="https://dev.to/mbiesiad"><img src="https://avatars0.githubusercontent.com/u/18367606?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Michal</b></sub></a><br /><a href="#translation-mbiesiad" title="Translation">🌍</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/alitorki/"><img src="https://avatars1.githubusercontent.com/u/9049092?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ali Torki</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=ali-master" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/jsoref"><img src="https://avatars0.githubusercontent.com/u/2119212?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Josh Soref</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=jsoref" title="Documentation">📖</a></td>
    <td align="center"><a href="https://www.taiizor.com"><img src="https://avatars.githubusercontent.com/u/41683699?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Taiizor</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=Taiizor" title="Code">💻</a></td>
    <td align="center"><a href="https://bandism.net/"><img src="https://avatars.githubusercontent.com/u/22633385?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ikko Ashimine</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=eltociear" title="Documentation">📖</a></td>
    <td align="center"><a href="https://twitter.com/MatthewTFoley"><img src="https://avatars.githubusercontent.com/u/3792749?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Matthew</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=mtfoley" title="Documentation">📖</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/corneliusroemer"><img src="https://avatars.githubusercontent.com/u/25161793?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Cornelius Roemer</b></sub></a><br /><a href="#design-corneliusroemer" title="Design">🎨</a></td>
    <td align="center"><a href="https://turnipguy30.github.io"><img src="https://avatars.githubusercontent.com/u/50542928?v=4?s=100" width="100px;" alt=""/><br /><sub><b>JohnnySD</b></sub></a><br /><a href="#content-TurnipGuy30" title="Content">🖋</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=TurnipGuy30" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/mwaitzman"><img src="https://avatars.githubusercontent.com/u/51432220?v=4?s=100" width="100px;" alt=""/><br /><sub><b>mwaitzman</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=mwaitzman" title="Documentation">📖</a></td>
    <td align="center"><a href="https://kachick.github.io/"><img src="https://avatars.githubusercontent.com/u/1180335?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kenichi Kamiya</b></sub></a><br /><a href="https://github.com/all-contributors/all-contributors/commits?author=kachick" title="Documentation">📖</a></td>
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
[product-screenshot]: /tc_site/assets/landing/hero/hero.png

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

