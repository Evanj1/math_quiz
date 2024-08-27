import random

# print("hello")
# print(random.randint(0,100))

def addition():
    x1=random.randint(0,100)
    x2=random.randint(0,100)
    question="{0}+{1}".format(x1,x2)
    answer=eval(question)
    return question, answer

def ask():
    a,b= addition()
    response = input("What is: {}".format(a))
    # return response
    print(response)
    if b==int(response):
        print(True)
    else:
        print("incorrect the answer is :{b}".format(b))

# ask()


# response = input("What is: {}".format(addition()))