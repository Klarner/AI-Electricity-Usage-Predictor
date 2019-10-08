# AI-Electricity-Usage-Predictor
This project is a artificial intelligence model used for predicting electricity usage based on the given dataset. The dataset used is called 'household_power_consumption' which contains 7 variables and 1 unique varaible used to compare the predicted data which is the result of this model and the actual manually predicted data.

## Requirements
This program usually needs Anaconda to work, or for more specific, the usual APIs for using Artificial Intelligence such as numpy, pandas, matplotlib and sklearn. However, due to new updates, new additions has been added which is a simple form of GUI. Although the GUI is very, very basic, this just prepares a simple foundation towards creating the GUI for the program. The API used for the GUI is PyQt5 and PyQt5-sip and was made with PyQt5-tools.

## Instructions
The main.py file is a terminal, you can predict new data with the command 'predict -n'. Make sure you edit or add data in the test.csv file in order to predict new data. If you want to test the prediction, which itself give the same result everytime, use the command 'predict -t' to predict test data. This terminal is still new and early so no other commands contain in this terminal to worry about. And make sure to unpack the zip file since that's the dataset. It was compressed due to it having large file size which is 127MB and the zip file is only about 21MB.

## Other Notes
- Thanks to Dr. Jason Brownlee for providing the link to the dataset used in this project.
- This project uses Python3.
- The dependencies are the following: numpy, scikit-learn, pandas and matplotlib. All of this dependencies are not manually downloaded but downloaded via anaconda.
