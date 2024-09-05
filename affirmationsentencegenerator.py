import tkinter as tk
from tkinter import messagebox

def generate_sentences():
    try:
        # Get input from text boxes
        aaa = aaa_entry.get().split(',')
        bbb = bbb_entry.get()
        ccc = ccc_entry.get().split(',')

        # Generate sentences
        sentences = []
        for word in aaa:
            for sentence in ccc:
                sentences.append(f"{word.strip()} {bbb.strip()} {sentence.strip()}")

        # Display sentences in a text box with newlines
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, '\n'.join(sentences))  # Use a single newline

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Affirmation Sentence Generator")

# Create input frames
frame_aaa = tk.Frame(root)
frame_bbb = tk.Frame(root)
frame_ccc = tk.Frame(root)

# Create labels and entries for input
tk.Label(frame_aaa, text="Subject (Words or sentences separated by comma):").pack(side=tk.LEFT)
aaa_entry = tk.Entry(frame_aaa, width=50)
aaa_entry.pack(side=tk.LEFT)

tk.Label(frame_bbb, text="Bridge (Single Sentence):").pack(side=tk.LEFT)
bbb_entry = tk.Entry(frame_bbb, width=50)
bbb_entry.pack(side=tk.LEFT)

tk.Label(frame_ccc, text="Descriptor (Words or sentences separated by comma):").pack(side=tk.LEFT)
ccc_entry = tk.Entry(frame_ccc, width=50)
ccc_entry.pack(side=tk.LEFT)

# Pack input frames
frame_aaa.pack(pady=5)
frame_bbb.pack(pady=5)
frame_ccc.pack(pady=5)

# Create button to generate sentences
generate_button = tk.Button(root, text="Generate Sentences", command=generate_sentences)
generate_button.pack(pady=10)

# Create text box to display results
result_text = tk.Text(root, height=10, width=60)
result_text.pack(pady=10)

# Start the main loop
root.mainloop()