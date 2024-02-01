#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium


# In[2]:


pip install selenium webdriver-manager


# ### OPENING YOU TUBE VIDEO IN FIREFOX USING URL
# 
# 1. Import necessary modules
# 2. Set up browser options
# 3. Initialize the WebDriver
# 4. Set an implicit wait

# In[4]:


#https://youtu.be/uqsvyj6lnnE?si=Cqg6ijKSv5cnfDSo
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
option = Options()
option.headless = False
driver = webdriver.Firefox(options=option)
driver.implicitly_wait(5)

# Specify the ChromeDriver version explicitly
url=input("Enter the You Tube link: ")
driver.get(url)


# ### OPENING YOU TUBE IN FIREFOX USING SEARCH KEYWORD
# 
# 1. Import necessary modules:
# 2. Set up the browser options:
# 3. Initialize the WebDriver:
# 4. Set an implicit wait:
# 5. Define the base URL and ask the user for a keyword:
# 6. Navigate to the YouTube search results page with the entered keyword:
# 7. One can add further actions to interact with the search results page or scrape data as needed. 

# In[3]:


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import json


# In[6]:


option = Options()
option.headless = False
driver = webdriver.Firefox(options=option)
driver.implicitly_wait(5)
baseUrl = "https://youtube.com/"
keyword = input("Enter the keyword you want to search:")
driver.get(f"{baseUrl}/search?q={keyword}")


# ### OPENING YOU TUBE PAGE IN CHROME
# 1. Set up the Chrome WebDriver, specifying whether you want to run it in headless mode .
# 2. Initialize the WebDriver and navigate to the YouTube homepage.
# 3. Used Selenium to search for a video by entering a query in the search box and pressing Enter.
# 4. Click on the first video in the search results.
# 5. Wait for a few seconds .
# 6. Performing additional actions, such as extracting comments or interacting with the video player.

# In[7]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.headless = False


# In[8]:


driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://youtube.com/")


# ### SCRAPING LIKES 
# 
# 1. Import necessary modules
# 2. Initialize the Chrome WebDriver
# 3. Input the URL of the YouTube video
# 4. Wait for the page to load completely (we may need to adjust the wait time)
# 5. Scroll down to load additional video details (optional)
# 6. Locate the "Like" and "Dislike" buttons - as per update in September 2021, YouTube does not provide the number of dislikes on a video through its public API or directly in the video player interface so the number of dislikes is not displayed
# 7. Extract the likes 
# 8. Print the total number of likes 

# In[166]:


#https://www.youtube.com/live/_IcgGYZTXQw?si=SwO8a7YozPXwY0kO
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = input("Enter the URL: ")
driver.get(url)

# Locate all the search result elements
results = driver.find_elements(By.ID, "actions")

# Initialize empty lists to store likes and dislikes
likes = []
#dislikes = []

# Iterate through the results
for result in results:
    # Find the like button within each result
    like_button = result.find_element(By.ID, "segmented-like-button")
    
    # Find the dislike button within each result
    #dislike_button = result.find_element(By.ID, "segmented-dislike-button")
    
    # Get the text from the like button
    like_text = like_button.text
    
    # Get the text from the dislike button
    #dislike_text = dislike_button.text
    
    # Append the text to the respective lists
    likes.append(like_text)
    #dislikes.append(dislike_text)

# Print the likes and dislikes
print("Likes:", likes)
#print("Dislikes:", dislikes)


# ### EXTRACTING CHANNEL DETAILS
# 1. Import necessary modules
# 2. Initialize the Chrome WebDriver
# 3. Input the channel name
# 4. Navigate to the YouTube search results for the channel name
# 5. Locate the channel information section
# 6. Extract the channel name, subscriber count, and description
# 7. Print the extracted information

# In[10]:


from selenium import webdriver
from selenium.webdriver.common.by import By


# In[11]:


driver= webdriver.Chrome()


# In[12]:


channelname = input("Enter channel name: ")
driver.get(f"https://www.youtube.com/results?search_query={channelname}")


# In[13]:


channelname_info = driver.find_elements(By.CSS_SELECTOR, '[id="info"]')
channelname= driver.find_element(By.ID,"info-section")
name_text = channelname.find_element(By.ID,"channel-title").text
name_text1 = channelname.find_element(By.ID,"metadata").text
name_text2 = channelname.find_element(By.ID,"description").text


# In[14]:


print("Channel text\t: " + name_text)
print("Suscriber count\t: " + name_text1)
print("Channel Description\t: " + name_text2)


# ### EXTRACTING SEARCH DETAILS USING KEYWORD
# 1. Import necessary modules
# 2. Initialize the Chrome WebDriver
# 3. Input the search keyword
# 4. Navigate to the YouTube search page with the desired 
# 5. Locate all the search result elements
# 6. Iterate through the search results
# 7. Find elements within each search result
# 8. Extract text from elements
# 9. Print the extracted information
# 10. Handle any exceptions if an element is missing or cannot be located

# In[159]:


from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
search_keyword = input("Enter your search keyword:")
search_url = f"https://www.youtube.com/results?search_query={search_keyword}"
driver.get(search_url)

# Locate all the search result elements
search_results = driver.find_elements(By.ID, "dismissible")
# Iterate through the search results
for result in search_results:
    try:
        # Find elements within each search result
        channelname= result.find_element(By.ID,"channel-info").text
        metadata = result.find_element(By.ID,"metadata-line").text
        title = result.find_element(By.ID, "video-title").text
        print("Title:", title)
        print("Channel Name:", channelname)
        print("Metadata:", metadata)
        print("--"*50)     
    except:
        # Handle any exceptions if an element is missing or cannot be located
        print("An error occurred while extracting information from a search result.")


# ### EXTRACTING SEARCH DETAILS AND STORING IT IN DATAFRAME
# 1. Import necessary modules
# 2. Initialize the Chrome WebDriver
# 3. Input the search keyword
# 4. Navigate to the YouTube search page with the desired keyword
# 5. Create an empty DataFrame to store the results
# 6. Locate all the search result elements
# 7. Iterate through the search results
# 8. Find elements within each search result
# 9. Extract text from elements
# 10. Append the extracted information to the DataFrame
# 11. Handle any exceptions if an element is missing or cannot be located
# 12. Display the DataFrame

# In[165]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings

# Assuming you have already created a WebDriver instance, let's call it 'driver'
driver= webdriver.Chrome()
# Navigate to the YouTube search page with your desired keyword
search_keyword = input("Enter your search keyword:")
search_url = f"https://www.youtube.com/results?search_query={search_keyword}"
driver.get(search_url)

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)

    df = pd.DataFrame(columns=["Title", "Channel Name", "Metadata"])

    # Locate all the search result elements
    search_results = driver.find_elements(By.ID, "dismissible")
    # Iterate through the search results
    for result in search_results:
        try:
            # Find elements within each search result
            channelname= result.find_element(By.ID,"channel-info").text
            metadata = result.find_element(By.ID,"metadata-line").text
            title = result.find_element(By.ID, "video-title").text
            df = df.append({"Title": title, "Channel Name": channelname, "Metadata": metadata}, ignore_index=True)

        except:
            # Handle any exceptions if an element is missing or cannot be located
            print("An error occurred while extracting information from a search result.")

df


# ### EXTRACT COMMENTS  ON A TIME FRAME SPECIFIED BY THE USER.

# In[139]:


#https://youtu.be/i8ljZYzn0Uc?si=0C8L84orzpRJExHw 
#The race for artificial intelligence - Can Europe compete? | DW Documentary
driver= webdriver.Chrome()
url = input("Enter the URL: ")
driver.get(url)


# In[156]:


from datetime import datetime, timedelta
ctime = input("Enter the time(in days/weeks/months ago):")
parts1 = ctime.split()
numeric_value1 = int(parts1[0])
text1 = " ".join(parts1[1:])
comments = driver.find_elements(By.ID,"main")
for comment in comments:
    comment_date_str = comment.find_element(By.TAG_NAME, "yt-formatted-string").text
    parts2 = comment_date_str.split()
    numeric_value2 = int(parts2[0])
    text2 = " ".join(parts2[1:])
    if numeric_value1 == numeric_value2 and text1 == text2:
        comment_text = comment.find_element(By.ID, 'comment-content').text
        print("comment text: " + comment_text)


# ### OPENING YOUTUBE VIDEO IN JUPYTER
# 1. Import the necessary library:
# 2. Get the YouTube video URL from the user:
# 3. Extract the video ID from the URL. You can do this by splitting the URL using "v=" 
#     as a delimiter and taking the second part:
# 4. Create and display the YouTube video using the `YouTubeVideo` class:

# In[122]:


pip install ipython


# In[2]:


#https://www.youtube.com/watch?v=csXmVBw8cdo: Science of Data Visualization
from IPython.display import YouTubeVideo

# Get the YouTube video URL from the user
video_url = input("Enter the YouTube video URL: ")

# Extract the video ID from the URL
video_id = video_url.split("v=")[1]

# Create and display the YouTube video
YouTubeVideo(video_id)


# ### CONCLUSION 

# Web scraping YouTube can provide a wealth of data that can be used for various analyses and insights. Here are some common analyses:
# 
# **Content Analysis:**
# 
# *Video Titles and Descriptions:* Analyzing keywords, trends, and patterns in video titles and descriptions.
# 
# *Video Categories:* Categorizing videos based on content tags or categories.
# 
# *Thumbnails:* Analyzing the visual elements of video thumbnails to identify common themes.
# 
# **Popularity and Engagement Analysis:**
# 
# *View Counts:* Tracking view counts over time to identify trending videos.
# 
# *Likes and Dislikes:* Analyzing the likes & dislikes as a measure of video reception.
# 
# *Comments:* Studying the volume and sentiment of user comments to understand audience engagement.
# 
# **Channel Analysis:**
# 
# *Subscriber Counts:* Tracking channel growth and identifying popular channels.
# 
# *Video Upload Frequency:* Analyzing how often a channel uploads new content.
# 
# *Channel Categories:* Categorizing channels based on their content niche.
# 
# **User Behavior Analysis:**
# 
# *User Comments:* Analyzing user-generated comments for sentiment analysis, trending topics, or user interactions.
# 
# *User Interaction Patterns:* Identifying how users engage with videos (e.g., likes, shares, subscribes).
# 

# In[ ]:




