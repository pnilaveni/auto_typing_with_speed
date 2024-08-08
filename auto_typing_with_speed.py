import tkinter as tk
import pyautogui
import threading
import time
import webbrowser

typing = False
loop_count = 0

def start_typing():
    global typing, loop_count
    typing = True
    loop_count = 0  # Reset loop count on each start
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    delay = int(delay_entry.get())
    speed = float(speed_entry.get())
    time.sleep(delay)
    thread = threading.Thread(target=type_text, args=(speed,))
    thread.start()

def stop_typing():
    global typing
    typing = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

def type_text(speed):
    global typing, loop_count, loop_limit
    loop_limit = int(loop_entry.get())  # Get loop limit from entry
    while typing and loop_count < loop_limit:
        text = text_area.get("1.0", tk.END)
        for char in text:
            if not typing:
                break
            pyautogui.press(char)
            time.sleep(speed)
        loop_count += 1

        # Check loop completion and handle button states
        if loop_count >= loop_limit and typing:
            typing = False
            start_button.config(state=tk.NORMAL)
            stop_button.config(state=tk.DISABLED)
            # Optionally, reset text area position to beginning:
            text_area.see("1.0")  # Scroll to the beginning

def open_clientsdemos():
    webbrowser.open("https://www.clientsdemos.com")

def create_auto_typing_interface():
    root = tk.Tk()
    root.title("Auto Typing")
    root.configure(bg="#ADD8E6")  # Light blue background

    # Set window size
    window_width = 500
    window_height = 500
    root.geometry(f"{window_width}x{window_height}")

    # Center the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create a frame for the text area and the label
    frame = tk.Frame(root, bg="#ADD8E6")
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Create a label
    text_label = tk.Label(frame, text="Type your text here:", bg="#ADD8E6")
    text_label.grid(row=0, column=0, sticky='w', pady=5)

    global text_area
    text_area = tk.Text(frame, height=10, width=40, relief="solid", borderwidth=2)
    text_area.grid(row=1, column=0, columnspan=2, pady=5)

    delay_label = tk.Label(frame, text="Delay time (seconds):", bg="#ADD8E6")
    delay_label.grid(row=2, column=0, sticky='w', pady=5)

    global delay_entry
    delay_entry = tk.Entry(frame)
    delay_entry.insert(0, "5")  # Default delay time
    delay_entry.grid(row=2, column=1, pady=5)

    loop_label = tk.Label(frame, text="Loop count:", bg="#ADD8E6")
    loop_label.grid(row=3, column=0, sticky='w', pady=5)

    global loop_entry
    loop_entry = tk.Entry(frame)
    loop_entry.insert(0, "1")  # Default loop count
    loop_entry.grid(row=3, column=1, pady=5)

    speed_label = tk.Label(frame, text="Speed (seconds per character):", bg="#ADD8E6")
    speed_label.grid(row=4, column=0, sticky='w', pady=5)

    global speed_entry
    speed_entry = tk.Entry(frame)
    speed_entry.insert(0, "0.1")  # Default speed
    speed_entry.grid(row=4, column=1, pady=5)

    button_frame = tk.Frame(frame, bg="#ADD8E6")
    button_frame.grid(row=5, column=0, columnspan=2, pady=10)

    global start_button, stop_button
    start_button = tk.Button(button_frame, text="Start", command=start_typing)
    start_button.grid(row=0, column=0, padx=5)
    stop_button = tk.Button(button_frame, text="Stop", state=tk.DISABLED, command=stop_typing)
    stop_button.grid(row=0, column=1, padx=5)

    # Add copyright text with hyperlink
    copyright_frame = tk.Frame(root, bg="#ADD8E6")
    copyright_frame.pack(side="bottom", pady=10)

    copyright_label = tk.Label(copyright_frame, text="All copyright with ", bg="#ADD8E6")
    copyright_label.pack(side="left")

    hyperlink = tk.Label(copyright_frame, text="ClientsDemos", bg="#ADD8E6", fg="blue", cursor="hand2")
    hyperlink.pack(side="left")
    hyperlink.bind("<Button-1>", lambda e: open_clientsdemos())

    root.mainloop()

if __name__ == "__main__":
    create_auto_typing_interface()
