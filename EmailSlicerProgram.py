email = input ("Enter your email: ")

index = email.index("@")

username = email[:index]
domain = email [index + 1:]

print (f"Your user name is {username} and domain is {domain}")