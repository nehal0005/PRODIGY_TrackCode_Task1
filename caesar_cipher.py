import tkinter as tk
from tkinter import messagebox, ttk

# --- Caesar Cipher Algorithm ---
def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isupper():
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            result += new_char
        elif char.islower():
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            result += new_char
        else:
            result += char
    return result

# --- GUI Actions ---
def process_text():
    text = entry_message.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter a message first!")
        return
    
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Input Error", "Shift key must be a number!")
        return
        
    mode = var_mode.get()
    result = caesar_cipher(text, shift, mode)
    
    entry_result.config(state="normal")
    entry_result.delete("1.0", tk.END)
    entry_result.insert("1.0", result)
    entry_result.config(state="disabled")

def copy_to_clipboard():
    result_text = entry_result.get("1.0", tk.END).strip()
    if result_text:
        root.clipboard_clear()
        root.clipboard_append(result_text)
        messagebox.showinfo("Success", "Copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Nothing to copy yet.")

def clear_all():
    entry_message.delete("1.0", tk.END)
    entry_shift.delete(0, tk.END)
    entry_shift.insert(0, "3")
    entry_result.config(state="normal")
    entry_result.delete("1.0", tk.END)
    entry_result.config(state="disabled")

# --- Building the Application Interface ---
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("500x520")
root.configure(bg="#212529")
root.resizable(False, False)

# Forces the window to pop up directly on top of all other applications immediately
root.lift()
root.attributes('-topmost', True)
root.after(1, lambda: root.attributes('-topmost', False))

style = ttk.Style()
style.theme_use('clam')

# 1. Title
lbl_title = tk.Label(root, text="CAESAR CIPHER", font=("Helvetica", 18, "bold"), fg="#0D6EFD", bg="#212529")
lbl_title.pack(pady=15)

# 2. Input Box
lbl_msg = tk.Label(root, text="Enter Message:", font=("Helvetica", 10, "bold"), fg="white", bg="#212529")
lbl_msg.pack(anchor="w", padx=30)

entry_message = tk.Text(root, height=4, width=50, font=("Helvetica", 10), bg="#2B3035", fg="white", insertbackground="white")
entry_message.pack(pady=5)

# 3. Parameters (Shift & Mode)
frame_settings = tk.Frame(root, bg="#212529")
frame_settings.pack(fill="x", padx=30, pady=10)

lbl_shift = tk.Label(frame_settings, text="Shift Key:", font=("Helvetica", 10, "bold"), fg="white", bg="#212529")
lbl_shift.pack(side="left")

entry_shift = tk.Entry(frame_settings, width=5, font=("Helvetica", 10), bg="#2B3035", fg="white", insertbackground="white")
entry_shift.pack(side="left", padx=10)
entry_shift.insert(0, "3")

var_mode = tk.StringVar(value="encrypt")

radio_enc = tk.Radiobutton(frame_settings, text="Encrypt", variable=var_mode, value="encrypt", 
                           font=("Helvetica", 10), fg="white", bg="#212529", selectcolor="#2B3035", activebackground="#212529", activeforeground="white")
radio_enc.pack(side="right", padx=5)

radio_dec = tk.Radiobutton(frame_settings, text="Decrypt", variable=var_mode, value="decrypt", 
                           font=("Helvetica", 10), fg="white", bg="#212529", selectcolor="#2B3035", activebackground="#212529", activeforeground="white")
radio_dec.pack(side="right", padx=5)

# 4. Action Trigger Button
btn_process = tk.Button(root, text="RUN CIPHER", command=process_text, font=("Helvetica", 11, "bold"), 
                        bg="#0D6EFD", fg="white", width=20, cursor="hand2", activebackground="#0b5ed7", activeforeground="white")
btn_process.pack(pady=15)

# 5. Output Box
lbl_res = tk.Label(root, text="Output Result:", font=("Helvetica", 10, "bold"), fg="white", bg="#212529")
lbl_res.pack(anchor="w", padx=30)

entry_result = tk.Text(root, height=4, width=50, font=("Helvetica", 10), bg="#1E2125", fg="#0D6EFD", state="disabled")
entry_result.pack(pady=5)

# 6. Controls
frame_bottom = tk.Frame(root, bg="#212529")
frame_bottom.pack(pady=15)

btn_copy = tk.Button(frame_bottom, text="Copy Result", command=copy_to_clipboard, font=("Helvetica", 10), 
                     bg="#198754", fg="white", width=12, cursor="hand2", activebackground="#157347", activeforeground="white")
btn_copy.pack(side="left", padx=10)

btn_clear = tk.Button(frame_bottom, text="Clear", command=clear_all, font=("Helvetica", 10), 
                      bg="#DC3545", fg="white", width=12, cursor="hand2", activebackground="#BB2D3B", activeforeground="white")
btn_clear.pack(side="left", padx=10)

# Starts the execution loop immediately upon calling the script
root.mainloop()