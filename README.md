<div align="center">
    <br>
        <a href="https://github.com/FEUSION/rotor-extractor"><img src="source\logo_E.png" width="250px" height="250px" alt="Software_E-logo"></a>
      <br>
    <h1>EXTRACTOR</h1>
    <h2><b>A simple automatic GUI-based data extraction tool for Q-Rex Software</b></h2>
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
        <a href="https://github.com/FEUSION/Extractor/releases/latest/tags/v1.0.0">
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

[EXTRACTOR](https://github.com/FEUSION/Extractor) is an application that has been developed to assist _Rotor-Gene_ PCR cycler users to extract raw data ".rex" files from **_Rotor-Gene Q-Rex Software Series_**


![extractor_bg](https://user-images.githubusercontent.com/126145859/229084089-d8257d94-df4c-4a0f-910f-368f641c7909.png)


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

# Why EXTRACTOR?

EXTRACTOR is an artifact from our Main project, (currently, we are working on at **[Microbiological Laboratory Research and Services, Coimbatore](https://microserv.in/)** in association with **[Microbiological Laboratory, Coimbatore](https://microlabindia.com/)**) so we opted to make an application that automatically extracts the **High Resolution Melt (HRM)** raw data (**'.rex'** files) produced by **[Qiagen's](https://www.qiagen.com/us)** _[Rotor-Gene Q](https://www.qiagen.com/us/products/discovery-and-translational-research/epigenetics/dna-methylation/methylation-specific-pcr/rotor-gene-q)_ PCR cyclers to the necessary '.xls' files from the **[Qiagen's Q-Rex Software](https://www.qiagen.com/us/applications/pcr/thermal-cyclers/q-rex-software)** and its solely for the _analytical_ purpose only.

It's very useful for the laboratories, those who run plentiful PCR experiments and have past run files, and want to export those raw data into desired excel format (.xls files) for their internal analytics team to work with that data.

# What is EXTRACTOR?

EXTRACTOR is a lightweight simple GUI-based application that extracts **'.rex'** files from the **Qiagen's Rotor-Gene Q Software** to the necessary **'.xls'** file. It's built for the users such as laboratory technicians and clinicians who handle and run PCR experiments especially in **Qiagen's Rotor-Gene Q** thermal cycler machine.

After the successful experiment ran in _Rotor-Gene Q_ cycler, it produces the raw data and the users which can be only opened and analyzed via **Qiagen's Q-Rex Software**. If a specific run file (raw data) has to be exported into desired formats such as _text_(.txt), _HTML Table_(.html), _XML_(.xml), _excel_(.xls) given by the **Qiagen Rotor-Gene Q-Rex Software**. Here we automated the user role by our **EXTRACTOR** Software, by which you simply put the raw data file directory and desired directory to which the excel files are stored in your system, which saves time and not to burned out from this repititive task.

<p align="center">
<b>Manual Conversion</b><br />
    Time consuming and often introduce frustation and inconsistency, while converting bulks of raw data by manual process.
</p>

![Manual Conversion](https://user-images.githubusercontent.com/126145859/227910822-4ef20c41-3f6b-49d7-9dce-ff611d909419.png)

<p align="center">
<b>Automatic Conversion</b><br />
    Runs in a constant time and it handle countless of raw data automatically without any human intervence.
</p>

![Automatic Conversion](https://user-images.githubusercontent.com/126145859/227910859-43c36212-5e51-4061-8e71-cf66ab2951d9.png)

# System Requirements

The following are the essential requirements for this software to run:

<table>
  <tr>
    <td nowrap><strong>Q-Rex Software</strong></td><td><i><b>Rotor-Gene Q Software v2.3.5 (Build 1)</b></i></td>
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
