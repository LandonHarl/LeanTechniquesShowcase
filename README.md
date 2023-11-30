# Exact Change Calculator
This python program allows the user to enter a numeric value, 
which is then used in calculations to find how many of each denomination
is needed for exact change. There are no necessary installations for this project.

    EX: 15.50 is 1 $10, 1 $5 and 2 quarters.

## Usage
Clone the repository at `https://github.com/LandonHarl/LeanTechniquesShowcase` to your local machine.

Run the `"main.py"` class. When prompted, enter either a 1 for calculations, or 2 to quit:
    
    Enter 1 to do calculations, 2 to quit: 

For any input besides 1 or 2, an error will display for invalid input and the program
will stop. After entering 1, the user will receive a prompt to enter their value:

    Enter the amount to be calculated for change: 

If the user enters a non-numeric value, they receive the invalid input error. 
After entering a valid input, the number is sent to the `"change_calculator.py"` class.
The class takes the input, and gives back the exact change for each denomination.

## Testing
All testing is located within the `"exact_change_test.py"` class. Running this class will
run all tests within and show proper messages for running successfully.