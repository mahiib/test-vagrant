#Getting user's weekly budget
budget=int(input())

#Dictionary to stores weekly costs of newspapers
newspaperCost={}


newspaperCost['TOI']=26
newspaperCost['Hindu']=20.5
newspaperCost['ET']=34
newspaperCost['BM']=10.5
newspaperCost['HT']=18

#Converting dictionary to list
newspaperCostList = list(newspaperCost)



#Stores all pairs of combinations
res = [(x, y) for idx, x in enumerate(newspaperCostList) for y in newspaperCostList[idx + 1: ]]

#Stores all possible combinations
possibleSubscriptions=[]

for (x,y) in res:
    if newspaperCost[x]+newspaperCost[y]<budget:
        possiblePairs='{"'+x+'"'+',"'+y+'"}'
        possibleSubscriptions.append(possiblePairs)

print(possibleSubscriptions)
