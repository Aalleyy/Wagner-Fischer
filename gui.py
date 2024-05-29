import tkinter as tk
from wagner_fischer import spell_checker
from dictionary import dictionary

def main():
    global output_label, input_label, input_field, check_button, main_title, subtitle

    root = tk.Tk()
    root.title("Wagner-Fischer Spell Checker")

    # Set default window size with padding
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width - window_width) / 2)
    y_coordinate = int((screen_height - window_height) / 2)
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    
    # Create a frame to hold all widgets
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True)

    # Add main title
    main_title = tk.Label(main_frame, text="Spell Checker", font=("Helvetica", 24, "bold"))
    main_title.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 5), sticky='n')

    # Add subtitle
    subtitle = tk.Label(main_frame, text="based on Wagner Fischer", font=("Helvetica", 14))
    subtitle.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 20), sticky='n')

    input_label = tk.Label(main_frame, text="Enter a word:")
    input_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')

    input_field = tk.Entry(main_frame)
    input_field.grid(row=2, column=1, padx=10, pady=10, sticky='w')
    input_field.bind('<Return>', lambda event: check_spelling(input_field.get(), dictionary, output_label))

    check_button = tk.Button(main_frame, text="Check Spelling", command=lambda: check_spelling(input_field.get(), dictionary, output_label))
    check_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    output_label = tk.Label(main_frame, text="")
    output_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Center the frame within the root window and make it expand
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Ensure main_frame and its children resize properly
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)

    # Bind the configure event to adjust font sizes
    root.bind('<Configure>', lambda event: adjust_font_size(event, root, main_title, subtitle, input_label, output_label))

    root.mainloop()

def adjust_font_size(event, root, main_title, subtitle, input_label, output_label):
    # Calculate the new font size based on the window size
    new_size_main = min(int(root.winfo_height() / 15), 36)
    new_size_sub = min(int(root.winfo_height() / 30), 18)
    new_size_label = max(min(int(root.winfo_height() / 40), 14), 10)  # Minimum font size set to 10

    # Update font sizes
    main_title.config(font=("Helvetica", new_size_main, "bold"))
    subtitle.config(font=("Helvetica", new_size_sub))
    input_label.config(font=("Helvetica", new_size_label))
    output_label.config(font=("Helvetica", new_size_label))

def check_spelling(input_word, dictionary, output_label):
    suggested_word, distance = spell_checker(input_word, dictionary)
    output_text = f"Suggested correction for '{input_word}': '{suggested_word}' with edit distance {distance}"
    output_label.config(text=output_text)

if __name__ == "__main__":
    main()
