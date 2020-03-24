# Conor Shortt
# Run a few regex

import regex

userRegex = input("Enter the regex you wish to use: ")
userString = input("Enter the string you wish to compare against the regex: ")
print (regex.match(userRegex, userString))
