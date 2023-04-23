![pyHRM](https://user-images.githubusercontent.com/80576855/233845390-87e32c95-b170-44b3-b1fb-82baaadea8e6.png)

<div align="center">
    <br>
        <a href="" width="250px" height="250px" alt="pyHRM"></a>
      <br>
    <h1>PyHRM</h1>
    <h2><b>A library for processing DNA Melting signal with feature extraction and thresholding.</b></h2>
        <h4>
        <a href="#installing-with-pip">Installation</a>
        •
        <a href="#features">Features</a>
        •
        <a href="#documentation">Documentation</a>
        •
        <a href="#getting-help">Help</a>
    </h4>
    <h3>
        <img alt="PyPI" src="https://img.shields.io/pypi/v/pyhrm?color=blue"> 
        <a href="https://github.com/FEUSION/pyHRM/releases/latest">
            <img src="https://img.shields.io/badge/released-April%202023-teal" alt="Release">
        </a>                                                                                     
        <a href="https://www.python.org/downloads/">
            <img src="https://img.shields.io/badge/python-3.10 | 3.11-blue" alt="python">
      </a>
      <a href="https://github.com/FEUSION/pyHRM/commits/main">
      <img src="https://img.shields.io/github/last-commit/FEUSION/pyHRM?color=blueviolet&label=updated">
      </a>
      <img src="https://static.pepy.tech/personalized-badge/pyhrm?period=month&units=international_system&left_color=black&right_color=orange&left_text=PyPI%20total%20downloads%20" alt="pypi downloads">
        <a href="#meet-the-team">
            <img src="https://img.shields.io/badge/maintainers-The Team-cyan" alt="Maintainers">
        </a>
    </h3>
</div>

# PyHRM
[PyHRM]() is a python based library for processing <span><b>High Resolution Melting (HRM)</b> data, especially, DNA melting signals to extact features like <i>'Melting Temperatures', 'Take-off and Touch-down points of melting signal (Temperature at which peak start rising and temperature at which peak falls down)','Peak prominences',and 'Area Under the curve'</i>. Additionally, the library offers interactive visualization for DNA melting singal and vision based filtering, to eliminate noisy signals from the data and provides only genuine peaks with all the above mentioned features.<span>


## Installing with PIP

```
python -m pip install PyHRM
```
or
```
pip3 install PyHRM
```

## Classifiers


<table>
  <tr>
    <td nowrap><strong>Development Status</strong></td><td href = "https://pypi.org/search/?c=Development+Status+%3A%3A+5+-+Production%2FStable"><i >5 - Production/Stable </i></td>
  </tr>
  <tr>
    <td nowrap><strong>Intened Audience</strong></td><td><i>Healthcare</i></td>
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

# Documentation

## Import
```
from PyHRM import melt
```
## Creating the class Instance
```
obj = melt.MeltcurveInterpreter()
```
## PyHRM.melt.MeltcurveInterpreter.data_read

```
PyHRM.melt.MeltcurveInterpreter.data_read(data = None, path = None, labels =False, index = False, figure = False)
```

The function takes either a pandas dataframe or the path of the file (.xls, .xlsx). The method could read CT, MELT and raw fluorescence data as well.

<b>Parameters:</b>&emsp;<b>data : </b><i><b>pandas dataframe object</b></i>
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;A pandas dataframe with the specified input format of HRM data extracted from machines.
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;<b>path : </b></b><i><b>path of the file (.xls or .xlsx)</b></i><br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;A path of the HRM data file extracted from machines.
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;<b>labels : </b></b><i><b>bool : default False</b></i><br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Returns a list containing dataframe and label of the samples given in the 'Text' attribute based on a boolean value.
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;<b>index : </b></b><i><b>bool : default False</b></i><br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Required a boolean value to remove the index (if the HRM data has.)
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;<b>figure : </b></b><i><b>bool : default False</b></i><br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Required a boolean value to render a interactive plot in the browser.
<br>
<br>
<b>Returns: &emsp;&nbsp;</b>&emsp;<b>x, y cordinates : </b><i><b>pandas.core.frame.DataFrame</b></i>
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;A pandas dataframe with the temperature co-ordinates as 'X' and the signal co-ordinates as 'Y','Y.1'..'Y.n'
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;<b>x,y cordinates and labels : </b></b><i><b>list</b></i><br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;If <i>lables</i> is True, returns a list containing a dataframe and lables
<br>
<br>
<b>Warns: &emsp;&nbsp;</b>&emsp;<b>ValueError</b>
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Raised when unsupported data format passed.

<br>

### Example
```
from PyHRM import melt
obj = melt.MeltcurveInterpreter()

#reading the HRM data
hrmdata = obj.data_read(path = './path/file.xls', figure = True)
```
Alternatively,
```
import pandas as pd
import openpyxl
from PyHRM import melt
obj = melt.MeltcurveInterpreter()

#reading data with pandas
data = pd.read_excel('./path/file.xls', engine = 'xlrd')

#passing the dataframe to the function
hrmdata = obj.data_read(data = data, figure = True)
```
## PyHRM.melt.MeltcurveInterpreter.plot
```
PyHRM.melt.MeltcurveInterpreter.plot(data,save = False)
```

The function takes a pandas dataframe contains signal values and render back the respective figure. The plot function takes any data like CT, MELT and as well as raw fluorescence, and gives back the corresponding visulazation.

<b>Parameters:</b>&emsp;<b>data : </b><i><b>pandas dataframe object</b></i>
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;A pandas dataframe contains signal values.
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;<b>save : </b></b><i><b>bool : default False</b></i><br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Required a boolean value to save the plot in a figure object.
<br>
<br>
<b>Returns: &emsp;&nbsp;</b>&emsp;<b>figure: </b><i><b>plotly.graph_objs._figure.Figure</b></i>
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Returns an interactive plotly figure object.

<br>

### Example
```
from PyHRM import melt
obj = melt.MeltcurveInterpreter()

#reading the HRM data
hrmdata = obj.data_read(path = './path/file.xls')

#visualizing the data
fig = obj.plot(data = hrmdata, save = True)
fig.show()
```
## PyHRM.melt.MeltcurveInterpreter.melt_conversion
```
PyHRM.melt.MeltcurveInterpreter.plot(figure = False, return_value =False, download = False)
```
This methods only works for raw fluorescence data, and the input of this method is the class member itself. It converts the raw fluorescence signals into melting signals with signal smoothening. 
<br>
<b>NOTE : This method is the beta version of the library, the results may not be acuratae or appropriate and this is still in development</b>

<b>Parameters:</b>&emsp;<b>figure : </b><i><b>bool : default False</b></i>
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Required a boolean value to render the resultant values as a plot.
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;<b>return_value : </b></b><i><b>bool : default False</b></i><br>   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Required a boolean value to return the result as dataframe.
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;<b>download : </b></b><i><b>bool : default False</b></i><br> 
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Required a boolean value to save the resultant values as comma separated values.
<br>
<br>
<b>Returns: &emsp;&nbsp;</b>&emsp;<b>melt signal co-ordinates: </b><i><b>pandas.core.frame.DataFrame</b></i>
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Returns a dataframe, contains melting signal co-ordinates.

<br>

### Example
```
from PyHRM import melt
obj = melt.MeltcurveInterpreter()

#reading the raw fluorescence data
rfdata = obj.data_read(path = './path/file.xls')

meltdata = obj.melt_conversion(return_value = True, figure = True, download = True)
```
## PyHRM.melt.MeltcurveInterpreter.feature_detection
```
PyHRM.melt.MeltcurveInterpreter.plot(return_values =False, download = False)
```
This methods performs feature extraction process on melting signal data, that extracts features like <i>'Tm','Tstart','Tend','Prominence','Area under the curve'</i>. This also performs noise elimination using a trained CNN model embedded in the package. The input of the method is the class member itself.
<br>

<b>Parameters:</b>&emsp;<b>return_values : </b><i><b>bool : default False</b></i>
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Required a boolean value to return the result as dataframe.
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;<b>download : </b></b><i><b>bool : default False</b></i><br> 
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Required a boolean value to save the resultant values as comma separated values.
<br>
<br>
<b>Returns: &emsp;&nbsp;</b>&emsp;<b>Features of the signal: </b><i><b>pandas.core.frame.DataFrame</b></i>
<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Returns a dataframe, contains features of melting signals
<br>

### Example
```
from PyHRM import melt
obj = melt.MeltcurveInterpreter()

#reading the HRM data
hrmdata = obj.data_read(path = './path/file.xls')

#Extracting features of the melt signals
features = obj.feature_detection(return_values = True)
```
<br>

## PyHRM.melt.MeltcurveInterpreter.report
```
PyHRM.melt.MeltcurveInterpreter.report()
```
The method generates a report with the feature extracting data and it's corresponding melting signal figures.

<b>Parameters:</b>&emsp;<b>None</b>
<br>
### Example
```
from PyHRM import melt
obj = melt.MeltcurveInterpreter()

#reading the HRM data
hrmdata = obj.data_read(path = './path/file.xls')

#Extracting features of the melt signals
features = obj.feature_detection(return_values = True)

#Generating the report
obj.report()
```

# Getting Help

If you need to get in touch with the team, please contact through email address: [feusion.ai@gmail.com](mailto:feusion.ai@gmail.com?subject=Extractor%20Application)

# Meet the Team

   The developers in this project are post graduate students in the [Department of Computer Applications](https://b-u.ac.in/23/department-computer-applications) @ [Bharathiar University](https://b-u.ac.in/)
<table style="width:30%">
  <tbody>
    <tr>
      <td align="center" valign="top" width="15%"><a href="https://github.com/rajag0pal"><img src="https://avatars.githubusercontent.com/u/80576855?v=4" width="50px;" alt="Rajagopal Shanmugam"/><br /><sub><b><a href="https://www.linkedin.com/in/rajagopal-s/">Rajagopal S</a></b></sub></a><br /></td>
      <td align="center" valign="top" width="15%"><a href="https://github.com/VIGNESH-R-06"><img src="https://avatars.githubusercontent.com/u/94525493?v=4" width="50px;" alt="Vignesh Ravi"/><br /><sub><b><a href="https://www.linkedin.com/in/vignesh-r-31b5601b8/">Vignesh R</a></b></sub></a><br /></td>
      <td align="center" valign="top" width="15%"><a href="https://github.com/IamSenthilKumar"><img src="https://avatars.githubusercontent.com/u/89689985?v=4" width="50px;" alt="Senthil Kumar Nallendran"/><br /><sub><b><a href="https://www.linkedin.com/in/senthilkumar-n/">Senthil Kumar N</a></b></sub></a><br /></td>
    </tr>
  </tbody>
</table>
