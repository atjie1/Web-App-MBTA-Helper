# Project 3: MBTA-Helper
Web App Designed and Developed by Abby Tjie

**Project Overview**
   
   MBTA-Helper is a simple webapp created using Flask that prompts the user to enter a location within the Boston area as a text input. When the form is submitted, the output uses the Mapbox API and MBTA API to return the nearest MBTA train stop and whether the stop is wheelchair accessible. Additional features include a link to see the location of the MBTA train stop in Google Maps and even open Google Maps through the display. Background lofi music plays using the pygame python module while the webapp is running.

**Reflection**

***The Process + Obstacles***

My favorite aspect of creating this project was calling the API's. I finally feel that all the practice with obtaining keys, reading documentation, and calling API data is all starting to make sense. However, I did face a few obstacles:
1. After I had received my MapBox API token, I attempted to use the MapBox URL, but I kept receiving a "bad request" error. Once I requested a new MapBox token, the URL began to work.
   
2. I was stuck (for a long time) wondering why exactly I could not obtain the stop output although I was able to identify the coordinates. After staring (for too much time), I was able to figure out (without help, might I add...) that the coordinates list longitude then latitude in the dataset (latitude comes first when considering a coordinate on earth)! Here you can see my fix when I identified this:
   
mbta-helper.py  lines 29-33
   
    response_data = get_json(url)
    longitude, latitude = response_data["features"][0]["center"]  
    # coordinates are longitude then latitude
    return latitude, longitude

1. Another important obstacle I faced was that I was using the class exercise Flask port in this project "overwriting" the existing port. I created a new port routed to "3640".

2. My greatest  mistake was capitalizing the variable name "Location" when attempting to get the "location" input into my results HTML file. I kept receiving AttributeErrors, NoneTypeErrors, and MethodErrors that led me to think that my function was not returning a string, but a None type. However, my professor was able to identify one of my biggest mistakes.

I received more than a spark of joy when I was able to call the data in an HTML form in my Flask development webapp!

***Failed Attempts***

I attempted so many times to create and link a CSS style file, but after watching a YouTube video, consulting ChatGPT, and websites, everything that the examples were showing, I did exactly that, but still could not link a CSS file to store my style in.

I wanted to implement background music into the webapp, specifically "Hey, Jude" on loop. I consulted ChatGPT and the internet, and looked through API documentation for Spotify. Unfortunately, the Spotify API had data on artists and their music, not the specific song note data (which is what I needed). By asking ChatGPT to code the melody of "Hey, Jude", I could use pygame to play musical notes, but I needed .wav documents of each note on the piano. Ultimately, I was not able to write a code to create the frequencies of each note and store them. 

**Future Improvements**

If I was given more time, I feel like I would be able to implement the "Hey, Jude" piano instrumental as background music. Some additional features I have thought about was a validating feature to give feedback to the user if a location not in Boston is entered. Currently, it will give an IndexError. The Google Map also only shows the approximate coordinates of the nearby stop, not the true location that Google Maps has marked. The output of train arrival time would have been a great supplemental inclusion as well!

***Proud Moment***
1. I was able to play lofi music by downloading a free MP3 track, converting it to a .wav file and using pygame to play it when my webapp is running!
2. ChatGPT was able to help me with HTML style, which I really think looks great!

![image]:\Users\atjie1\Downloads\Web-App-MBTA-Helper\images\Final Form - MBTA-app.PNG

![image]:C:\Users\atjie1\Downloads\Web-App-MBTA-Helper\images\Final Form - MBTA-app.PNG

***Learnings***
I was able to learn about Flask and its ability to develop a webpage to present and apply an API. Moving foward, I will be using APIs in my final OIM project and potentially Flask. ChatGPT was a big help in assisting in formatting style in HTML, a topic that is not covered or practiced in this specific course. Before I had started this project, I wish I knew how to manipulate the style of a webpage (Web Tech would have been helpful!).
