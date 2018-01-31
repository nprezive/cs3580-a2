#!/usr/bin/python3
from collections import defaultdict
import operator
import pprint

def getRaceDict():
    return {"Hispanic":0,"White":0,"Black":0,"Native":0,"Asian":0,"Pacific":0}

def mk_int(s):
    return int(s) if s else 0

def mk_float(s):
    return float(s) if s else 0

#Part 1
def part1():
    #Make a dictionary of states and their race populations
    stateDict = defaultdict(lambda: getRaceDict())
    with open('acs2015_census_tract_data.csv') as f:
        next(f)
        for line in f:
            lineList = line.split(",")
            stateDict[lineList[1]]["Hispanic"] += (mk_int(lineList[3]) * mk_float(lineList[6]) / 100)
            stateDict[lineList[1]]["White"] += (mk_int(lineList[3]) * mk_float(lineList[7]) / 100)   
            stateDict[lineList[1]]["Black"] += (mk_int(lineList[3]) * mk_float(lineList[8]) / 100)          
            stateDict[lineList[1]]["Native"] += (mk_int(lineList[3]) * mk_float(lineList[9]) / 100)           
            stateDict[lineList[1]]["Asian"] += (mk_int(lineList[3]) * mk_float(lineList[10]) / 100)           
            stateDict[lineList[1]]["Pacific"] += (mk_int(lineList[3]) * mk_float(lineList[11]) / 100)
    stateDict.pop('District of Columbia')
    stateDict.pop('Puerto Rico')

    #Map dictionary to a dictionary of states and their race proportions
    stateDict2 = dict()
    for k, v in stateDict.items():
        stateTotalPop = sum(v.values())
        stateDict2[k] = {'Hispanic': ( v['Hispanic'] / stateTotalPop ),
                         'White': ( v['White'] / stateTotalPop ), 
                         'Black': ( v['Black'] / stateTotalPop ),
                         'Native': ( v['Native'] / stateTotalPop ),
                         'Asian': ( v['Asian'] / stateTotalPop ),
                         'Pacific': ( v['Pacific'] / stateTotalPop )}

    #Asian
    stateAsianProp = dict()
    for k, v in stateDict2.items():
        stateAsianProp[k] = v['Asian']
    sortedAsian = sorted(stateAsianProp.items(), 
                            key=operator.itemgetter(1), 
                            reverse=True)
    print("Part 1:")
    print("Asian: " + str(sortedAsian[0][0]))

    #Black
    stateBlackProp = dict()
    for k, v in stateDict2.items():
        stateBlackProp[k] = v['Black']
    sortedBlack = sorted(stateBlackProp.items(), 
                            key=operator.itemgetter(1), 
                            reverse=True)
    print("Black: " + str(sortedBlack[0][0]))

    #Hispanic
    stateHispanicProp = dict()
    for k, v in stateDict2.items():
        stateHispanicProp[k] = v['Hispanic']
    sortedHispanic = sorted(stateHispanicProp.items(), 
                            key=operator.itemgetter(1), 
                            reverse=True)
    print("Hispanic: " + str(sortedHispanic[0][0]))

    #Native
    stateNativeProp = dict()
    for k, v in stateDict2.items():
        stateNativeProp[k] = v['Native']
    sortedNative = sorted(stateNativeProp.items(), 
                            key=operator.itemgetter(1), 
                            reverse=True)
    print("Native: " + str(sortedNative[0][0]))

    #Pacific
    statePacificProp = dict()
    for k, v in stateDict2.items():
        statePacificProp[k] = v['Pacific']
    sortedPacific = sorted(statePacificProp.items(), 
                            key=operator.itemgetter(1), 
                            reverse=True)
    print("Pacific: " + str(sortedPacific[0][0]))

    #White
    stateWhiteProp = dict()
    for k, v in stateDict2.items():
        stateWhiteProp[k] = v['White']
    sortedWhite = sorted(stateWhiteProp.items(), 
                            key=operator.itemgetter(1), 
                            reverse=True)
    print("White: " + str(sortedWhite[0][0]))






#Run assignment
print("Name: Noah Preszler\n")
part1()