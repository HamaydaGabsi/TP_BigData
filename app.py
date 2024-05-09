import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to load data and plot
def plot_data():
    # Initialize canvas if it doesn't exist
    if not hasattr(plot_data, 'canvas'):
        plot_data.canvas = None
    
    # Clear the existing plot
    if plot_data.canvas is not None:
        plot_data.canvas.get_tk_widget().destroy()  # Destroy the existing canvas widget
    
    # Load data
    df = pd.read_csv('total_goals_by_league.csv')
    
    # Filter data by selected league
    selected_league = league_var.get()
    filtered_df = df[df['league'] == selected_league]
    
    # Plot data
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(filtered_df['season'], filtered_df['total_goals'], marker='o')
    ax.set_xlabel('Season')
    ax.set_ylabel('Total Goals')
    ax.set_title(f'Total Goals per Season for {selected_league}')
    
    # Display plot in the GUI
    plot_data.canvas = FigureCanvasTkAgg(fig, master=root)
    plot_data.canvas.draw()
    plot_data.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create the main window
root = tk.Tk()
root.title("League Goals Visualization")

# Create a dropdown menu for league selection
league_var = tk.StringVar(root)
league_var.set('Select a League')  # default value
league_dropdown = ttk.Combobox(root, textvariable=league_var, state='readonly')
league_dropdown['values'] = ('Premier Division', 'Liga I', 'English Football League Two', 'Ligue 1', 'Serie A')  # Add your leagues here
league_dropdown.pack(pady=20)

# Button to generate the plot
generate_button = tk.Button(root, text="Generate Plot", command=plot_data)
generate_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
