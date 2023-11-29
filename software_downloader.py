import tkinter as tk
from tkinter import messagebox
import subprocess
from tkinter import ttk

software_development = [
    ("Visual Studio Code", "Microsoft.VisualStudioCode"),
    ("Python", "Python.Python.3.12"),
    ("Notepad++", "Notepad++.Notepad++"),
    ("Git", "Git.Git"),
    ("Node.js", "OpenJS.NodeJS"),
    # Add more software for Development category as needed
]

software_browsers = [
    ("Google Chrome", "Google.Chrome"),
    ("Mozilla Firefox", "Mozilla.Firefox"),
    ("Microsoft Edge", "Microsoft.Edge"),
    # Add more software for Browsers category as needed
]

software_communication = [
    ("Zoom", "Zoom.Zoom"),
    ("Discord", "Discord.Discord"),
    ("Microsoft Teams", "Microsoft.Teams"),
    ("Skype", "Microsoft.Skype"),
    # Add more software for Communication category as needed
]

software_multimedia = [
    ("Spotify", "Spotify.Spotify"),
    ("VLC media player", "VideoLAN.VLC"),
    # Add more software for Multimedia category as needed
]

software_utilities = [
    ("WinRAR", "RARLab.WinRAR"),
    ("7-Zip", "7zip.7zip"),
    ("Adobe Acrobat Reader", "Adobe.Acrobat.Reader.32-bit"),
    # Add more software for Utilities category as needed
]

software_gaming = [
    ("Steam", "Valve.Steam"),
    # Add more software for Gaming category as needed
]

software_productivity = [
    ("Microsoft Office", "Microsoft.Office"),
    # Add more software for Productivity category as needed
]

software_storage = [
    ("Dropbox", "Dropbox.Dropbox"),
    # Add more software for Storage category as needed
]

# Function to handle software download
def download_selected_software():
    selected_indices = software_checkbox_state()
    if not selected_indices:
        messagebox.showerror("Error", "Please select at least one software to download.")
        return

    for index in selected_indices:
        try:
            software_id = current_category_software[index][1]
            command = f"winget install --id {software_id} -e"
            result = subprocess.run(command, shell=True, capture_output=True)
            if result.returncode == 0:
                messagebox.showinfo("Success", f"Successfully installed {current_category_software[index][0]}!")
            else:
                error_message = result.stderr.decode('utf-8').strip()
                messagebox.showerror("Error", f"Failed to install {current_category_software[index][0]}. Error: {error_message}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install {current_category_software[index][0]}. Error: {str(e)}")

# Function to retrieve selected checkbox indices
def software_checkbox_state():
    selected_indices = []
    for index, var in enumerate(checkbox_vars):
        if var.get() == 1:
            selected_indices.append(index)
    return selected_indices

# Create GUI
root = tk.Tk()
root.title("Software Downloader")
root.state('zoomed')  # Start the application maximized

checkbox_frame = tk.Frame(root)
checkbox_frame.pack(fill=tk.BOTH, expand=True)

checkbox_vars = []
categories = {
    "Development": software_development,
    "Browsers": software_browsers,
    "Communication": software_communication,
    "Multimedia": software_multimedia,
    "Utilities": software_utilities,
    "Gaming": software_gaming,
    "Productivity": software_productivity,
    "Storage": software_storage,
    # Add more categories as needed
}

current_category_software = None

column_frames = []
current_column = None

def create_new_column():
    global current_column
    current_column = tk.Frame(checkbox_frame)
    current_column.pack(side="left", padx=10, pady=10, fill="y")
    column_frames.append(current_column)

# Define the number of columns dynamically
column_width = 200  # Adjust as needed
window_width = root.winfo_screenwidth()
num_columns = window_width // column_width
if num_columns < 1:
    num_columns = 1  # Ensure at least one column

for category, software_list in categories.items():
    if not current_column or len(current_column.winfo_children()) >= 40:  # Number of items per column
        create_new_column()

    title_frame = tk.Frame(current_column)
    title_frame.pack(anchor="w")  # Align the title to the left

    title_label = ttk.Label(title_frame, text=category, font=("Arial", 12, "bold"))
    title_label.pack(anchor="w")

    for software_name, _ in software_list:
        var = tk.IntVar()
        checkbox_vars.append(var)
        checkbox = tk.Checkbutton(current_column, text=software_name, variable=var, onvalue=1, offvalue=0)
        checkbox.pack(anchor="w")

    tk.Label(current_column, text="", height=1).pack()

download_button = tk.Button(root, text="Download", command=download_selected_software)
download_button.pack(pady=10)

root.mainloop()
