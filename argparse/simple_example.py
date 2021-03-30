# import the necessary packages
import argparse

# construct the argument parse and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="name of the user")
args = vars(ap.parse_args())

# display a friendly message to the user
print(f"Hi there {args['name']}, it's nice to meet you!")
