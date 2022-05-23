from email import message
import json
import time
import urllib.request
import smtplib, ssl

API="9WpEIDIaYfNKHJvGAT9kC1XF1Rzbwhge"
CountryCode="IN"
City="Bengaluru"
date=""
Key ="204108"
data={}
#def getLocationKey(CountryCode,City):
#    searchaddress="http://dataservice.accuweather.com/locations/v1/cities/"+CountryCode+"/search?apikey="+API+"&q="+City+"&details=true"
#    with urllib.request.urlopen(searchaddress) as search_address:
#        data = json.loads(search_address.read().decode())
#    location_key = data[0]['Key']
#    return (location_key)

def getForcast(location_key):
    daily_Forecast_Url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+location_key+"?apikey="+API+"&details=true&metric=true"
    with urllib.request.urlopen(daily_Forecast_Url) as daily_Forecast_Url:
        data = json.loads(daily_Forecast_Url.read().decode())
    for key1 in data['DailyForecasts']:
        date = key1['Date']
        min_Temperature=str(key1['Temperature']['Minimum']['Value'])
        max_Temperature = str(key1['Temperature']['Maximum']['Value'])
        air_Quality=str(key1['AirAndPollen'][0]['Category'])
        uv_Index = str(key1['AirAndPollen'][5]['Category'])
        day_Forecast = str(key1['Day']['LongPhrase'])
        wind_Speed = str(key1['Day']['Wind']['Speed']['Value'])
        wind_Gustspeed = str(key1['Day']['WindGust']['Speed']['Value'])  
    return date,min_Temperature,max_Temperature,air_Quality,uv_Index,day_Forecast,wind_Speed,wind_Gustspeed

date,min_Temperature,max_Temperature,air_Quality,uv_Index,day_Forecast,wind_Speed,wind_Gustspeed=getForcast(Key)

Message = "Weather forecast for Bengaluru on "+date
Message+= "\n Minimum Temperature(Celsius) is "+min_Temperature
Message+= "\n Maximum Temperature(Celsius) is "+max_Temperature
Message+="\n Air Quality is "+air_Quality
Message+="\n Uv Index is "+ uv_Index
Message+="\n Day Forecast is "+day_Forecast
Message+="\n Wind Speed is "+wind_Speed +" KMPH"
Message+="\n wind Gust Speed is "+wind_Gustspeed +" KMPH"


print(Message)
print("**********************************************")
print("**********************************************")
print("\n")
print("\n")
print("\n")

gmail_user = 'sreekanthc0298@gmail.com'
gmail_password = 'Sree_cvA309'

sent_from = gmail_user
to = ['csrikanthreddy002@gmail.com','Sumanjit.Saha@dell.com','Sreekanth.Reddy2@dell.com']   
subject = 'Weather forecast for the day'
body = Message

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)
