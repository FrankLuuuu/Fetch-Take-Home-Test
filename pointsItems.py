import sys
from csv import DictReader
# with filename = "transactions.csv"

# convert the given csv file into a list of dictionaries
def readCSV(inputFile):
    with open(inputFile, 'r') as csvFile:
        dict = DictReader(csvFile)
        transactions = list(dict)
    csvFile.close()

    # sort the list by the timestamps of the transactions
    transactions = sorted(transactions, key = lambda d: d['timestamp'])

    return transactions

# spend the points given and execute the transactions
def spendPoints(transactions, points):
    output = {}
    spent = False
    
    # loop through every transaction
    for i in range(len(transactions)):
        payer = transactions[i]["payer"]
        # add the payer to the output dictionary
        if payer not in output.keys():
            output[payer] = 0

        # spend the points until they are all spent
        # then execute all other transactions
        if not spent:
            points = points - int(transactions[i]['points'])
            if points > 0:
                continue
            output[payer] = output[payer] - points
            spent = True
        else:
            output[payer] = output[payer] + int(transactions[i]['points'])
    
    # return the payer balances
    return output

# prompt and read the input and print the resulting dictionary
if __name__ == "__main__":
    if int(sys.argv[1]) <= 0:
        print("please input the number greater than 0!")
        exit(0)
    transactionsList = readCSV("transactions.csv")
    result = spendPoints(transactionsList, int(sys.argv[1]))

    print(result)
