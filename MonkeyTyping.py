import tkinter as tk
import random
import time

# Function definitions

def clear_placeholder(event):
    if user_entry.get() == 'Enter your name':
        user_entry.delete(0, tk.END)

def add_placeholder(event):
    if user_entry.get() == '':
        user_entry.insert(0, 'Enter your name')


def username():
    global user_name 
    user_name = user_entry.get()
    user_entry.place_forget()
    user_entry_lb.config(text="Welcome  "+ user_name)

def show():
    leader_label.config(text="hello world")

def start_typing():
    global start_time
    start_time = time.time()  
    entry.config(state="normal")

def check_sentence(*args):
    typed_sentence = user_inp.get()
    if len(typed_sentence) <= len(rn_sentences):
        for i in range(len(typed_sentence)):
            if typed_sentence[i] == rn_sentences[i]: 
                entry.config(fg="green") 
            else:
                entry.config(fg="red")
                entry.delete(i, "end") 
    else:
        entry.config(state="disabled")
        end_time = time.time()
        time_taken = end_time - start_time  
        ans = round(time_taken)
        time_taken /= 60  
        wpm = len(typed_sentence.split()) // time_taken 
        wpm_label.config(text=f"WPM: {wpm}")
        if ans < 59:
            time_taken_lb.config(text =f"Time Taken: {ans}sec")
        else:
            time_taken_lb.config(text =f"Time Taken: {round(ans/60,2)}min")
    
    word_count = len(typed_sentence.split())
    word_count_label.config(text=f"Words Typed: {word_count}")

def close(event):
    mn.destroy()

def reset_function():
    user_inp.set('')

    # Generate a new random sentence
    global rn_sentences
    rn_sentences = random.choice(words)

    # Update the label with the new sentence
    label.config(text=rn_sentences)

    # Reset the color of the entry field
    entry.config(fg="black")

    # Clear the WPM, word count and time taken labels
    wpm_label.config(text="")
    word_count_label.config(text="")
    time_taken_lb.config(text="")

# Main program
if __name__ == "__main__":
    mn = tk.Tk()
    mn.title("Typing Test")
    mn["bg"] = "#cdc0b0"
    mn.geometry("1000x800")

    logo = tk.Label(mn,text="Typing Test",font = ("Arial",20,"bold"),bg ="#cdc0b0")
    logo.place(x=330,y=10)

    words = ["The quick brown fox jumps over the lazy dog.",
              "Pack my box with five dozen liquor jugs.", 
              "Jackdaws love my big sphinx of quartz.", 
              "How vexingly quick daft zebras jump!", 
              "Bright vixens jump; dozy fowl quack."]

    rn_sentences = random.choice(words)
    label = tk.Label(mn,text = rn_sentences,font =("Arial",15,"bold"))
    label.place(x=200,y=150)

    user_inp = tk.StringVar()
    username_inp = tk.StringVar()
    entry = tk.Entry(mn,textvariable=user_inp,font=("Arial",15,"bold"))
    entry.place(width=440,height=30,x=200,y=200)
    entry.config(state="disabled")

    word_count_label = tk.Label(mn, text="", font=("Arial", 15))
    word_count_label["bg"]="#cdc0b0"
    word_count_label.place(width=150,height=30,x=195, y=300)

    wpm_label = tk.Label(mn, text="", font=("Arial", 15))
    wpm_label["bg"]="#cdc0b0"
    wpm_label.place(width=120,height=30,x=190, y=400)

    time_taken_lb = tk.Label(mn,text="",font=("Arial", 15))
    time_taken_lb["bg"]="#cdc0b0"
    time_taken_lb.place(width=185,height=30,x=190, y=350)

    leader_label = tk.Label(mn,text="",font=("Arial", 15))
    leader_label["bg"]="#cdc0b0"
    leader_label.place(width=120,height=30,x=190, y=500)

    user_entry_lb = tk.Label(mn,text="",font=("Arial",15,"bold"));user_entry_lb['bg']="#cdc0b0"
    user_entry_lb.place(width=350,height=30,x=200,y=80)

    user_entry = tk.Entry(mn,textvariable=username_inp,font=("Arial",15))
    user_entry.insert(0, 'Enter your name')
    user_entry.bind("<FocusIn>", clear_placeholder)
    user_entry.bind("<FocusOut>", add_placeholder)
    user_entry.place(width=350,height=30,x=200,y=80)

    start_button = tk.Button(mn,text="Start",font=("Arial",15,"bold"),command=start_typing)
    start_button.place(x=200,y=250,width=80,height=30)

    exit_button = tk.Button(mn,text="Exit",font=("Arial",15,"bold"),command=mn.destroy)
    exit_button.place(x=500,y=250,width=80,height=30)

    leader_button = tk.Button(mn,text="Show Leaderboard",font=("Arial",15,"bold"),command=show)
    leader_button.place(x=290,y=250,width=200,height=30)

    reset_button = tk.Button(mn, text="↺", font=("Arial", 25, "bold"), command=reset_function)
    reset_button.place(x=600, y=250, width=30, height=30)

    user_submit = tk.Button(mn,text="Submit",font=("Arial", 15, "bold"),command=username)
    user_submit.place(width=80,height=30,x=560,y=80)

    user_inp.trace("w", check_sentence)
    mn.bind('<Control-q>', close)

    mn.mainloop()




