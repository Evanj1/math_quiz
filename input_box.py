# Program to make a simple 
# login screen  


import tkinter as tk
# from first_steps import *
import random

# print("hello")
# print(random.randint(0,100))

questions=[]
answers=[]
responses=[]

def submit(event=None):
    global submitted
    qq=question_resp.get()
    print(qq)
    responses.append(int(qq))
    name_var.set("")
    submitted = True

def addition():
    x1=random.randint(0,100)
    x2=random.randint(0,100)
    question="{0}+{1}".format(x1,x2)
    answer=eval(question)
    return question, answer

def ask(answer,user_response):
    if answer==int(user_response):
        print(True)
    else:
        print("incorrect the answer is :{0}".format(answer))

root=tk.Tk()
root.title("Question")

question_label = tk.Label(root, text = "", font=('calibre',10, 'bold'))
question_label.pack(pady=20)
name_var=tk.StringVar()
question_resp = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))
question_resp.pack(pady=10)
sub_btn = tk.Button(root, text='Submit', command=submit)
sub_btn.pack(pady=20)

# Bind the Enter key to the submit function
root.bind('<Return>', submit)
# setting the windows size
root.geometry("400x200")
# question_label.grid(row=0,column=0)
# question_resp.grid(row=0,column=1)
# sub_btn.grid(row=2,column=1)
 
# declaring string variable
# for storing name and password
for i in range(0,2):
    q1,a1=addition()
    questions.append(q1)
    answers.append(a1)
    question_label.config(text=q1)
    root.update()
    # Wait for user input
    # Wait for the submit button to be pressed
    submitted = False
    while not submitted:
        root.update()
    

    #describes the size of the text box

root.destroy()  # Close the window after the loop
root.mainloop()

perf=0
for i,v in enumerate(questions):
    if  responses[i]==answers[i]:
        perf=perf+1

print("your performance was {0}/{1}".format(perf,len(questions)))

# performing an infinite loop 
# for the window to display
# root.mainloop()

responses

