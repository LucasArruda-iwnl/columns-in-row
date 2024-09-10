import tkinter as tk
from tkinter import messagebox


def transform_to_horizontal_with_commas():
    data = text_box.get("1.0", tk.END).strip()
    if not data:
        messagebox.showwarning("HEY!", "NO data to process.")
        return
    
    start_char = start_char_entry.get()
    end_char = end_char_entry.get()

    lines = data.split('\n')
    result = ','.join(f"{start_char}{line.strip()}{end_char}" for line in lines if line.strip())
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

def transform_to_horizontal_without_commas():
    data = text_box.get("1.0", tk.END).strip()
    if not data:
        messagebox.showwarning("HEY!", "NO data to process.")
        return
    
    start_char = start_char_entry.get()
    end_char = end_char_entry.get()

    lines = data.split('\n')
    result = ' '.join(f"{start_char}{line.strip()}{end_char}" for line in lines if line.strip())
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

def format_as_cpf():
    data = text_box.get("1.0", tk.END).strip()
    if len(data) != 11 or not data.isdigit():
        messagebox.showwarning("Invalid input", "Please enter exactly 11 digits.")
        return
    cpf_formatted = f"{data[:3]}.{data[3:6]}.{data[6:9]}-{data[9:]}"
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, cpf_formatted)

def remove_cpf_format():
    data = text_box.get("1.0", tk.END).strip()
    cpf_unformatted = data.replace('.', '').replace('-', '')
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, cpf_unformatted)

def copy_to_clipboard():
    app.clipboard_clear()
    output_text = output_box.get("1.0", tk.END).strip()
    if output_text:
        app.clipboard_append(output_text)
        messagebox.showinfo("Copy!", "Result copied to clipboard.")
    else:
        messagebox.showwarning("No data to copy")

app = tk.Tk()
app.title("column to line")


app.geometry("600x440")

text_label = tk.Label(app, text="Copy column:")
text_label.pack()
text_box = tk.Text(app, height=10, width=50)
text_box.pack()

start_char_label = tk.Label(app, text="Character at the start:")
start_char_label.pack()
start_char_entry = tk.Entry(app)
start_char_entry.pack()

end_char_label = tk.Label(app, text="Character at the end:")
end_char_label.pack()
end_char_entry = tk.Entry(app)
end_char_entry.pack()

comma_button = tk.Button(app, text="with ,", command=transform_to_horizontal_with_commas)
comma_button.pack(pady=5)

space_button = tk.Button(app, text="without ,", command=transform_to_horizontal_without_commas)
space_button.pack(pady=5)

cpf_frame = tk.Frame(app)
cpf_frame.pack(pady=5)

cpf_format_button = tk.Button(cpf_frame, text="Format as CPF", command=format_as_cpf)
cpf_format_button.pack(side=tk.LEFT, padx=10)

cpf_remove_button = tk.Button(cpf_frame, text="Remove CPF format", command=remove_cpf_format)
cpf_remove_button.pack(side=tk.LEFT, padx=10)

output_frame = tk.Frame(app)
output_frame.pack(pady=5)

output_label = tk.Label(output_frame, text="Result")
output_label.pack(side=tk.LEFT)

output_box = tk.Text(output_frame, height=2, width=40)
output_box.pack(side=tk.LEFT)

copy_button = tk.Button(output_frame, command=copy_to_clipboard, text="Copy the result")
copy_button.pack(side=tk.LEFT, padx=10)

app.mainloop()
