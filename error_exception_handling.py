#
# try:
#  file = open("order.txt")
# except FileNotFoundError:
#  print("file not found")
#
# finally:
#  print("Please visit again Thanks")
#
# def open_file(file):
#  try:
#   with open(file, "r") as file:
#        for line in file.readline():
#          print(line.strip('\n'))
#  except FileNotFoundError as errmsg:
#        print("file can not be found ")
#  finally:
#   print("Please select the item from the list and enjoy your HAPPY MEAL")
#
# print(open_file(order.txt))
#
# import requests
#
# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
#
# print(post_codes_req)
# print(post_codes_req.headers)
# print(post_codes_req.content)
# print(type(post_codes_req.json()))





### `try`, `except` and `finally` block of codes
# They as if and else block -

# create a function called greetings
# def greetings():
#     pass

# name = "devops"
# year = 2021
# print(name + year)
# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     #raise
# # creating aliases
#     print("order.txt not found")
# finally:
#     print("Thank you for visiting hope you to see you again!")

# Second Iteration
def open_using_with_and_print(file):

    try:
        with open("order.txt", "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))
    # try code block ends
    except FileNotFoundError as errmsg:
        print("Sorry file not found ;) ")


    finally:
        return "Thank you for visiting hope you to see you again!"

print(open_using_with_and_print("order.txt"))

# create a new function to called open_with_to_write_to_file write/add/append
# display the data with the added items - item names - Pizza, cake, avacado, biryani,
def write_to_file(file, order_item):
    try:
        with open(file, "a") as file:
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("Sorry file cannot be found")
        raise
write_to_file("order.txt", "cake")
write_to_file("order.txt", "ice cream")
# ----------------



