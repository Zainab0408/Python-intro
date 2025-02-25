def test(lst):
    result = {}
    for item in lst:
            result[item[0]]=item[1:]
    return result
Students=[[1,"Zainab","IX"], [2,"Zara","VI"],[3,"Fatima","VII"],[4,"Sarah","VIII"],[5,"Zehra","VIII"]]
print(test(Students))