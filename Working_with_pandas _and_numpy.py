#!/usr/bin/env python
# coding: utf-8

# <h1>Activity: Dataframes with pandas</h1>

# ## Introduction
# 
# Your work as a data professional for the U.S. Environmental Protection Agency (EPA) requires you to analyze air quality index data collected from the United States and Mexico.
# 
# The air quality index (AQI) is a number that runs from 0 to 500. The higher the AQI value, the greater the level of air pollution and the greater the health concern. For example, an AQI value of 50 or below represents good air quality, while an AQI value over 300 represents hazardous air quality. Refer to this guide from [AirNow.gov](https://www.airnow.gov/aqi/aqi-basics/) for more information.
# 
# In this lab, you will practice working in pandas. You will load a dataframe, examine its metadata and summary statistics, and explore it using iloc indexing and sorting. You will also practice Boolean masking, grouping, and concatenating data.

# ## Tips for completing this lab
# 
# As you navigate this lab, keep the following tips in mind:
# 
# - `### YOUR CODE HERE ###` indicates where you should write code. Be sure to replace this with your own code before running the code cell.
# - Feel free to open the hints for additional guidance as you work on each task.
# - To enter your answer to a question, double-click the markdown cell to edit. Be sure to replace the "[Double-click to enter your responses here.]" with your own answer.
# - You can save your work manually by clicking File and then Save in the menu bar at the top of the notebook.
# - You can download your work locally by clicking File and then Download and then specifying your preferred file format in the menu bar at the top of the notebook.

# ## Task 1: Read data from csv file into a pandas dataframe
# 
# You are given two files of data. Begin with the first file, which contains the three states with the most observations (rows): California, Texas, and Pennsylvania.

# ### 1a: Import statements
# 
# Import numpy and pandas. Use their standard aliases.

# In[45]:


### YOUR CODE HERE ###
import numpy as np
import pandas as pd


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Begin with the `import` keyword for each statement.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the `as` keyword to assign an alias.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# The conventional aliases are `np` for numpy and `pd` for pandas.
# 
# </details>

# ### 1b: Read in the first file
# 
# 1. As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.
# 
# 2. Use the `head()` method on the `top3` dataframe to inspect the first five rows.

# In[84]:


# 1. ### YOUR CODE HERE ###
top3 = pd.read_csv('epa_ca_tx_pa.csv')
print(top3)
# 2. ### YOUR CODE HERE ###
df = pd.DataFrame(top3)
print(df.head())


# <details>
#   <summary><h4><strong>Hint</strong></h4></summary>
# 
# Because the file is already in your working directory, you can simply pass the file name to the `pd.read_csv()` function as a string.
# 
# </details>

# ## Task 2: Summary information
# 
# Now that you have a dataframe with the AQI data for California, Texas, and Pennsylvania, get some high-level summary information about it.

# ### 2a: Metadata
# 
# Use a DataFrame method to examine the number of rows and columns, the column names, the data type contained in each column, the number of non-null values in each column, and the amount of memory the dataframe uses.

# In[47]:


### YOUR CODE HERE ###
df.info()


# <details>
#   <summary><h4><strong>Hint</strong></h4></summary>
# 
# The `info()` method returns a dataframe's metadata.
# 
# </details>

# ### 2b: Summary statistics
# 
# Examine the summary statistics of the dataframe's numeric columns. The output should be a table that includes row count, mean, standard deviation, min, max, and quartile values.

# In[48]:


### YOUR CODE HERE ###
df[['state_code','county_code']].describe()


# <details>
#   <summary><h4><strong>Hint</strong></h4></summary>
# 
# The `describe()` method returns a table of summary statistics for a dataframe's numeric columns.
# 
# </details>

# ## Task 3: Explore your data
# 
# Practice exploring your data by completing the following exercises.

# ### 3a: Rows per state
# 
# Select the `state_name` column and use the `value_counts()` method on it to check how many rows there are for each state in the dataframe.

# In[49]:


### YOUR CODE HERE ##
df['state_name'].value_counts()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# This code should all be on a single line. Begin by selecting the `top3` dataframe at the `state_name` column. You can use either selector brackets or dot notation.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# When using brackets to select a column, the column's name should be entered as a string.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# The `value_counts()` method is added to the end of the selection statement using dot notation. Its parentheses are empty.
# 
# </details>

# ### 3b: Sort by AQI
# 
# 1.  Create a new dataframe called `top3_sorted` by using the `sort_values()` method on the `top3` dataframe. Refer to the [sort_values pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#) for more information about how to use this method.
#     *  The new dataframe should contain the data sorted by AQI, beginning with the rows with the highest AQI values.
# 2.  Print the top 10 rows of `top3_sorted`.

# In[50]:


# 1. ### YOUR CODE HERE ###
top3_sorted = df.sort_values(by='aqi', ascending = False)

print(top3_sorted)
# 2. ### YOUR CODE HERE ###


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Attach the `sort_values()` method to the `top3` dataframe using dot notation.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# *  The `by` argument of the `sort_values()` method should be a string of the column you want to sort by.
# 
# *  The default behavior of the `sort_values()` method is to sort in ascending order. You want to sort in *descending* order. Which keyword argument modifies this behavior? Refer to the [sort_values() pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# *  Use the `head()` method on the `top3_sorted` dataframe.
# 
# *  The default behavior of the `head()` method is to print the first five rows of a dataframe. You want to print the first 10 rows. Refer to the [head() pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) for more information on how to modify this behavior.
# 
# 
# </details>

# ### 3c: Use `iloc` to select rows
# 
# Use `iloc` to select the two rows at indices 10 and 11 of the `top3_sorted` dataframe.

# In[51]:


### YOUR CODE HERE ###
df.iloc[10:12]


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# To use `iloc` on the `top3_sorted` dataframe, use dot notation.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# `iloc` uses brackets to index data.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# `iloc` index ranges are separated by a colon. Remember, the end index is not included in the range of returned indices.
# 
# </details>

# ## Task 4: Examine California data
# 
# You notice that the rows with the highest AQI represent data from California, so you want to examine the data for just the state of California.

# ### 4a: Basic Boolean masking
# 
# 1. Create a Boolean mask that selects only the observations of the `top3_sorted` dataframe that are from California.
# 2. Apply the Boolean mask to the `top3_sorted` dataframe and assign the result to a variable called `ca_df`.
# 3. Print the first five rows of `ca_df`.

# In[57]:


# 1. ### YOUR CODE HERE ###
ca_df = top3_sorted[top3_sorted['state_name']=='California']

# 2. ### YOUR CODE HERE ###


# 3. ### YOUR CODE HERE ###
print(ca_df)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to what you've learned about Boolean masking.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Define a `mask` variable that is the `top3_sorted` dataframe selected where the `state_name` column is `California`.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# *  Apply the `mask` variable to the `top3_sorted` dataframe and assign the result to a new dataframe called `ca_df`.
# 
# *  Use the `head()` method on the new `ca_df` dataframe.
# </details>

# ### 4b: Validate CA data
# 
# Inspect the shape of your new `ca_df` dataframe. Does its row count match the number of California rows determined in Task 3a?

# In[58]:


### YOUR CODE HERE ###
ca_df.info()
print('Yes')


# <details>
#   <summary><h4><strong>Hint</strong></h4></summary>
# 
# *   Use the `shape` attribute on the `ca_df` dataframe.
# 
# *   Attributes don't use parentheses.
# 
# 
# </details>

# ### 4c: Rows per CA county
# 
# Examine a list of the number of times each county is represented in the California data.

# In[32]:


### YOUR CODE HERE ###
ca_df.info()


# <details>
#   <summary><h4><strong>Hint</strong></h4></summary>
# 
# Select the `county_name` column of `ca_df` and apply the `value_counts()` method to it using dot notation.
# 
# </details>

# ### 4d: Calculate mean AQI for Los Angeles county
# 
# You notice that Los Angeles county has more than twice the number of rows of the next-most-represented county in California, and you want to learn more about it.
# 
# *  Calculate the mean AQI for LA county.

# In[62]:


### YOUR CODE HERE ###
ca_df = ca_df[ca_df['county_name']=='Los Angeles']
mean = np.mean(ca_df['aqi'])

mean


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Use Boolean masking to create a mask. Then apply the mask to the `ca_df` dataframe, select the `aqi` column of the result, and calculate its mean.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# The Boolean mask is `ca_df` selected where `county_name` is `Los Angeles`.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# *  Apply the Boolean mask to `ca_df`.
# *  Then use selector brackets to select the `aqi` column.
# *  Then use dot notation to attach the `mean()` method to the end of the expression.
# 
# </details>

# ## Task 5: Groupby
# 
# Group the original dataframe (`top3`) by state and calculate the mean AQI for each state.

# In[71]:


### YOUR CODE HERE ###
new_top3 =top3.groupby('state_name')
new_top3.mean()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Use the `groupby()` method on the `top3` dataframe.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Group by `state_name` and use dot notation to chain the `mean()` method to the expression.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# `top3.groupby('state_name').mean()` will produce a table of the mean values of every numeric column for each state. To filter the table on just the `aqi` column, add `['aqi']` to the end of the expression.
# 
# </details>

# ## Task 6: Add more data
# 
# Now that you have performed a short examination of the file with AQI data for California, Texas, and Pennsylvania, you want to add more data from your second file.

# ### 6a: Read in the second file
# 
# 1. Read in the data for the remaining territories. The file is called `'epa_others.csv'` and is already in your working directory. Assign the resulting dataframe to a variable named `other_states`.
# 
# 2. Use the `head()` method on the `other_states` dataframe to inspect the first five rows.

# In[78]:


# 1. ### YOUR CODE HERE ###
other_states = pd.read_csv('epa_others.csv')


# 2. ### YOUR CODE HERE ###
other_states.head()


# ### 6b: Concatenate the data
# 
# The data from `other_states` is in the same format as the data from `top3`. It has the same columns in the same order.
# 
# 1. Add the data from `other_states` as new rows beneath the data from `top3`. Assign the result to a new dataframe called `combined_df`.
# 
# 2. Verify that the length of `combined_df` is equal to the sum of the lengths of `top3` and `other_states`.

# In[85]:


# 1. ### YOUR CODE HERE ###
conbined_df = pd.concat([other_states,top3])
conbined_df.reset_index(drop=True)
conbined_df

# 2. ### YOUR CODE HERE ###


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Use the `concat()` function. For more information on this function, refer to the [concat() pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.concat.html).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# *  Enter the two dataframes being joined as a list in the argument field of the `concat()` function.
# 
# *  To add rows, concatenate along axis 0. To add columns, concatenate along axis 1.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `len()` function in a comparison statement to determine if the length of `combined_df` equals the length of `top3` plus the length of `other_states`.
# 
# </details>

# ## Task 7: Complex Boolean masking
# 
# According to the EPA, AQI values of 51-100 are considered of "Moderate" concern. You've been tasked with examining some data for the state of Washington.
# 
# *  Use Boolean masking to return the rows that represent data from the state of Washington with AQI values of 51+.

# In[87]:


### YOUR CODE HERE ###
washinton_data = conbined_df[conbined_df['state_name']=='Washington']
state_of_51_aqi = washinton_data['aqi']>=50
washinton_data[state_of_51_aqi]


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Create a Boolean mask for `combined_df` with two conditions:
# 
# *   The state is Washington
# *   The AQI is greater than or equal to 51
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Remember to enclose each condition in its own set of parentheses.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Separate the two conditions with the `&` operator, because both conditions need to evaluate as true for the row to be included in the filtered dataframe.
# 
# </details>

# # Conclusion
# 
# **What are your key takeaways from this lab?**

# [Double-click here to record your response.]

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged. 
