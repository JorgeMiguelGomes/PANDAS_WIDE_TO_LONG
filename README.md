# PANDAS_WIDE_TO_LONG
A Python script to convert a wide csv to long csv 

## REQURMENTS 

Pandas library 

## BRIEF EXPLNATION 
I've decided to publish this very simple Python script because for a beginner, like me, there is a lack of examples, in plain language to transform a wide csv file into a long format csv file.
The truth is: technical documentation is written by technical people and the entry level is not as easy as tehcnical people think. 

## EXAMPLE

For this script I used a quite complex wide format csv that has 145 columns and 278 rows. It's COVID-19 data from Portugal, compiled by all of us at [@VOSTPT](https://github.com/vostpt)

The structure of the wide format csv is as follows 

| CONCELHO | LAT | LONG | DATE 1 | DATE 2 | DATE 3 to DATE 144     | DATE 145 |
|----------|-----|------|--------|--------|----------|----------|
| COUNTY 1 | X.XX| X.XX | value  | value  | values    | value   |
| COUNTIES 2 - 277  | X.XX| Y.YY | value  | value  | values    | value   |
| COUNTY 278 | X.XX| X.XX | value  | value  | values    | value   |



In order to work with most data analysis and graphical packages that exist, we need to use something called a "Long Format". 
Basically we need to turn the above into this
| CONCELHO | LAT | LONG | DATA | VALUE |
|----------|-----|------|------|-------|
| COUNTY 1 | X.XX |Y.YY| DATE 1 | VALUE (DATE 1 ) |
| COUNTY 2 | X.XX |Y.YY| DATE 1 | VALUE (DATE 1 ) |
| COUNTY 278 | X.XX |Y.YY| DATE 1 | VALUE (DATE 1 ) |
| COUNTY 1 | X.XX |Y.YY| DATE 145 | VALUE (DATE 1 ) |
| COUNTY 2 | X.XX |Y.YY| DATE 145 | VALUE (DATE 1 ) |
| COUNTY 278 | X.XX |Y.YY| DATE 145 | VALUE (DATE 1 ) |

## THE SCRIPT 

This script allows you to take any **wide format** data file into a **long format** datafile

We start by importing the pandas library 

Then we assign a variable "df" to the result of reading the datafile 

As you can see by the example we have 3 columns (CONCELHO, LAT, LONG) that we want to keep, and the dates start from the 4th column on

We assign a variable called "dates" to all the columns from the 4th column on 

Then we create a variable called "longform" and use ```pd.melt``` to do the following 

- Based on the our "df" dataframe we tell Pandas to keep CONCELHO, LAT, LONG
- We tell Pandas to use our variable "dates" to create two new columns, one based "DATA", and one named "INC"

From this moment on you can start working with your long format dataframe [as I did here](https://github.com/JorgeMiguelGomes/COVID19MAP2021/blob/main/app.py) or you can
save the result to a csv file. 

## CONCLUSIONS

After understanding how ```pd.melt``` or ```pandas.melt``` work it's quite easy to transform a wide format datafile into a long format. However the documentation that exists, for those
that are beginning, it's not ver clear. I hope that this script and explanation can be helpful. 





