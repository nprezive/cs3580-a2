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
    print("\tAsian: " + str(sortedAsian[0][0]))

    #Black
    stateBlackProp = dict()
    for k, v in stateDict2.items():
        stateBlackProp[k] = v['Black']
    sortedBlack = sorted(stateBlackProp.items(), 
                            key=operator.itemgetter(1), 
                            reverse=True)
    print("\tBlack: " + str(sortedBlack[0][0]))

    #Hispanic
    stateHispanicProp = dict()
    for k, v in stateDict2.items():
        stateHispanicProp[k] = v['Hispanic']
    sortedHispanic = sorted(stateHispanicProp.items(), 
                            key=operator.itemgetter(1), 
                            reverse=True)
    print("\tHispanic: " + str(sortedHispanic[0][0]))

    #Native
    stateNativeProp = dict()
    for k, v in stateDict2.items():
        stateNativeProp[k] = v['Native']
    sortedNative = sorted(stateNativeProp.items(), 
                            key=operator.itemgetter(1), 
                            reverse=True)
    print("\tNative: " + str(sortedNative[0][0]))

    #Pacific
    statePacificProp = dict()
    for k, v in stateDict2.items():
        statePacificProp[k] = v['Pacific']
    sortedPacific = sorted(statePacificProp.items(), 
                            key=operator.itemgetter(1), 
                            reverse=True)
    print("\tPacific: " + str(sortedPacific[0][0]))

    #White
    stateWhiteProp = dict()
    for k, v in stateDict2.items():
        stateWhiteProp[k] = v['White']
    sortedWhite = sorted(stateWhiteProp.items(), 
                            key=operator.itemgetter(1), 
                            reverse=True)
    print("\tWhite: " + str(sortedWhite[0][0]))

    print()

#Part 2
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
    print("\tHighest unemployment: " + str(statePopUnemployed[0][0]))
    
    #Sort list by % unemployed (A-Z)
    statePopUnemployed = sorted(statePopUnemployed, 
                                key=operator.itemgetter(1))
    print("\tLowest unemployment: " + str(statePopUnemployed[0][0]))
    print()

#Part 3
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
    
    print("Part 3: ({0} answers)".format(len(p3list)))
    for i, l in enumerate(p3list):
        print("\t#" + str(i+1))
        print("\tCensus tract: " + l[0])
        print("\tCounty: " + l[1])
        print("\tState: " + l[2])
        print("\tRaces: " + ', '.join(l[3]))
        print()

#Part 4
def part4():
    p4list = list()
    with open('acs2015_census_tract_data.csv') as f:
        next(f)
        for line in f:
            lineList = line.split(",")

            tract = lineList[0]
            county = lineList[2]
            state = lineList[1]

            totalPop = mk_float(lineList[3])
            women = mk_float(lineList[5])

            hispanic = mk_float(lineList[6])
            white = mk_float(lineList[7])
            black = mk_float(lineList[8])
            native = mk_float(lineList[9]) 
            asian = mk_float(lineList[10])
            pacific = mk_float(lineList[11])

            if( totalPop >= 10000 and women/totalPop > 0.57 ):
                races = list()
                if(hispanic > 1): races.append("Hispanic") 
                if(white > 1): races.append("White")
                if(black > 1): races.append("Black") 
                if(native > 1): races.append("Native")
                if(asian > 1): races.append("Asian") 
                if(pacific > 1): races.append("Pacific") 

                p4list.append([tract, county, state, races])
    
    print("Part 4: ({0} answers)".format(len(p4list)))
    for i, l in enumerate(p4list):
        print("\t#" + str(i+1))
        print("\tCensus tract: " + l[0])
        print("\tCounty: " + l[1])
        print("\tState: " + l[2])
        print("\tRaces: " + ', '.join(l[3]))
        print()

#Part 5
def part5():
    p5list = list()
    with open('acs2015_census_tract_data.csv') as f:
        next(f)
        for line in f:
            lineList = line.split(",")

            tract = lineList[0]
            county = lineList[2]
            state = lineList[1]

            totalPop = mk_float(lineList[3])
            women = mk_float(lineList[5])

            hispanic = mk_float(lineList[6])
            white = mk_float(lineList[7])
            black = mk_float(lineList[8])
            native = mk_float(lineList[9]) 
            asian = mk_float(lineList[10])
            pacific = mk_float(lineList[11])

            countRacesOver15 = 0
            if(hispanic >= 15): countRacesOver15 = countRacesOver15 + 1
            if(white >= 15): countRacesOver15 = countRacesOver15 + 1
            if(black >= 15): countRacesOver15 = countRacesOver15 + 1
            if(native >= 15): countRacesOver15 = countRacesOver15 + 1
            if(asian >= 15): countRacesOver15 = countRacesOver15 + 1
            if(pacific >= 15): countRacesOver15 = countRacesOver15 + 1

            if( countRacesOver15 >= 4 ):
                races = list()
                if(hispanic > 1): races.append("Hispanic") 
                if(white > 1): races.append("White")
                if(black > 1): races.append("Black") 
                if(native > 1): races.append("Native")
                if(asian > 1): races.append("Asian") 
                if(pacific > 1): races.append("Pacific") 

                p5list.append([tract, county, state, races])
    
    print("Part 5 ({0} answers):".format(len(p5list)))
    for i, l in enumerate(p5list):
        print("\t#" + str(i+1))
        print("\tCensus tract: " + l[0])
        print("\tCounty: " + l[1])
        print("\tState: " + l[2])
        print("\tRaces: " + ', '.join(l[3]))
        print()
    
    
#Run assignment
print("Name: Noah Preszler\n")
part1()
part2()
part3()
part4()
part5()


# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(p3list)