import json
import tempfile
import tkinter as tk
from tkinter import filedialog
import seaborn as sns
import matplotlib.pyplot as plt
import torch
import weasyprint

def custom_build_print_options(options: dict = None):
    merged = DEFAULT_PRINT_OPTIONS.copy()
    if options:
        merged.update(options)
    return merged


def custom_generate_pdf(html: str, print_options: dict) -> bytes:

    pdf_bytes = weasyprint.HTML(string=html).write_pdf(**print_options)
    return pdf_bytes



def select_html_file():
    file_selected = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
    if file_selected:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_selected)

def generate_and_display_pdf():
    file_path = entry_path.get()
    if not file_path.endswith('.html'):
        status_label.config(text="Selected file is not an HTML file.")
        return

    with open(file_path, 'r') as file:
        html_content = file.read()

    print_options = custom_build_print_options()

 
    pdf_content = custom_generate_pdf(html_content, print_options)

    
    
    status_label.config(text=f"Generated PDF content: {pdf_content[:50]}...")

  

  
    sns.lineplot(x=range(len(torch_tensor)), y=torch_tensor.numpy())
    plt.title('Seaborn Plot of Torch Tensor')
    plt.show()

root = tk.Tk()
root.title("PDF Generation with GUI")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=20, pady=20)

label_path = tk.Label(frame, text="Select HTML File:")
label_path.grid(row=0, column=0, sticky='e')

entry_path = tk.Entry(frame, width=50)
entry_path.grid(row=0, column=1, padx=5)

button_browse = tk.Button(frame, text="Browse", command=select_html_file)
button_browse.grid(row=0, column=2, padx=5)

button_generate = tk.Button(frame, text="Generate PDF", command=generate_and_display_pdf)
button_generate.grid(row=1, column=1, pady=10)

status_label = tk.Label(frame, text="")
status_label.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
