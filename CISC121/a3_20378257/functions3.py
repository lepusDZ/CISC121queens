'''
CISC-121 2023W
Name: Dmytro Zaichenko
Student Number: 20378257
Email: 22bh17@queensu.ca
Date: 2023-03-07
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''

def displayInfo(csvData, num):
    """
    -------------------------------------------------------
    Display information for an electoral district.
    -------------------------------------------------------
    Parameters:
        Data set and the electoral district number.
    Returns:
        All information from the electoral district.
    -------------------------------------------------------
    """
    # Turns the data set into a readable list.
    for k in range(len(csvData)):
        tempList = list(csvData[k].values())
        if num == tempList[2]:

            # Gathers each piece of info from the dictionary.
            pollingStations = tempList[5]
            validBallots = tempList[6]
            totalBallots = tempList[10]
            voterTurnout = tempList[11]

            # Prints the info.
            print('Polling Stations:', str(pollingStations))
            print('Valid Ballots:', str(validBallots))
            print('Total Ballots Cast:', str(totalBallots))
            print('Voter Turnout:', str(voterTurnout))

def uniqueDistricts(csvData, name):
    """
    -------------------------------------------------------
    Displays unique districts from a province.
    -------------------------------------------------------
    Parameters:
        Data set and the name of the province.
    Returns:
        Unique districts.
    -------------------------------------------------------
    """
    # Initialize
    districts = []
    
    # Makes the data set readable.
    for k in range(len(csvData)):
        tempList = list(csvData[k].values())
        
        # Adds the district names to a list.
        if name in tempList[0]:
            districts.append(tempList[1])
    
    return districts

def findMax(csvData, name):
    """
    -------------------------------------------------------
    Find the maximum value of any of the key values.
    -------------------------------------------------------
    Parameters:
        Data set and the key value.
    Returns:
        The max number.
    -------------------------------------------------------
    """
    # Initialize
    max_value = 0

    # Finds the max number.
    for i in csvData:      
        if int(i[name]) > max_value:
            max_value = int(i[name])
            districtName = i['Electoral District Name']

    return max_value, districtName

def findMin(csvData, name):
    """
    -------------------------------------------------------
    Find the minimum value of any of the key values.
    -------------------------------------------------------
    Parameters:
        Data set and the key value.
    Returns:
        The minimum number.
    -------------------------------------------------------
    """  
    min_value = findMax(csvData,name)[0]

    # Finds the minimum value.
    for i in csvData:      
        if int(i[name]) < min_value:
            min_value = int(i[name])
            districtName = i['Electoral District Name']

    return min_value, districtName

def totalVotes(csvData):
    """
    -------------------------------------------------------
    Finds number of ballots in every territory.
    -------------------------------------------------------
    Parameters:
        Data set.
    Returns:
        The total number of ballots in every Canadian territory.
    -------------------------------------------------------
    """
    # Initialize
    finalList = []
    i = 0
    provinceName = 'Newfoundland and Labrador'
    total = 0
    
    # Creates a list from the info in the data set.
    while (i < (len(csvData))):
        tempList = list(csvData[i].values())
        
        # With every cycle checks if the province from current line is the same as it was
        if tempList[0] == provinceName:
            tempName = provinceName
            total += int(tempList[10])
            i += 1
         
        # If the province changes, it adds the previous one to the dictionary as a key and total value of ballots from
        # it as a corresponding value
        else:
            tempDict = {}
            tempDict['Province'] = str(tempName)
            tempDict['Total Ballots'] = str(total)
            
            finalList.append(tempDict)

            provinceName = tempList[0]
            total = 0
        
        # When the list reaches the last line, it also adds it to the dictionary
        if i == len(csvData):
            tempDict = {}
            tempDict['Province'] = str(tempName)
            tempDict['Total Ballots'] = str(total)
            
            finalList.append(tempDict)
    
    return finalList

def selectionSort(csvData,key):
    """
    -------------------------------------------------------
    Sorts a supplied list of dictionaries from a key.
    -------------------------------------------------------
    Parameters:
        Data set and key.
    Returns:
        Sorted list of dictionaries.
    -------------------------------------------------------
    """
    n = len(csvData)
    
    # Selection sort.
    for i in range (n-1):
        current_min = i

        for j in range(i+1,n):
            
            # Redefines the current minimum if needed.
            if csvData[j][key] < csvData[current_min][key]:
                current_min = j
            
            # Swaps 2 values if they aren't in the correct spot.
            if current_min != i:
                csvData[i], csvData[current_min] = csvData[current_min], csvData[i]

def binarySearch(low, high, templist, target, csvData):
    """
    -------------------------------------------------------
    Searches through a sorted list of numbers to find the target.
    -------------------------------------------------------
    Parameters:
        Minimum, maximum, the sorted list, the target number, and the original data set.
    Returns:
        Percentage of the target number.
    -------------------------------------------------------
    """
    mid = ((high-low)//2) + low
    
    # Checks if the middle number is the target value. Base case.
    if templist[mid] == int(target):
        tempList = list(csvData[mid].values())

        # Returns the percentage.
        return tempList[11]
    
    # Checks if the middle is above or below the target and goes through the
    # function again recursively.
    if int(templist[mid]) < target:
        return binarySearch(mid, high, templist, target, csvData)
    
    if int(templist[mid]) > int(target):
        return binarySearch(low, mid, templist, target, csvData)
    
    else:
        result = 'Item was not found'
        return result