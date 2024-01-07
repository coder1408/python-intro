#get user email address
#slice out user name
#slice domain name
#format message
#display output message
email=input("What is your email address? : ").strip()
user=email[:email.index("@")]
domain=email[email.index("@")+1:]
output="Your username is {} and domain name is {}".format(user,domain)
print(output)
