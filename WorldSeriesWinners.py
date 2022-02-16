#8) WorldSeriesWinners.py -  This file - WorldSeriesWinners.txt Download WorldSeriesWinners.txt contains a chronological list of the World Series’ winning teams 
# from 1903 through 2009. The first line in the file is the name of the team that won in 1903, and the last line is the name of the team that won in 2009. 
# (Note the World Series was not played in 1904 or 1994. There are entries in the file indicating this.) Write a program that reads this file and creates a dictionary 
# in which the keys are the names of the teams, and each key’s associated value is the number of times the team has won the World Series. 

# Create another dictionary in which the keys are the years, and each key’s associated value is the name of the team that won that year.The program should prompt 
# the user for a year in the range of 1903 through 2009. It should then display the name of the team that won the World Series that year, and the number of times 
# that team has won the World Series.

def main():
    #Open a file named WorldSeriesWinners.txt
    infile = open("WorldSeriesWinners.txt", "r")

    SeriesDict = {}
    
    YearDict = {}
    year = 1902

    #Read the file's contents and create win count dictionary
    for winner in infile:
        winner = winner.rstrip("\n")

        
        year += 1
        if year == 1904 or year == 1994:
            YearDict[year] = "Not Played"
            year += 1
            YearDict[year] = winner
        else:
            YearDict[year] = winner

        if winner in SeriesDict:
            SeriesDict[winner] += 1
        else:
            SeriesDict[winner] = 1

    print(SeriesDict)
    print(YearDict)

    #Close the File
    infile.close()

main()
