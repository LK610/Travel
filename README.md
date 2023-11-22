<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/LK610/Travel.git">
    <img src="https://www.publicdomainpictures.net/pictures/220000/velka/travel-map.jpg" alt="Logo" width="348" height="270">
  </a>

<h3 align="center">Laura's Travel Planning Scripts & Tools</h3>

  <p align="center">
    Supports Laura's travel planning process with help from ESRI's desktop and online software.
    <br />
    <a href="https://github.com/LK610/Travel.git"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#Files">Files</a></li>
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

Laura wants to take productive vacations to Europe. She just didn't think she'd need to learn Python to do it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
[![Python][Python.com]][Python-url]
[![ArcGIS Pro][https://www.esriuk.com/content/dam/esrisites/en-us/arcgis/capabilities/data-management/data-management-2020-update/assets/capabilities-data-managment-card-arcgis-pro.jpg]][https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview]
[![ArcGIS Online][https://www.esriuk.com/content/dam/esrisites/en-us/arcgis/capabilities/data-management/data-management-2020-update/assets/capabilities-data-managment-card-arcgis-online.jpg]][https://www.esri.com/en-us/arcgis/products/arcgis-online/overview]
Authenic human tears

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Just don't. Take a cruise like a normal person.

### Prerequisites

Install packages using the ArcGIS Pro built-in package manager
* arcpy
* pandas
* os
* datetime
* PyQT5
* selenium

### Files

* Travel_Module - defines frequently used functions for the project
* MakeNewGDB.ipynb - Generates an empty geodatabase according to the data dictionary spreadsheet
* MakeReports.ipynb - Truncates and appends data into the already established 'Reporting' database to connect to layouts and reports styled in ArcGIS Pro
* GoogleScraping.ipynb - Rudimentary script to compile Regions attribute data by scraping Google maps

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Pity the fool attempting to repurpose this mess.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Validate the data model
    - [ ] Script and populate Reporting database to generate Safety Cards
    - [ ] Script and populate Reporting database to generate Itinerary for Emergency Contacts
    - [ ] Script and populate Reporting database to generate the Daily Itinerary Summaries
    - [ ] Script and populate Reporting database to generate Google calendar events in place of the detailed itineraries
- [ ] Migrate database to Production
    - [ ] Publish geodatabase schema to Production
    - [ ] Move and augment data as needed
    - [ ] Style layers and save styles within the Pro project
- [ ] Configure data collection via ArcGIS Online
    - [ ] Publish necessary datasets
    - [ ] Configure editing apps
    - [ ] Add custom functionality, if necessary

See the [open issues](https://github.com/LK610/Travel.git/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Place all blame directly on Laura.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Do you have questions, like 'Why?', 'How did you do that?' and 'Are you a masochist?'

Me too! 

Contact me at: lmmk81914@gmail.com (*Good* answers not guaranteed)

Project Link: [https://github.com/LK610/Travel.git](https://github.com/LK610/Travel.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/LK610/Travel.git.svg?style=for-the-badge
[contributors-url]: https://github.com/LK610/Travel.git/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/LK610/Travel.git.svg?style=for-the-badge
[forks-url]: https://github.com/LK610/Travel.git/network/members
[stars-shield]: https://img.shields.io/github/stars/LK610/Travel.git.svg?style=for-the-badge
[stars-url]: https://github.com/LK610/Travel.git/stargazers
[issues-shield]: https://img.shields.io/github/issues/LK610/Travel.git.svg?style=for-the-badge
[issues-url]: https://github.com/LK610/Travel.git/issues
[license-shield]: https://img.shields.io/github/license/LK610/Travel.git.svg?style=for-the-badge
[license-url]: https://github.com/LK610/Travel.git/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/laurakaufmann08
[product-screenshot]: images/screenshot.png
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Python.com]: https://www.python.org/static/img/python-logo.png
[Python-url]: https://www.python.org/