# dallas_covid_testing
Looking at Dallas (city) covid-19 testing data


I found testing data for Dallas [here](https://public.tableau.com/views/Book3_15862351183220/DallasCountyLabReports?:display_count=y&:origin=viz_share_link). I manually
tabulated the tests per day and positive results. I wrote python scripts to plot the following:


1. Positive results per day (cases per day)
2. tests per day
3. Percent positive test results per day



# Outlier removal


I used a linear program [of my devising](https://www.reidatcheson.com/linear%20program/covid19/smoothing/2020/04/28/covid19-smooth.html) to draw the trend lines
in a way that was robust to outliers. 
