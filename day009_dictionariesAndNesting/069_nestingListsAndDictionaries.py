travelLog = {
    "France": ["Paris", "Normandy"],
    "Italy": ["Rome", "Venice", "Florence"],
    "Japan": ["Tokyo", "Kyoto", "Osaka"],
    "USA": ["New York", "Los Angeles", "San Francisco"],
    "India": ["Delhi", "Mumbai", "Jaipur"],
    "Australia": ["Sydney", "Melbourne", "Brisbane"]
}

print(travelLog["France"][1])

nestedList = [1, 2, [3, 4]]

print(nestedList[2][0])

travelLogDetailed = {
    "France": {
        "times visited": 4,
        "places visited": ["Paris", "Normandy"]
    },
    "Italy": {
        "times visited": 3,
        "places visited": ["Rome", "Venice", "Florence"]
    },
    "Japan": {
        "times visited": 2,
        "places visited": ["Tokyo", "Kyoto", "Osaka"]
    },
    "USA": {
        "times visited": 5,
        "places visited": ["New York", "Los Angeles", "San Francisco"]
    },
    "India": {
        "times visited": 1,
        "places visited": ["Delhi", "Mumbai", "Jaipur"]
    }
}

print(travelLogDetailed["India"]["times visited"])
print(travelLogDetailed["India"]["places visited"])