# Conor Shortt
# Run a few regex

import regex, menu

# Print program header.
menu.print_menu()

# User input for regex and string.
userRegex = input("Enter the regex you wish to use: ")
userString = input("Enter the string you wish to compare against the regex: ")

# Calls match from regex script on users regex and string.
result = (regex.match(userRegex, userString))
if result:
	print("\nThe regex " + userRegex + " matches the string " + userString)
else:
	print("\nThe regex " + userRegex + " does not match the string " + userString)
