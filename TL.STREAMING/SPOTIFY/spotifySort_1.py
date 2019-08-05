# Spotify Sort by Pinguin | Ver 1.0
# Current Config for Data looking like:
# user@domain.com:password  ||  Premium for Family, US

import argparse

# Only configure if you have a different data format
# Current data format: user@domain.com:password  ||  Premium for Family, US
captureDelim = ''
countryDelim = ''
listFocus = []

def main():
    global captureDelim
    global countryDelim
    global listFocus

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', type = int, default = 0, required = True, help = "the mode to use (0 = file, 1 = folder)")
    parser.add_argument('-i', '--input', required = True, help = "the file or folder name or path to use as input")
    parser.add_argument('-o', '--output', default = "output.txt", help = "the output's filename")
    parser.add_argument('-cad', '--capture-delim', default = "  ||  ", help = "")
    parser.add_argument('-cod', '--country-delim', default = ", ", help = "")
    parser.add_argument('-f', '--focus', nargs = "+", default = ['US', 'Premium', 'Family', 'Owner'], help = "")
    args = parser.parse_args()

    mode = args.mode
    input = args.input
    output = args.output
    captureDelim = args.capture_delim
    countryDelim = args.country_delim
    listFocus = args.focus

    mainPrint(mode, input, output, captureDelim, countryDelim, listFocus)

    if mode == 0:
        targetLists = openSortByCountry(input)
    elif mode == 1:
        targetLists = openSortByCountry(input)

    countriesList = targetLists[0]
    unknownList = targetLists[1]
    totalAccounts = targetLists[2]
    print(f"\n Unknown: {len(unknownList)}/{totalAccounts}")

    lootList = []
    otherList = []

    for code in countriesList[0]:
        codeIndex = int(code[1])
        codeStr = code[0]
        accountList = countriesList[codeIndex]
        print(f" {codeStr} accounts: {len(accountList)}/{totalAccounts}")
        #print(accountList
        focusList = []
        otherAccounts = []
        for account in countriesList[codeIndex]:
            #print(account
            isFocus = False
            accountType = str(account[1]).split(' ')
            focusPoints = 0
            for keyword in accountType:
                if keyword in listFocus:
                    isFocus = True
                    focusPoints += 1
            if isFocus:
                focusList.append([focusPoints, account])
            else:
                otherAccounts.append(account)

        focusList = sorted(focusList, key=lambda x: x[0], reverse=True)
        otherAccounts = sorted(otherAccounts, key=lambda x: x[1], reverse=True)
        sortedList = []
        #print("Focus Accounts: "
        for account in focusList:
            sortedList.append(account[1])
        #print("Other Accounts: "
        for account in otherAccounts:
            sortedList.append(account)
        if codeStr in listFocus:
            lootList = sortedList
        else:
            otherList.append([codeStr, sortedList])
    save(output, "==========\nSorted Data by Pinguin\n==========\n-----[Focused Loot]-----\n", writeMode='w')
    for data in lootList:
        saveStr = data[0] + " - [" + data[1] + "]\n"
        save(output, saveStr)
    for data in otherList:
        save(output, "\n-----[" + str(data[0]) + "]-----\n")
        for d in data[1]:
            save(output, d[0] + " - [" + d[1] + "]\n")

    print("\n DONE!\n")

def save(fileName, dataToWrite, writeMode='a'):
    with open(fileName, writeMode) as f:
        f.write(dataToWrite)

def openSortByCountry(filename):
    masterList = [[]]  # List that contains sub lists, sub list will be for each country code
    unknownList = []  # list of unknown accounts we have data for
    countriesFound = 0
    accountsFound = 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            data = returnData(line)
            if data[0]:
                # data[1] = combo
                # data[2] = accountType
                # data[3] = countryCode
                #print(data
                if data[2] == '' or data[2] is False:
                    data[2] = 'Unknown'
                accountsFound += 1
                if data[3] == '' or data[3] is False:
                    unknownList.append([data[1],data[2]])
                elif str(masterList[0]).__contains__(data[3]) is False:
                    countriesFound += 1
                    #print("New Country Found: " + str(data[3]) + " | Countries Found: " + str(countriesFound)
                    masterList[0].append([data[3], countriesFound])
                    masterList.append([])
                    masterList[countriesFound].append([data[1], data[2]])
                else:
                    codeIndex = 0
                    cc = []
                    for code in masterList[0]:
                        if data[3] in code:
                            codeIndex = code[1]
                            cc = code
                    #print("============="
                    #print("code: " + str(cc) + " | index: " + str(codeIndex)
                    #print(line
                    #print("^ => " + str(data)
                    if codeIndex == 0:
                        unknownList.append([data[1], data[2]])
                    else:
                        masterList[codeIndex].append([data[1], data[2]])
    f.close()
    print(f" Countries: {countriesFound}")
    print(f" Accounts: {accountsFound}")
    return [masterList, unknownList, accountsFound]


def returnData(line):
    # Current Format: user@domain.com:pass  ||  Premium for Family, US

    if line.__contains__(captureDelim) and line.__contains__(countryDelim):
        combo = line.split(captureDelim)[0]
        accountType = line.split(captureDelim)[1]
        countryCode = accountType.split(countryDelim)[1]
        accountType = accountType.split(countryDelim)[0]
        return [True, combo, accountType, countryCode]
    else:
        return [False, 0, 0, 0]

def mainPrint(mode, input, output, captureDelim, countryDelim, listFocus):
    keywordList = ""
    for keyword in listFocus:
        keywordList += f"'{keyword}', "
    keywordList = keywordList[:-2]
    print(r"""
   _____             _    _____            _
  / ____|           | |  / ____|          | |
 | (___  _ __   ___ | |_| (___   ___  _ __| |_
  \___ \| '_ \ / _ \| __|\___ \ / _ \| '__| __|
  ____) | |_) | (_) | |_ ____) | (_) | |  | |_
 |_____/| .__/ \___/ \__|_____/ \___/|_|   \__|
        | |
        |_|
        """)
    print(f" Mode: '{mode}'")
    print(f" Input: '{input}'")
    print(f" Output: '{output}'")
    print(f" Capture Delimiter: '{captureDelim}'")
    print(f" Country Delimiter: '{countryDelim}'")
    print(f" Focus keywords: {keywordList}\n")


if __name__ == '__main__':
    main()
