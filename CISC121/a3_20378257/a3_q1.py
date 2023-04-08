import csv
import functions3
'''
CISC-121 2023W
Name: Dmytro Zaichenko
Student Number: 20378257
Email: 22bh17@queensu.ca
Date: 2023-03-07
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''

def menu():
    """
    -------------------------------------------------------
    Creates a menu for user to choose between functions they want to use.
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        Information from function they want.
    -------------------------------------------------------
    """

    # Creates a readable table from the csv file.
    csvData = []
    with open('electionsData.csv', 'r', encoding='utf-8-sig') as data:
        for line in csv.DictReader(data):
            csvData.append(line)
    
    # Loop that repeats as long as the user wants.
    check = "Y"
    while check == "Y":

        # Gives the user information to choose from.
        print("1. Display information for a district")

        print("2. Show districts by the given province")

        print('3. Find the maximum value')
        
        print('4. Find the minimum value')
        
        print('5. Total number of ballots by dictionaries')
        
        print("6. Sort dictionary")

        print('7. Percentage of voter turnout')
        
        option = int(input("Enter the corresponding number to your needs: "))
        
        # Runs the corresponding function based on the number the user typed.
        if option == 1:
            district = input("Enter the district number: ")
            functions3.displayInfo(csvData, district)
        
        if option == 2:
            province = input("Enter the province: ")
            print(functions3.uniqueDistricts(csvData, province))
        
        if option == 3:
            value = input('Enter the key value: ')
            outputValue, outputDistrict = functions3.findMax(csvData, value)[0], functions3.findMax(csvData, value)[1]
            print('Max', str(value)+":", outputDistrict, outputValue)

        if option == 4:
            value = input('Enter the key value: ')
            outputValue, outputDistrict = functions3.findMin(csvData, value)[0], functions3.findMin(csvData, value)[1]
            print('Min', str(value)+":", outputDistrict, outputValue)

        if option == 5:
            tempDict = sorted(functions3.totalVotes(csvData), key=lambda x: x['Province'])

            for k in range(len(tempDict)):
                print((list(tempDict[k].values())[0])+":",list(tempDict[k].values())[1])

        if option == 6:
            value = input('Enter the key value: ')
            functions3.selectionSort(csvData, value)
            print('Sorted by', "'"+value+"'")

        if option == 7:
            # Initializing and sorting the data for binary search
            tempList = []
            functions3.selectionSort(csvData, 'Electoral District Number')

            # Gathers the electoral district numbers into a list to be searched.
            for k in range(len(csvData)):
                tempList.append(int(csvData[k]['Electoral District Number']))
            
            target = int(input("Enter the target district number: "))
            
            try:
                print('Found:',str(functions3.binarySearch(0, len(tempList)-1, tempList, target, csvData)))
            
            except:
                print('Item was not found')
        
        # Lets the code repeat.
        check = input("Would you like to pick another menu number? (Y/N): ").capitalize()

menu()