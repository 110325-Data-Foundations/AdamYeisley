# pandas
# python library for working with large data sets, to do data analysis
# will be working with just one data set, and for now we'll just write a .py file

# however it is common to use pandas and other data analysis tools inside something like a jupyter notebook.

# 1st step to working with data in pandas: we have to read it in

# imports
import pandas as pd # import-as: lets us alias the module/class with an easier to reference name

# read our csv
df = pd.read_csv("./data/Electric_Vehicle_Population_Data.csv")

# pandas has built in methods for reading our data in - we dont need to go
# through the File IO that we saw last week

# that .read_csv() method produces a data frame, we need to store it in a variable in order to work with it\

# a data-frame is just a pythonic object respresetation of our data. its organized
# as rows and columns, with each column having a title. our rows are our individual
# entries in our data set.

# They are mutable and built on NumPy arrays.
# Columns can be of different data types, and we can decide the data types and change them as needed

# We can create data frames from datasets like CVS or JSON

# Inspecting data
print(df.head()) # Reads first 5 lines of dataframe

df.info() # gives metadata about dataset like columns, non-null counts, data types, etc.

print(df.describe()) # Gives summary info like count, mean, standard deviation, etc.

print(df.shape) # GIves total number of rows and columns.

# Beyond inspecrting, we can work with our data - we can select individual rows and columns, filter, etc.

# df.loc() and df.iloc() - Loc is label based selection, iloc is index based selection.

print(df.loc[1]) # Selecting a slice of entries from the dataset

print(df["Make"]) # Extract everything in one column

df.loc( 0 : 5, ['City']) 

