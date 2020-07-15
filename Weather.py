import tkinter as tk
from tkinter import font
import requests

# def test_function(entry):
#     print("This is the entry",entry)

root = tk.Tk()
# 4accb5545d7a120e48ca2a392dea53c9
# api.openweathermap.org/data/2.5/forecast?q={city name},{state},{country code}&appid={your api key}
def format_response(weather):
    try:
        name=weather['name']
        description =weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str= 'City: %s \nConditions: %s \nTemperature(Celsius): %s' %(name,description,temp)
    except:
        final_str = "There was a problem"

    finally:return final_str

def get_weather(city):
    weather_key = '4accb5545d7a120e48ca2a392dea53c9'
    url ='https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key, 'q':city,'units':'metric'}
    response = requests.get(url, params=params)
    # print(response.json())
    weather=response.json()
    label['text']=format_response(weather)

    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])

canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

background_image = tk.PhotoImage(file='bgpic.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0, relwidth=1,relheight=1)

frame = tk.Frame(root, bg ='#AFF8DB',bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=("Bahnschrift SemiBold",15))
entry.place( relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Weather", bg='#DBFFD6', font=("Bahnschrift SemiBold",10), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#AFF8DB', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6,anchor='n')

label = tk.Label(lower_frame, font=("Bahnschrift SemiBold",15) )
label.place(relwidth=1, relheight=1)


# print(tk.font.families())

root.mainloop()