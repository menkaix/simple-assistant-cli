import argparse
import requests
import json

from callapi import post_prompt


# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-k", "--apikey", required=True,
   help="please specify apikey")
ap.add_argument("-b", "--baseurl", required=True,
   help="second operand")

ap.add_argument("-p", "--filepath", required=False,
   help="second operand")

args = vars(ap.parse_args())

history = [] ;

# Calculate the sum
while(True) :
    prompt = input(">")

    if len(prompt)<=0 :
        break
    else :
        response = post_prompt(args['baseurl'], args['apikey'], args['filepath'], history, prompt)
        print(response)