import random

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = [chr(i) for i in range(97,97 + 26)]
uppercase = [chr(i) for i in range(65,65 + 26)]
special = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

combined_list = digits + lowercase + uppercase + special

def strongPass(maxlen):
    temp = [random.choice(digits) + random.choice(lowercase) + random.choice(uppercase) + random.choice(special)]
    for i in range(len(temp), maxlen):
        temp.append(random.choice(combined_list))
        random.shuffle(temp)
    return ''.join(temp)
