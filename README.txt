Parameters/Input:
This function takes in two parameters. The first parameter is a Pandas dataframe and the second is the 
threshold value that will be used to be determined if the columns should be dropped due to 
multicollinearity. 

Output:
The function drops columns that has high multicollinearity based on Variance Inflation Factor (VIF). The 
default threshold is 5, so if there are instances of columns with VIF value of more than the threshold, 
the column with the maximum VIF value will be dropped first. This process will be done iteratively until 
all columns left have VIF value less than the threshold. Thereafter, the function will output the 
dataframe with its remaining columns.
