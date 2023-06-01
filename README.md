# IntroToProg-Python-Mod07
This code is using the pickle module to save and load data, with try/except error handling to demo its functionality.

The pickle module is first imported. This module provides methods to serialize and deserialize Python objects, which means converting them to a byte stream and back.

The user is then prompted to enter some data to be pickled using the input() function.

The code then attempts to save the data entered by the user in the file named data.pkl using the pickle.dump() function. This function takes two arguments: the data to be pickled and the file object where the pickled data will be written. The file is opened in binary write mode ('wb') using the open() function. If successful, a message is printed indicating that the data was saved successfully. If an error occurs while saving the data, an error message is printed using an exception handler.

The code then tries to load the data from the data.pkl file using the pickle.load() function. This function takes one argument: the file object where the pickled data will be read from. The file is opened in binary read mode ('rb') using the open() function. If successful, the loaded data is assigned to a variable named loaded_data and printed. If an error occurs while loading the data, an error message is printed using an exception handler.

Displayed in the following two figures are the proof of function for the program in PyCharm and Command Line respectively. (See Figures 3-4:).
<img src="https://github.com/L4ughingF0x/IntroToProg-Python-Mod07/blob/main/screenshot2.png">
Figure 3:
<img src="https://github.com/L4ughingF0x/IntroToProg-Python-Mod07/blob/main/screenshot1.png"> 
Figure 4:
