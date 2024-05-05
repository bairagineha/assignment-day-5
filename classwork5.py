#!/usr/bin/env python
# coding: utf-8

# # classwork5 

# In[19]:


import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the URL in the browser
driver.get("https://www.flipkart.com/laptops/pr?sid=6bo,b5g")

# Wait for the page to load
time.sleep(5)  # You might need to adjust this time depending on your internet speed

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Define classes for names, prices, and ratings
names = "_4rR01T"
prices = "_30jeq3 _1_WHN1"
rating = "_3LWZlK"

# Find elements with specified classes
laptop_names_div = soup.find_all(class_=names)
laptop_prices_div = soup.find_all(class_=prices)
laptop_rating_div = soup.find_all(class_=rating)

# Extract text from found elements and store in lists
laptop_names = []
for i in laptop_names_div:
    laptop_names.append(i.text)

laptop_prices = []
for i in laptop_prices_div:
    laptop_prices.append(i.text)

laptop_ratings = []
for i in laptop_rating_div:
    laptop_ratings.append(i.text)
    
print(laptop_names)
print(laptop_prices)
print(laptop_ratings)


# Close the WebDriver
driver.quit()

# Zip the lists to combine them into a list of tuples
data = zip(laptop_names, laptop_prices, laptop_ratings)

# Define the output CSV file path
output_file = "laptops_data.csv"

# Write the data to the CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write header row
    writer.writerow(["Name", "Price", "Rating"])
    # Write data rows
    writer.writerows(data)

print("Data has been saved to", output_file)


# # homework5

# In[18]:


from bs4 import BeautifulSoup 
from selenium import webdriver
import csv 
import time 

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the URL in the browser
driver.get("https://www.naukri.com/data-science-jobs?src=discovery_trendingWdgt_homepage_srch")

# Wait for the page to load (adjust the time based on your internet speed)
time.sleep(5)

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Define class for job data
job_class = "cust-job-tuple layout-wrapper lay-2 sjw__tuple"

# Find elements with specified class
job_data_div = soup.find_all(class_=job_class)

# Extract text from found elements and store in a list
job_data = []
for i in job_data_div:
    job_data.append(i.text)

# Define the output CSV file path
output_file = "job_data.csv"

# Write the data to the CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write data rows
    for data in job_data:
        writer.writerow([data])

# Print message after data is saved
print(output_file)

# Close the WebDriver
driver.quit()


# In[ ]:




