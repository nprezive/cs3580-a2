#!/usr/bin/python3
from collections import defaultdict
import operator
import pprint


def mk_int(s):
    return int(s) if s else 0

def mk_float(s):
    try:
        return float(s)
    except ValueError:
        return 0


#Part 1
def part1():
    #Make a dictionary of states and their race populations
    stateDict = defaultdict(lambda: {"Hispanic":0,
                                     "White":0,
                                     "Black":0,
                                     "Native":0,
                                     "Asian":0,
                                     "Pacific":0})
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
    
    #Get rid of non-states
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

    print()


def part2():
    #Create a dict of the form {State}:[{Total population}, {Total unemployed}]
    statePopUnemployed = defaultdict(lambda: [0,0])
    with open('acs2015_census_tract_data.csv') as f:
        next(f)
        for line in f:
            lineList = line.split(",")
            statePopUnemployed[lineList[1]][0] += mk_int(lineList[3])
            statePopUnemployed[lineList[1]][1] += ( mk_int(lineList[3]) 
                                                    * mk_float(lineList[36]) 
                                                    / 100)

    #Get rid of non-states
    statePopUnemployed.pop('District of Columbia')
    statePopUnemployed.pop('Puerto Rico')

    #Map to dict of the form {State}:{% unemployed}
    for k,v in statePopUnemployed.items():
        statePopUnemployed[k] = ( v[1] / v[0] )
    
    #Sort dict by % unemployed (Z-A)
    statePopUnemployed = sorted(statePopUnemployed.items(), 
                                key=operator.itemgetter(1), 
                                reverse=True)
    print("Part 2:")
    print("Highest unemployment: " + str(statePopUnemployed[0][0]))
    
    #Sort list by % unemployed (A-Z)
    statePopUnemployed = sorted(statePopUnemployed, 
                                key=operator.itemgetter(1))
    print("Lowest unemployment: " + str(statePopUnemployed[0][0]))
    print()

def part3():
    p3list = list()
    with open('acs2015_census_tract_data.csv') as f:
        next(f)
        for line in f:
            lineList = line.split(",")
            tract = lineList[0]
            county = lineList[2]
            state = lineList[1]
            income = mk_float(lineList[13])
            poverty = mk_float(lineList[17])
            hispanic = mk_float(lineList[6])
            white = mk_float(lineList[7])
            black = mk_float(lineList[8])
            native = mk_float(lineList[9]) 
            asian = mk_float(lineList[10])
            pacific = mk_float(lineList[11])

            if(income >= 50000 and poverty > 50):
                races = list()
                if(hispanic > 1): races.append("Hispanic") 
                if(white > 1): races.append("White")
                if(black > 1): races.append("Black") 
                if(native > 1): races.append("Native")
                if(asian > 1): races.append("Asian") 
                if(pacific > 1): races.append("Pacific") 

                p3list.append([tract, county, state, races])
    
    print("Part 3:")
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(p3list)
    
    


#Run assignment
print("Name: Noah Preszler\n")
# part1()
# part2()
part3()