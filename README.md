![y](https://user-images.githubusercontent.com/80576855/233824868-99358619-cc04-415c-9f55-94d105fa8d3d.png)
<div align="center">
    <br>
        <a href="" width="250px" height="250px" alt="Software_E-logo"></a>
      <br>
    <h1>PyHRM</h1>
    <h2><b>A library for processing DNA Melting signal with feature extraction and thresholding.</b></h2>
        <h4>
        <a href="#system-requirements">Requirements</a>
        •
        <a href="#getting-started">Getting Started</a>
        •
        <a href="#features">Features</a>
        •
        <a href="#demo">Demo</a>
    </h4>
    <h3>
        <a href="#meet-the-team">
            <img src="https://img.shields.io/badge/maintainers-The Team-cyan" alt="Maintainers">
        </a>
        <a href="https://github.com/FEUSION/Extractor/releases/latest/tags/v0.0.1">
            <img src="https://img.shields.io/badge/launched-April%202023-teal" alt="Release">
        </a>
        <a href="https://github.com/FEUSION/Extractor/releases/latest">
        <img src="https://img.shields.io/github/release/MLRS-dev/Extractor?color=brightgreen&label=version" alt="Version">
        </a>
        <a href="https://www.microsoft.com/en-in/software-download/">
        <img src="https://img.shields.io/badge/platform-Windows-blue" alt="Operating system">
      </a>
      <a href="https://github.com/FEUSION/Extractor/commits/main">
      <img src="https://img.shields.io/github/last-commit/FEUSION/Extractor?color=blueviolet&label=updated">
      </a>
    </h3>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>📌 Table of Contents</summary>
  <ol>
    <li>
      <a href="#why-extractor">Why EXTRACTOR?</a>
    </li>
    <li>
    <a href="#what-is-extractor">What is EXTRACTOR?</a>
    </li>
    <li><a href="#system-requirements">System Requirements</a></li>
    <li><a href="#features">Features</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#setup">Setup</a></li>
      </ul>
    </li>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#getting-help">Getting Help</a></li>
    <li><a href="#meet-the-team">Meet the Team</a></li>
  </ol>
</details>

<br />

# What is PyHRM?
[PyHRM]([https://github.com/FEUSION/Extractor](https://feusion.github.io/PyHRM/)) is a python based library for processing HRM data, especially, DNA melting signals to extact features like 'Melting Temperatures', 'Take-off and Touch-down points of melting signal (Temperature at which peak start rising and temperature at which peak falls down)','Peak prominences',and 'Area Under the curve'. Additionally, the library offers vision based filtering, to eliminate noisy signals from the data and provides only genuine peaks with all the above mentioned features.


# Installing with PIP

```
python -m pip install PyHRM
```
or
```
pip3 install PyHRM
```

# System Requirements

The following are the essential requirements for this software to run:

<table>
  <tr>
    <td nowrap><strong>Development Status</strong></td><td href = "https://pypi.org/search/?c=Development+Status+%3A%3A+5+-+Production%2FStable"><i ><b >5 - Production/Stable </b></i></td>
  </tr>
  <tr>
    <td nowrap><strong>Platforms</strong></td><td><i>Windows</i></td>
  </tr>
</table>

# Features
- Able to set user credentials.
- Selection of which type of data to extract from the raw data, i.e.,
    - CT (Amplification Curve)
    - MELT (derivative) &
    - HRM (Normalized fluorescence)
- Supports desired output format as excel file.

# Getting Started

It is easy to get started, you can download the executable zip file [here](https://github.com/FEUSION/Extractor/releases/latest/download/EXTRACTOR-v1.0.0.zip)

# Setup

1. Go to the unzipped application folder.

![folder](https://user-images.githubusercontent.com/126145859/228214338-2dbcedb7-74bd-43ac-acf2-57e372cc806e.jpg)


2. Find the executable file and run it.

![app](https://user-images.githubusercontent.com/126145859/229074435-de70dc29-2d13-4245-932b-cacd9ad72cf3.jpg)


3. After the successful installation, register with new user credentials

> **Note**:
> - An user can able to set only two new user credentials.
> - Username is  case-sensitive.

![signup_user](https://user-images.githubusercontent.com/126145859/229084487-5184df34-ccce-4e87-9cae-9ab78d4c62d7.png)


## Type of data to extract

Select the type of data from the drop-down menu and enter the respected fields below and finally enter submit.

![types](https://user-images.githubusercontent.com/126145859/229084427-a837e98a-fbc9-451c-9ff7-51c30f41b3df.png)

Let the Extractor do it.


# Demo

To see the detailed demo of this application, click [here](https://youtu.be/4sDumV86qFI)

# Getting Help

If you need to get in touch with the team, please contact through email address: [feusion.ai@gmail.com](mailto:feusion.ai@gmail.com?subject=Extractor%20Application)

# Meet the Team

   The developers in this project are post graduate students in the [Department of Computer Applications](https://b-u.ac.in/23/department-computer-applications) @ [Bharathiar University](https://b-u.ac.in/)
<table style="width:25%">
  <tbody>
    <tr>
      <td align="center" valign="top"><a href="https://github.com/rajag0pal"><img src="https://avatars.githubusercontent.com/u/80576855?v=4" width="50px;" alt="Rajagopal S"/><br /><sub><b><a href="https://www.linkedin.com/in/rajagopal-s/">Rajagopal S</a></b></sub></a><br /></td>
      <td align="center" valign="top"><a href="https://github.com/VIGNESH-R-06"><img src="https://avatars.githubusercontent.com/u/94525493?v=4" width="50px;" alt="Vignesh R"/><br /><sub><b><a href="https://www.linkedin.com/in/vignesh-r-31b5601b8/">Vignesh R</a></b></sub></a><br /></td>
      <td align="center" valign="top"><a href="https://github.com/IamSenthilKumar"><img src="https://avatars.githubusercontent.com/u/89689985?v=4" width="50px;" alt="Senthil Kumar N"/><br /><sub><b><a href="https://www.linkedin.com/in/senthilkumar-n/">N.S.K</a></b></sub></a><br /></td>
    </tr>
  </tbody>
</table>
