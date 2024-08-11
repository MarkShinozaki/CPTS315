from logging import root
from typing import Text
import numpy as np
import pandas as pd
import itertools as it


def main():
    f = open("output.txt","w")
    data = Read_data()
    support = 100
    
    #--- Starting Apiori 1 --- #
    print("$ A-piori - 1 Has Started ")
    p1Data = Apiori1(data,support)
    print("$ A-piori - 1 Has Finished ")
     #--- Apiori 1 Has Finished --- #
     
    #--- Sorting 1 Has Started --- # 
    print("$ Sorting - Has Started")
    Sorting = sort(p1Data, support)
    print("$ Sorting - Has Finished")
    #--- Sorting 1 Has Finished --- # 
    
    #--- Starting Apiori 2 --- #
    print("$ A-piori - 2 Has Started ")
    p2Data = Apiori2(data,p1Data, support)
    print("$ A-piori - 2 Has Finished ")
     #--- Apiori 2 Has Finished --- #
    
     #--- Starting Apiori 3 --- #
    print("$ A-piori - 3 Has Started ")
    p3Data = Apiori3(data, p1Data, support)
    print("$ A-piori - 3 Has Finished ")
     #--- Apiori 3 Has Finished --- #
    
    # Pairs Confidence
    pairs = PairConf(p1Data, p2Data)
    
    # Triples Confidence
    triples = tripleConfidence(p1Data, p2Data, p3Data)
    # Writing to Output Screen
    f.write("OUTPUT A: \n")
    FilePrint(pairs,f)
    
    f.write("OUTPUT B: \n")
    FilePrint(triples,f)
    
    f.close()


 # GET DATA FROM FILE ANALYZE

def Read_data():
    data_file = "browsing-data.txt"

    data_file_delimiter = ','

    largest_column_count = 0

    with open(data_file, 'r') as temp_f:
        lines = temp_f.readlines()
        for l in lines:
            column_count = len(l.split(data_file_delimiter)) + 1
            
            largest_column_count = column_count if largest_column_count < column_count else largest_column_count

    column_names = [i for i in range(0, largest_column_count)]

    df = pd.read_csv(data_file, header=None, delimiter=data_file_delimiter, names=column_names)
    newLine = [lines[i].strip().split() for i in range(len(lines))]
    return newLine

def sort(data, support):
    ans = {}
    for key, value in data.items():
        if value >= support:
            ans[key] = value
    return sorted(ans)

def Apiori1(data, support):
    counter = {}
    finalCounter = {}
    for row in data:
        for i in row:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] +=  1
    
    for key, value in counter.items():
        if value >= support:
            finalCounter[key] = value
        
    return finalCounter

            

def Apiori2(data, p1data, support):
    counter = {}
    finalCounter = {}
    combos = list(it.combinations(p1data.keys(), 2)) 

    for key in combos:
        counter[key] = 0

                
    for row in data:
        rcombo = list(it.combinations(row, 2))
        for key in rcombo:
            if (key in counter.keys()):
                counter[key] += 1
            elif (key[::-1] in counter.keys()):
                counter[key[::-1]] += 1



    for key, value in counter.items():
        if value >= support:
            finalCounter[key] = value


    return finalCounter
            

def Apiori3(data, p1data, support):
    counter = {}
    finalCounter = {}
    combos = list(it.combinations(p1data.keys(), 3)) 

    for key in combos:
        counter[key] = 0

                
    for row in data:
        rcombo = list(it.combinations(row, 3))
        for key in rcombo:
            a = key[0]
            b = key[1]
            c = key[2]
            keycombo = [(a,b,c), (a,c,b), (b,a,c), (b,c,a), (c,a,b), (c,b,a)]
            for kc in keycombo:
                if (kc in counter.keys()):
                    counter[kc] += 1



    for key, value in counter.items():
        if value >= support:
            finalCounter[key] = value


    return finalCounter


def FilePrint(data, f):

    for key, value in data.items():
        f.write("%s,%s\n"  % (key,value))
    f.write("\n")

def PairConf(p1, p2):
    confidence = {}
    for key in p2.keys():
        confidence[(key[0], key[1])] =  p2[key] / p1[key[0]]

        confidence[(key[1], key[0])] =  p2[key] / p1[key[1]]
    return dict(sorted(confidence.items(), key = lambda x:x[1],reverse=True)[:5])

def tripleConfidence(p1, p2, p3):
    confidence = {}
    for key in p3.keys():
        var = p2.get((key[0], key[2])) or p2.get((key[2], key[0]))
        confidence[(key[0],key[2],key[1])] = p3[key] / var

        var = p2.get((key[0], key[1])) or p2.get((key[1], key[0]))
        confidence[(key[0],key[1],key[2])] = p3[key] / var

        var = p2.get((key[1], key[2])) or p2.get((key[2], key[1]))
        confidence[(key[1],key[2],key[0])] = p3[key] / var
    return dict(sorted(confidence.items(), key = lambda x:x[1],reverse=True)[:5])



if __name__ == "__main__":
    main()