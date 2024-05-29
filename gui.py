import tkinter as tk
from wagner_fischer import spell_checker
from dictionary import dictionary

def main():
    global output_label  

    root = tk.Tk()
    root.title("Wagner-Fischer Spell Checker")
    
    input_label = tk.Label(root, text="Enter a word:")
    input_label.grid(row=0, column=0, padx=10, pady=10)

    input_field = tk.Entry(root)
    input_field.grid(row=0, column=1, padx=10, pady=10)

    check_button = tk.Button(root, text="Check Spelling", command=lambda: check_spelling(input_field.get(), dictionary, output_label))
    check_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    output_label = tk.Label(root, text="")
    output_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

def check_spelling(input_word, dictionary, output_label):
    suggested_word, distance = spell_checker(input_word, dictionary)
    output_text = f"Suggested correction for '{input_word}': '{suggested_word}' with edit distance {distance}"
    output_label.config(text=output_text)

if __name__ == "__main__":
    main()