

def sortPeople(names, heights):

    for i in range(len(names) -1):
        for j in range(len(heights)-i-1):
            if heights[j] > heights[j + i]:
                names[j], names[j+1], names[j+1], names[j]
                heights[j], heights[j+1], heights[j+1], heights[j]
    
    return names

names = ["Mary","John","Emma"]
heights = [180,165,170]
print(sortPeople(names, heights))
