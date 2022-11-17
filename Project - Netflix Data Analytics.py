#!/usr/bin/env python
# coding: utf-8

# ### The Netflix dataset has information about TV Shows and Movies available on Netflix till 2021.

# In[1]:


import pandas as pd                         #to import pandas library


# In[2]:


# Importing the dataset
data= pd.read_csv(r"C:\Users\shrik\Downloads\Netflix Dataset.csv")
print(data)


# ### Getting some basic information about the dataset 

# #### 1. head()

# In[3]:


data.head()                                   #to show top-5 records of the dataset


# #### 2. tail()

# In[4]:


data.tail()                                    #to show bottom-5 records of the dataset 


# #### 3. Shape

# In[5]:


data.shape                                     #to show the No. of Rows and Columns


# #### 4. Size

# In[6]:


data.size                                     #to show No. of total values(elements) in the dataset


# #### 5. columns

# In[7]:


data.columns                                #to show column Name


# #### 7. dtypes

# In[8]:


data.dtypes                                #to show the data-type of each column


# #### 8. info()

# In[9]:


data.info()                              #to show indexes, columns, data-types of each column, memory at once


# ### Task.1. Is there any Duplicate Record in this dataset? If yes, then remove the duplicate records.

# #### duplicate()

# In[10]:


data.head()


# In[11]:


data.shape


# In[12]:


data[data.duplicated()]                        #to check row wise and detect the Duplicate rows


# In[13]:


data.drop_duplicates(inplace = True)          #to Remove the Duplicate rows permanently


# In[14]:


data[data.duplicated()]     


# In[15]:


data.shape


# ### Task.2. Is there any Null Value present in any column? Show with the Heat-map.

# #### isnull()

# In[16]:


data.head()


# In[17]:


data.isnull()                     # To show where Null value is present


# In[18]:


data.isnull().sum()              #to show the count of Null values in each column


# #### Seaborn library(heat-map)

# In[19]:


import seaborn as sns                     #to import Seaborn library


# In[20]:


sns.heatmap(data.isnull())                  #using heat-map to show null values count


# ### Q.1. For "House of Cards", what is the Show id and who is the Director of this show ?

# #### isin()

# In[21]:



data.head()


# In[22]:


data[data['Title'].isin(['House of Cards'])]               #to show all records of a particular item in any column


# #### str.contains()

# In[23]:


data[data['Title'].str.contains('House of Cards')]          #to show all records of a particular string in any column


#  ### Q.2. In which year highest number of the TV Shows & Movies were released? Show with Bar Graph.

# #### dtypes

# In[24]:


data.dtypes


# #### to_datetime

# In[25]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[26]:


data.head()


# In[27]:


data.dtypes


# #### dt.year.value_counts()

# In[28]:


data['Date_N'].dt.year.value_counts()                     #It counts the occurence of all individual Year in Date column.


# #### Bar Graph

# In[29]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# ### Q.3. How many Movies and TV Shows are in the dataset? Show with Bar Graph

# In[30]:


data.head(2)


# #### groupby()

# In[31]:


data.groupby('Category').Category.count()                   #to group all unique items of a column and show their counts


# #### countplot()

# In[32]:


sns.countplot(data['Category'])


# ### Q.4. Show all the Movies that were released in year 2000.

# #### creating new column

# In[33]:


data.head(2)


# In[34]:


data['Year'] = data['Date_N'].dt.year           # to create new Year column ; it will consider only year


# In[35]:


data.head(2)


# #### Filtering

# In[36]:


data[(data['Category'] == 'Movie') & (data['Year'] == 2000)]


# In[37]:


data[(data['Category'] == 'Movie') & (data['Year']==2020)]


# ### Q.5. Show only the Titles of all TV Shows that were released in India

# #### Filtering

# In[38]:


data.head(2)


# In[39]:


data[(data['Category']=='TV Show') & (data['Country']=='India')] ['Title']


# ### Q.6. Show Top 10 Directors, who gave the highest number of TV Shows and Movies to Netflix ?

# #### value_counts()

# In[40]:


data.head(2)


# In[41]:


data['Director'].value_counts().head(10)


# ### Q.7. Show all the Records, where "Category is Movies and type is Comedies" or "Country is United Kingdom"

# #### Filtering (And, Or Operators)

# In[42]:


data.head(2)


# In[43]:


data[(data['Category'] == 'Movie') & (data['Type'] == 'Comedies')]


# In[44]:


data[(data['Category'] == 'Movie') & (data['Type'] == 'Comedies') | (data['Country'] == 'United Kingdom')]


# ### Q.8. In how many Movies/TV Shows, Tom Cruise was cast

# In[45]:


data.head(2)


# #### filtering

# In[46]:


data[data['Cast'] == 'Tom Cruise']


# #### str.contains()

# In[47]:


data[data['Cast'].str.contains('Tom Cruise')]


# #### Creating new data-frame

# In[48]:


data_new = data.dropna()                                   #It drops the row that contains all or any missing values.


# In[49]:


data_new.head(2)


# In[50]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# ### Q.9. What are the different Ratings defined by Netflix?

# In[51]:


data.head(2)


# In[52]:


data['Rating'].nunique()                              # it shows how many different unique values are present in the column


# In[53]:


data['Rating'].unique()


# #### Q.9.1 How many Movies got the 'TV-14' rating, in Canada?

# In[54]:


data.head(2)


# In[55]:


data[(data['Category'] == 'Movie') & (data['Rating'] == 'TV-14')].shape


# In[56]:


data[(data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') & (data['Country'] == 'Canada')]


# In[57]:


data[(data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') & (data['Country'] == 'Canada')].shape


# #### Q.9.2. How many TV Show got the 'R' rating, after year 2018?

# In[58]:


data.head(2)


# In[59]:


data[(data['Category'] == 'TV Show') & (data['Rating'] == 'R')]


# In[60]:


data[(data['Category'] == 'TV Show') & (data['Rating'] == 'R') & (data['Year'] > 2018)]


# ### Q.10. What is the maximum duration of a movie/show on Netflix ?

# In[61]:


data.head(2)


# In[62]:


data['Duration'].unique()


# In[63]:


data['Duration'].dtype


# ### str.split()

# In[64]:


data.head(2)


# In[66]:


data[['Minutes' , 'Unit']] = data['Duration'].str.split(' ' , expand = True)


# In[67]:


data.head(2)


# #### max()

# In[74]:


data['Minutes'].max()


# In[76]:


data['Minutes'].min()


# ### Q.11. Which individual country has the Highest No. of TV Shows ?

# In[77]:


data.head(2)


# In[78]:


data_tvshow = data[data['Category'] == 'TV Show']


# In[79]:


data_tvshow.head(2)


# In[80]:


data_tvshow.Country.value_counts()


# In[82]:


data_tvshow.Country.value_counts().head(1)


# ### Q.12. How can we sort the dataset by Year ?

# In[83]:


data.head(2)


# In[84]:


data.sort_values(by = 'Year')


# In[86]:


data.sort_values(by = 'Year' , ascending = False)


# ### Q.13. Find all the instances where:

# ### Category is 'Movie' and Type is 'Dramas'

# ### or

# ### Category is 'TV Show' and Type is 'Kids TV'

# In[87]:


data.head(2)


# In[89]:


data[(data['Category'] == 'Movie') & (data['Type'] == 'Dramas')]


# In[92]:


data[(data['Category'] == 'TV Show') & (data['Type'] == "Kids' TV")]


# In[93]:


data [(data['Category'] == 'Movie') & (data['Type'] == 'Dramas') | (data['Category'] == 'TV Show') & (data['Type'] == "Kids' TV")]

