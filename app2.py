import tkinter as tk
from pymongo import MongoClient
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['football']
collection = db['goals_per_season']

# Retrieve data from MongoDB for the 2016/2017 season
season_data = collection.find({'season': '2016/2017'})

# Extract leagues and goals from the retrieved data
leagues = []
goals = []
for data in season_data:
    leagues.append(data['league'])
    goals.append(data['total_goals'])

# Create the Tkinter app
root = tk.Tk()
root.title('Football Goals by League (2016/2017)')

# Create a figure and axes for the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Create the bar plot
ax.bar(leagues, goals)
ax.set_xlabel('League')
ax.set_ylabel('Number of Goals')
ax.set_title('Football Goals by League (2016/2017)')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Create a canvas for displaying the plot
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# Pack the canvas into the Tkinter app
canvas.get_tk_widget().pack()

# Run the Tkinter event loop
root.mainloop()