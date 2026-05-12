# #1. Data Cleaning -while using this code, I will fill empty rows and columns by using average numbers of table
# import pandas as pd
# df=pd.read_excel('Python-pandas/employees.xlsx')
# df['Experience_Years'] = df['Experience_Years'].fillna(df['Experience_Years'].mean())
# df['Performance_Score'] = df['Performance_Score'].fillna(df['Performance_Score'].mean())
# #print(df)
# print(df.describe())  #describe() -will help you to find the table's max,min,average value




# #2. Data Transformation - "Mark employees with a performance score above 80 as 'High' and 
# # the others as 'Normal' apply  and loc (location) functions
# import pandas as pd
# df=pd.read_excel('Python-pandas/employees.xlsx')
# df.loc[df['Salary'] >= 1400 , 'Level'] = 'Senior'
# df.loc[df['Salary'] <1400 , 'Level'] = 'Middle'
# print(df)
# df.to_excel('Python-pandas/new-employees.xlsx' , index=False)



#3. Date Visualization
#a bar chart showing the number of employees by department
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('Python-pandas/employees.xlsx')
#How many people are there in the department?
count = df['Department'].value_counts()
#print(count) in this point we will see departments' count
# Rendering the distribution of categorical variables as a bar chart.
#count.plot(kind='bar' , color = 'red' , rot=0) #rot helps to see all titles together on the table
#if you want to see bars in the different colors you can add other colors but sometimes its hard to write all of them, therefore we use 
#cmap='viridis' function to automate colors
count.plot(kind = 'bar' , cmap = 'viridis' , rot = 0)
plt.title('The main count of the table')
plt.xlabel('The name of departments')
plt.ylabel('The count of departments')
plt.show()
