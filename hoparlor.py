import tkinter as tk
import pyaudio

# Create a Tkinter window
window = tk.Tk()

# Create an instance of PyAudio
audio = pyaudio.PyAudio()

# Get the available audio outputs
audio_outputs = []
for i in range(audio.get_device_count()):
    output = audio.get_device_info_by_index(i)
    audio_outputs.append(output)

# Global variable to store the active audio stream
active_stream = None

def change_audio_output():
    global active_stream

    if active_stream:
        # Stop the active stream if it exists
        active_stream.stop_stream()
        active_stream.close()

    # Get the index of the selected audio output
    selected_index = audio_output_listbox.curselection()[0]
    selected_output = audio_outputs[selected_index]

    # Open a new audio stream with the selected output device
    active_stream = audio.open(output_device_index=selected_output['index'], format=pyaudio.paInt16, channels=2, rate=44100, output=True)

    # Play a test sound to verify the output
    test_sound = b'\x00\x00\x00\x00' * 44100  # Silence for 1 second
    active_stream.write(test_sound)

def close_audio_stream():
    global active_stream

    if active_stream:
        active_stream.stop_stream()
        active_stream.close()
        active_stream = None

# Create a listbox to display the available audio outputs
audio_output_listbox = tk.Listbox(window)
for output in audio_outputs:
    audio_output_listbox.insert(tk.END, output['name'])

# Create a button to change the default audio output
change_output_button = tk.Button(window, text='Change Default Audio Output', command=change_audio_output)

# Create a button to close the audio stream
close_stream_button = tk.Button(window, text='Close Audio Stream', command=close_audio_stream)

# Pack the widgets into the window

audio_output_listbox.pack()
change_output_button.pack()
close_stream_button.pack()

# Start the main loop
window.mainloop()