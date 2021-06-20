#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[1]:


import requests


# In[ ]:





# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: This sure seems familiar.*

# In[2]:


api_key = 'xxxx'


# In[3]:


url = "http://api.weatherapi.com/v1/forecast.json?key=" + api_key + "&q=london/current.json"

response = requests.get(url)
data = response.json()


# In[4]:


data


# ## 2) What's the current wind speed, and how much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference. Same as we did last time!*

# In[5]:


data['current']['wind_mph']


# In[6]:


temp_diff = data['current']['temp_c'] - data['current']['feelslike_c']
temp_diff


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible on next Thursday?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[18]:


https://api.weatherapi.com/v1/astronomy.json?key=[key]&q=london


# In[35]:


url_astro = "https://api.weatherapi.com/v1/forecast.json?key=" + api_key + "&q=london&dt=2021-06-24"

response_astro = requests.get(url_astro)
data_astro = response_astro.json()

data_astro


# In[39]:


for i in data_astro['forecast']['forecastday']:
    print(i['date'] + ': ' + i['astro']['moon_phase'])


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[67]:


url_temp = "https://api.weatherapi.com/v1/forecast.json?key=" + api_key + "&q=london&dt=2021-06-20"

response_temp = requests.get(url_temp)
data_temp = response_temp.json()

data_temp


# In[68]:


for i in data_temp['forecast']['forecastday']:
    print(f"The difference between high and low temps is {i['day']['maxtemp_c'] - i['day']['mintemp_c']}")


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# ###### Need to change the variables for url, response and data_temp
# 
# ###### I rename them by adding a '_' and more info

# ## 5) Go through the daily forecasts, printing out the next week's worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[50]:


url_week = "https://api.weatherapi.com/v1/forecast.json?key=" + api_key + "&q=london&dt="


# In[52]:


dates = ["2021-06-21", "2021-06-22", "2021-06-23", "2021-06-24", "2021-06-25", "2021-06-26", "2021-06-27"]


# In[76]:


for date in range(len(dates)):
    url_week = "https://api.weatherapi.com/v1/forecast.json?key=" + api_key + "&q=london&dt=" + dates[date]
    response_week = requests.get(url_week)
    data_week = response_week.json()
    
    for x in data_week['forecast']['forecastday']:
        if x['day']['avgtemp_c'] <= 13:
            print(f"It's cold on {x['date']}")
        elif 14 < x['day']['avgtemp_c'] < 17 :
            print(f"It's warm on {x['date']}")
        else:
            print(f"It's hot on {x['date']}")


# In[ ]:





# # 6) What will be the hottest day in the next week? What is the high temperature on that day?

# In[82]:


for date in range(len(dates)):
    url_week = "https://api.weatherapi.com/v1/forecast.json?key=" + api_key + "&q=london&dt=" + dates[date]
    response_week = requests.get(url_week)
    data_week = response_week.json()
    
    for x in data_week['forecast']['forecastday']:
        print(f"{x['date']} will be {x['day']['avgtemp_c']}")


# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[107]:


cities = ["miami", "florida"]

for i in range(len(cities)):
    url_24 = "https://api.weatherapi.com/v1/forecast.json?key=" + api_key + "&q=" + cities[i]
    response_24 = requests.get(url_24)
    data_24 = response_24.json()

    for hour in data_24['forecast']['forecastday']:
        for item in hour['hour']:
            if item['cloud'] > 50:
                print(f"in {cities[i]} it's {item['temp_c']} and cloudy")
            else:
                print(f"in {cities[i]} it's {item['temp_c']}")
                
            


# In[ ]:





# # 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[109]:


url_miami = "https://api.weatherapi.com/v1/forecast.json?key=" + api_key + "&q=miami"

response_miami = requests.get(url_miami)
data_miami = response_miami.json()


# In[117]:


over_85 = 0
other = 0

for hour in data_miami['forecast']['forecastday']:
        for item in hour['hour']:
            if item['temp_f'] > 85:
                over_85 += 1
            else:
                other += 1


# In[123]:


print(f"{over_85 / over_85 + other:.0f}% are over 85 degrees ")


# In[ ]:





# ## 9) What was the temperature in Central Park on Christmas Day, 2020? How about 2012? 2007? How far back does the API allow you to go?
# 
# - *Tip: You'll need to use latitude/longitude. You can ask Google where Central Park is, it knows*
# - *Tip: Remember when latitude/longitude might use negative numbers*

# In[130]:


central_park = "40.7812,-73.9665"

url_cp = "https://api.weatherapi.com/v1/history.json?key=" + api_key + "&q=" + central_park + "&dt=2020-12-25"


# In[131]:


response_cp = requests.get(url_cp)
data_cp = response_cp.json()

data_cp


# In[128]:


for i in data_cp['forecast']['forecastday']:
    print(f"The temperature in Central Park on Christmas Day 2020 was {i['day']['temp_c']}")


# In[ ]:





# In[ ]:





# In[ ]:




