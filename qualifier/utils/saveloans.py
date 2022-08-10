import questionary
import csv
from pathlib import Path
import os.path

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    #if there are no loans exit with message.
    if 0 >= len(qualifying_loans):
        print("We're sorry, there are no qualifying loans.")
        print("Thank you, exiting program.")
        quit()
    #would you like to save as a yes/no queston.
    save_file = questionary.confirm("Would you like to save the qualifying loans as a csv file?").ask()
    #if no thakn user and exit.
    if save_file == False:
        print("Thank you, exiting program.")
        quit()
    #if yes ask the user for a file path.
    elif save_file == True:
        file_path = questionary.text("Please enter a file path for the CSV file:").ask()
        file_path = Path(file_path)
        #if the file path doesnt exist, try again.
        if not file_path.exists():
            print("Sorry no file path exists, please try again.")
            file_path = questionary.text("Please enter a file path for the CSV file:").ask()
        #create file path for the csv
        csvpath = os.path.join(file_path, "qualifying_loans.csv")
        #header for the CSV, same format as daily_rate_sheet.csv
        header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]    
        #create csv using data from qualifying_loans
        with open(csvpath, 'w', newline= '') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)
            for row in qualifying_loans:
                csvwriter.writerow(row)
        print("Saving qualifying loans to a CSV file...")
        return csvfile