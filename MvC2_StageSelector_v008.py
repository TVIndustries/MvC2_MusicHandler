# MvC2_StageSelector_v008.py

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import shutil
from dict_musicHandler import stage_data_dict, track_settings

max_track_amount = 32

# Initialize the main application window
root = tk.Tk()
root.title("MvC2 Music Handler")

current_stage = None  # Store the currently selected stage
# Set dark mode colors
dark_mode_bg = "#1E1E1E"
dark_mode_fg = "#FFFFFF"

# Create a custom style for the combobox
root.style = ttk.Style()
root.style.configure(
    "Dark.TCombobox",
    fieldbackground=dark_mode_bg,
    foreground=dark_mode_bg,
    background=dark_mode_bg,
)
# Create labels and dropdowns for each track
track_labels = []
track_dropdowns = []

# Create a dictionary to store track choices for each stage and playlist
track_choices = {playlist: {stage: ['Choose from ADXs'] * max_track_amount for stage in stage_data_dict}
                 for playlist in track_settings}


# Function to save the current track choices for the current playlist
# Function to save the current track choices for the current playlist
def save_playlist_choices(playlist):
    filename = get_playlist_choices_filename(playlist)
    with open(filename, "w") as file:
        if playlist == '32 Shuffle':
            if '32Shuffle' not in track_choices[playlist]:
                track_choices[playlist]['32Shuffle'] = ['Choose from ADXs'] * 32
            file.write('32Shuffle:' + ",".join(track_choices[playlist]['32Shuffle']) + "\n")
        else:
            for stage in stage_data_dict:
                # Get the number of tracks for the current playlist
                track_amount = track_settings[playlist]['TrackAmount']

                # Get the choices for the current stage and filter out any "Choose from ADXs" entries
                choices = [choice for choice in track_choices[playlist][stage] if choice != "Choose from ADXs"]

                # Ensure that only the specified number of track choices is saved
                if len(choices) > track_amount:
                    choices = choices[:track_amount]

                # Fill any remaining slots with "Choose from ADXs" if necessary
                choices += ["Choose from ADXs"] * (track_amount - len(choices))

                file.write(f"{stage}:" + ",".join(choices) + "\n")


# Function to load saved track choices for the current playlist
def load_playlist_choices(playlist):
    filename = get_playlist_choices_filename(playlist)
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    stage, choices = parts
                    if playlist == '32 Shuffle':
                        track_choices[playlist]['32Shuffle'] = choices.split(',')
                    else:
                        track_choices[playlist][stage] = choices.split(',')


# Function to create a filename based on the playlist
def get_playlist_choices_filename(playlist):
    if playlist == '32 Shuffle':
        return 'Playlists\\32_ShufflePlaylist.txt'
    else:
        track_amount = track_settings[playlist]['TrackAmount']
        formatted_track_amount = f"{track_amount:02d}"
        return f"Playlists\\{formatted_track_amount}_TrackPlaylist.txt"


# Function to create and center the images
def create_centered_image(image_path, padding=3):
    img = Image.open(image_path)
    img = img.resize((100, 100), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    canvas = tk.Canvas(stage_image_frame, width=106, height=106, bg=dark_mode_bg)
    canvas.create_image(padding + 2, padding + 2, anchor=tk.NW, image=photo)
    canvas.image = photo  # Reference to prevent garbage collection
    canvas.configure(bg=dark_mode_bg, highlightbackground=dark_mode_bg)
    return canvas


def on_image_click(stage_name):
    global current_stage
    track_playlist = track_var.get()  # Get the selected playlist
    if track_playlist != '32 Shuffle':
        current_stage = stage_name
    else:
        current_stage = '32Shuffle'
    track_setting = track_var.get()
    update_track_labels(track_setting)


def select_image(stage_name):
    global current_stage
    track_playlist = track_var.get()  # Get the selected playlist
    if track_playlist != '32 Shuffle':
        current_stage = stage_name
    else:
        current_stage = '32Shuffle'
    track_setting = track_var.get()
    update_track_labels(track_setting)

    border_color = "magenta" if track_playlist != '32 Shuffle' else dark_mode_bg

    # Change the background color and border color of the selected stage image
    for canvas, name in stage_canvases:
        if name == stage_name:
            canvas.configure(bg=border_color, highlightbackground=border_color)
        else:
            canvas.configure(bg=dark_mode_bg, highlightbackground=dark_mode_bg)


# Function to update the displayed track labels and dropdowns based on the selected playlist
def update_track_labels(track_playlist):
    global current_stage

    # Initialize stage_choices
    stage_choices = []

    # Check if the playlist changed from '32 Shuffle'
    if track_playlist != '32 Shuffle':
        # current_stage = 'STG00'  # Automatically set the current stage to 'STG00'
        # Highlight 'STG00' with magenta background
        for canvas, name in stage_canvases:
            if name == current_stage:
                canvas.configure(bg="magenta")
            else:
                canvas.configure(bg=dark_mode_bg)

    # Handle 32 Shuffle playlist differently
    if track_playlist == '32 Shuffle':
        # Check if '32Shuffle' is in track_choices[track_playlist] dictionary
        if '32Shuffle' in track_choices[track_playlist]:
            stage_choices = track_choices[track_playlist]['32Shuffle'][:32]
        else:
            # If the key is not present, provide a default value (e.g., all 'Choose from ADXs')
            stage_choices = ['Choose from ADXs'] * 32
    else:
        if current_stage == '32Shuffle':
            # Update image selection for the previous '32Shuffle' stage
            current_stage = 'STG00'
            for canvas, name in stage_canvases:
                if name == current_stage:
                    canvas.configure(bg="magenta")
                else:
                    canvas.configure(bg=dark_mode_bg)

        if current_stage is not None:
            # Get the selected track amount
            track_amount = track_settings[track_playlist]['TrackAmount']

            # Get the stage-specific information
            stage_info = stage_data_dict[current_stage]

            # Get the choices for the current stage and filter out any "Choose from ADXs" entries
            stage_choices = track_choices[track_playlist][current_stage][:track_amount]
        else:
            # In "32 Shuffle" mode, create or update the special 32-track list
            special_32_track_list = track_choices['32 Shuffle'].get('special_32_track_list', ['Choose from ADXs'] * 32)
            stage_choices = special_32_track_list

    # Clear the existing track labels and dropdowns
    for label in track_labels:
        label.grid_forget()
        label.destroy()
    for dropdown in track_dropdowns:
        dropdown.grid_forget()
        dropdown.destroy()

    track_labels.clear()
    track_dropdowns.clear()

    # Create new track labels and dropdowns based on the selected playlist and stage
    for i in range(len(stage_choices)):
        label = tk.Label(track_list_frame, text=f'Track {i + 1}:', fg=dark_mode_fg, bg=dark_mode_bg)
        label.grid(row=i % 16, column=(i // 16) * 2, padx=10, pady=5, sticky='w')

        dropdown = ttk.Combobox(
            track_list_frame,
            style="Dark.TCombobox"  # Add this line to use a custom style
        )
        adx_files = ['Choose from ADXs'] + [f for f in os.listdir("ADXs") if f.endswith('.adx')]
        dropdown['values'] = adx_files
        dropdown.set(stage_choices[i])
        dropdown.grid(row=i % 16, column=(i // 16) * 2 + 1, padx=10, pady=5, sticky='w')
        track_labels.append(label)
        track_dropdowns.append(dropdown)


# Function to save the current track choices for the current stage and playlist
def save_track_choices():
    if current_stage is not None:
        playlist = track_var.get()
        choices = [dropdown.get() for dropdown in track_dropdowns[:track_settings[playlist][
            'TrackAmount']]]  # Get choices up to the selected track amount
        track_choices[playlist][current_stage] = choices
        save_playlist_choices(playlist)


def on_playlist_change(event):
    global stage_name
    global gbl_track_amount
    gbl_track_amount = track_settings[playlist]['TrackAmount']
    # Get the selected playlist
    selected_playlist = track_var.get()
    if playlist != '32 Shuffle':
        stage_name = 'STG00'
    # Update the track labels and dropdowns for the selected playlist
    update_track_labels(selected_playlist)


gbl_track_amount = 2
# Create a Save Track List button
save_button = ttk.Button(root, text="Save Track List", command=save_track_choices)
save_button.grid(row=0, column=2, padx=10, pady=5, sticky='w')

# List of stage names
stages = list(stage_data_dict.keys())

# Create a frame for the stage images
stage_image_frame = ttk.Frame(root, style="Dark.TFrame")
stage_image_frame.grid(row=1, column=0, columnspan=4)

# Create a custom style for the frame
root.style.configure(
    "Dark.TFrame",
    background=dark_mode_bg,
)
# Load and display stage images with padding
stage_canvases = []  # Store canvas widgets

for i, stage_name in enumerate(stages):
    image_path = f"images/{stage_name}_thumb.png"  # Replace with the actual image paths
    if os.path.isfile(image_path):
        canvas = create_centered_image(image_path, padding=3)
        canvas.grid(row=i // 4, column=i % 4)
        # canvas.configure(bg=dark_mode_bg)
        canvas.bind("<Button-1>", lambda event, stage=stage_name: select_image(stage))
        canvas.configure(bg=dark_mode_bg)
        stage_canvases.append((canvas, stage_name))

# Track List Frame
track_list_frame = ttk.Frame(root, style="Dark.TFrame")
track_list_frame.grid(row=0, column=5, rowspan=2)

# Label for Track Playlist selection
track_label = tk.Label(root, text="Track Playlist:")
track_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
track_label.configure(fg=dark_mode_fg, bg=dark_mode_bg)
# Options for Track Playlist dropdown
track_var = tk.StringVar(value='2 Track')  # Create a variable with an initial value
track_dropdown = ttk.Combobox(
    root,
    textvariable=track_var,
    values=list(track_settings.keys()),
    style="Dark.TCombobox"  # Add this line to use a custom style
)
track_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky='w')

# Bind the combobox to the callback function
track_dropdown.bind("<<ComboboxSelected>>", on_playlist_change)

# Load saved track choices when the program starts
for playlist in track_settings:
    for stage in stage_data_dict:
        load_playlist_choices(playlist)


# Function to export the track files
def export_tracks():
    global track_choices  # Use the global variable

    selected_playlist = track_var.get()

    if selected_playlist == '32 Shuffle':
        stage_name = '32Shuffle'
        output_dir = f"Output/{selected_playlist}"
        os.makedirs(output_dir, exist_ok=True)
        for i in range(32):
            track_choice = track_choices[selected_playlist][stage_name][i]
            if track_choice != 'Choose from ADXs':
                src_file = f"ADXs/{track_choice}"
                dst_file = ("ADX_S%02X" % i) + '0.BIN'
                dst_file_path = os.path.join(output_dir, dst_file)
                print(dst_file, f"{track_choice}")
                shutil.copy(src_file, dst_file_path)
    else:
        for stage_name in stage_data_dict:
            output_dir = f"Output/{selected_playlist}"
            os.makedirs(output_dir, exist_ok=True)
            stage_choices = track_choices[selected_playlist][stage_name]  # Change the variable name to avoid shadowing
            for i, track_choice in enumerate(stage_choices):
                if track_choice != 'Choose from ADXs':
                    src_file = f"ADXs/{track_choice}"
                    track_fmt = stage_data_dict[stage_name]['TrackFmt']
                    if i == 0:
                        midstring = '_'
                    else:
                        midstring = '%1X' % i
                    track_out = track_fmt % midstring
                    dst_file = f"{track_out}.BIN"
                    dst_file_path = os.path.join(output_dir, dst_file)
                    print(dst_file, f"{track_choice}")
                    shutil.copy(src_file, dst_file_path)


# Create an Export Tracks button
export_button = ttk.Button(root, text="Export Tracks", command=export_tracks)
export_button.grid(row=0, column=3, padx=10, pady=5, sticky='w')

# Configure root window for dark mode
root.configure(bg=dark_mode_bg)
root.option_add("*TButton*highlightBackground", dark_mode_bg)
root.option_add("*TButton*highlightColor", dark_mode_bg)
root.option_add("*TButton*background", dark_mode_fg)
root.option_add("*TButton*foreground", dark_mode_bg)
root.option_add("*TCombobox*background", dark_mode_fg)
root.option_add("*TCombobox*foreground", dark_mode_bg)
root.option_add("*TCombobox*listbox*Background", dark_mode_bg)
root.option_add("*TCombobox*listbox*Foreground", dark_mode_fg)
root.option_add("*TLabel*background", dark_mode_bg)
root.option_add("*TLabel*foreground", dark_mode_fg)
root.option_add("*TEntry*background", dark_mode_fg)
root.option_add("*TEntry*foreground", dark_mode_bg)

# Start the GUI application
root.mainloop()
