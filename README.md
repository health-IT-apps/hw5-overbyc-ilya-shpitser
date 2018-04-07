# Example HW5 Group Assignment

## Team Members

1. Casey Overby Taylor (overbyc)
2. Ilya Shpitser (ilya-shpitser)

## Age at Diagnosis of Breast Cancer in Different Racial and Ethnic Groups

As a researcher I want to compare age at diagnosis of breast cancer among different racial and ethnic groups, so that I can see what groups may be diagnosed at a younger age when compared to other groups.

## Access and Running Instructions

Access our interactive chart [here](http://cot.pythonanywhere.com) or download this repository and run `python controller.py` and access this from http://127.0.0.1:5000/.

## Story Board

<img src="https://github.com/health-IT-apps/hw5-overbyc-ilya-shpitser/blob/master/storyboard.png" width="500">

### Changes between Storyboard and the Final Implementation

* Used boxplots instead of a barchart because it allows the user to better see the distribution of the data among groups.

## Development Process

* Processed data: imputed missing data in the SEER dataset, and extracted a subset of 5000 patients with variables relevant to our scenario.
* Implemented computations:  (a) determine which variables in the dataset are continuous and wich are categorical, (b) for a selected continuous variable, calculate min, max, median, and mean (used in the chart).
* Implemented an interaction: allow the user to select the x-axis and y-axis variable and to plot data as a chart.
* Implemented a chart: upon clicking the "Plot" button, generate a box-plot.
  
## Data Source Acknowledgement

* Surveillance, Epidemiology, and End Results (SEER) Program (www.seer.cancer.gov) Research Data (1973-2013), National Cancer Institute, DCCPS, Surveillance Research Program, Surveillance Systems Branch, released April 2016, based on the November 2015 submission.
