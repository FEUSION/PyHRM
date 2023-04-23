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

## What is PyHRM?
[PyHRM]([https://github.com/FEUSION/Extractor](https://feusion.github.io/PyHRM/)) is a python based library for processing High Resolution Melting (HRM) data, especially, DNA melting signals to extact features like 'Melting Temperatures', 'Take-off and Touch-down points of melting signal (Temperature at which peak start rising and temperature at which peak falls down)','Peak prominences',and 'Area Under the curve'. Additionally, the library offers interactive visualization for DNA melting singal and vision based filtering, to eliminate noisy signals from the data and provides only genuine peaks with all the above mentioned features.


## Installing with PIP

```
python -m pip install PyHRM
```
or
```
pip3 install PyHRM
```

## Classifiers

The following are the essential requirements for this software to run:

<table>
  <tr>
    <td nowrap><strong>Development Status</strong></td><td href = "https://pypi.org/search/?c=Development+Status+%3A%3A+5+-+Production%2FStable"><i >5 - Production/Stable </i></td>
  </tr>
  <tr>
    <td nowrap><strong>Intened Audience</strong></td><td><i>Education</i></td>
  </tr>
  <tr>
    <td nowrap><strong>License</strong></td><td><i>OSI Approved :: MIT License </i></td>
  </tr>
  <tr>
    <td nowrap><strong>Operating System</strong></td><td><i>Microsoft :: Windows :: Windows 10 </i></td>
  </tr>
  <tr>
    <td nowrap><strong>Programming Language</strong></td><td><i>Python 3</i></td>
  </tr>
</table>

## Features
- Rapid preprocessing.
- Feature Extraction
    - Tm (Melting Temperature (Max 2))
    - Tstart (Starting temperature point)
    - Tend (Ending Temperature)
    - Prominence
    - Area Under the curve
- Interactive Visulization.
- Computer Vision based thresholding for eliminating noisy signals.
- Report Generation.

## Input Data format

<p align="center">
<b>Format</b><br />
    The input format should be as followed below. 'Text','X','Y'.... 
</p>


![dataformat](https://user-images.githubusercontent.com/80576855/233830128-279608f2-42f4-4bca-84b1-1063922956db.png)

The current release only support .xls and .xlsx formats. Further updates on multiple file supports will be released in the upcoming versions.

## Setup

```
from PyHRM import melt
obj = melt.MeltcurveInterpreter()
```




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
