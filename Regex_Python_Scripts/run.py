# Conor Shortt
# Run a few regex

import argparse
import regex, menu
import printdocs
import tests

# Print program header.
menu.print_menu()

# Calls match from regex script on users regex and string.
parser = argparse.ArgumentParser(description='Enter the regex and string you wish to compare against one another.')
optional = parser.add_argument_group('optional arguments')
optional.add_argument('-r', action='store', type=str, help='The regex to convert to an NFA.')
optional.add_argument('-s', action='store', type=str, help='The string to compare against the regular expression.')
optional.add_argument('--info', action='store_true', help='A menu that allows you to print information on each '
                                                          'function of this program.')
optional.add_argument('--tests', action='store_true', help='Run tests that checks to see if regex and string '
                                                           'comparison is working correctly. Returns nothing if '
                                                           'tests all pass.')

args = parser.parse_args()

if args.info:
    printdocs.docs()

elif args.tests:
    tests.test()
    print("Tests complete, if nothing returned all tests passed.")

elif args.r and args.s:
    userRegex = str(args.r)
    userString = str(args.s)

    result = (regex.match(userRegex, userString))

    if result:
        print("\nThe regex " + userRegex + " matches the string " + userString)
    else:
        print("\nThe regex " + userRegex + " does not match the string " + userString)

else:
    print("No arguments supplied. Use python run.py -h/--help to get help.")
