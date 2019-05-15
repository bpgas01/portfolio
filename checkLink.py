import unittest                                         # Testing library which I ended not using

import re
import os
import sys
import time


class link_Check():
   
    def __init__(self):                                 # init the link_check() class
        print('Reading contents of list.... Please wait')  
        self.lines = ['one.com','two.com','three.com']  # Predefine blocked links. I have provided a few examples
        self.content = None
       
    def List_return(self):                              # Return the list value to the main script for reference
        return self.lines

    def LinkSearch(self, messageContent):
        found = False                                   # Set the found variable to false, we haven't checked anything yet
        
        for i in self.lines:                            # Start to loop through the list
 
            if i in str(messageContent):                # check to see if the list contains anything in the sent link.
                found = True                            # If so, set found to True... We found something
                print(i,' + ',messageContent)           # Print the blocked link and message

        if found == True:                               # If something is found, return True back to the main script
            return True

        if found == False:                              #If nothing is found, return False back to the main script
            return False

    



  
        
       
