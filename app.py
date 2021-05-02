#Import Library 
import pandas as pd 

# Read CSV file 

df = pd.read_csv('wideformat_csv.csv')


#Wide Format: "Concelho", "LAT", "LONG", "dates(...)"

# Set variable "dates" from the 4th column on


dates = df.columns[4:]

# Assign to the dataframe "longformat" the melting of the wide format df
# Leave the out of the melt the first three columns, create two new columns "Data" and "INC"
# Depending on your original CSV you'll have to change these

longformat = pd.melt(df, id_vars = ['CONCELHO','LAT','LONG'],
	          value_vars=dates, 		
			  var_name='DATA',
			  value_name='INC'
			  )

# Optional - Write to CSV the resulting format 

longformat.to_csv('longformat_csv.csv', index=False)
	
