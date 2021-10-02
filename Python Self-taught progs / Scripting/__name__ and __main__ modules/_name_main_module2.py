# Program created by Brayan Vera
# Date 09/24/21

import _name_main_module #This is getting imported to this current file
                    #So it provides the output of that file.

_name_main_module.main() #<-- Allows us to run the main() function of __name__main anyways.

print("Second Module's Name: {}".format(__name__)) #Will print __main__ corresponding to this file


