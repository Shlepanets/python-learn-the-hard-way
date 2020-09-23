# this is like scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# now, we can do this
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")

# this takes no arguments
def print_none():
	print("I got nothin'.")


print_two("Zed","Dead")
print_two_again("One","Two")
print_one("The only!")
print_none()
