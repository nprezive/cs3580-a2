#!/usr/bin/python3
from collections import defaultdict
import pprint

def getRaceDict():
    return {"Hispanic":0,"White":0,"Black":0,"Native":0,"Asian":0,"Pacific":0}

def mk_int(s):
    return int(s) if s else 0

def mk_float(s):
    return float(s) if s else 0

#Part 1
def part1():
    stateDict = defaultdict(lambda: getRaceDict())
    with open('/home/nprezive/School/CS3580/a2/acs2015_census_tract_data.csv') as f:
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
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(stateDict)

    print("\n\n\n")

    stateDict2 = defaultdict(lambda: getRaceDict())
    with open('/home/nprezive/School/CS3580/a2/acs2015_county_data.csv') as f:
        next(f)
        for line in f:
            lineList = line.split(",")
            stateDict2[lineList[1]]["Hispanic"] += (mk_int(lineList[3]) * mk_float(lineList[6]) / 100)
            stateDict2[lineList[1]]["White"] += (mk_int(lineList[3]) * mk_float(lineList[7]) / 100)   
            stateDict2[lineList[1]]["Black"] += (mk_int(lineList[3]) * mk_float(lineList[8]) / 100)          
            stateDict2[lineList[1]]["Native"] += (mk_int(lineList[3]) * mk_float(lineList[9]) / 100)           
            stateDict2[lineList[1]]["Asian"] += (mk_int(lineList[3]) * mk_float(lineList[10]) / 100)           
            stateDict2[lineList[1]]["Pacific"] += (mk_int(lineList[3]) * mk_float(lineList[11]) / 100)
    stateDict2.pop('District of Columbia')
    stateDict2.pop('Puerto Rico')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(stateDict2)    

def test1():
    stateDict = defaultdict(lambda: getRaceDict())
    with open('/home/nprezive/School/CS3580/a2/acs2015_census_tract_data.csv') as f:
        next(f)
        for line in f:
            lineList = line.split(",")
            print("{0}, {1}, {2}".format(lineList[1], lineList[3], lineList[6]))
            stateDict[lineList[1]]['Hispanic'] += (int(lineList[3]) * float(lineList[6]) / 100)




#Run assignment
print("Name: Noah Preszler")
part1()