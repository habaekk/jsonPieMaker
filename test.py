# iter = range(365)


# data = {
#     "2020": {
#         "12": {
#             "1": {"lunDay": "00", "moonPhase": None},
#             "2": {"lunDay": "00", "moonPhase": None}
#         },
#         "11": {

#         }
#     },
#     "2021": {}
# }

# dic = {}
# dic1 = {}
# dic2 = {"12": {1, 2, 3}, "11": {1, 2, 3}}
# dic3 = {"1": {"lunDay": "00", "moonPhase": None}, "1": {"lunDay": "00", "moonPhase": None}, "1": {"lunDay": "00", "moonPhase": None}}


dic = {}
for y in range(2020, 2024):
    dic1 = {}
    for m in range(1, 3):
        dic2 = {}
        for d in range(5):
            lunDay = 0
            moonPhase = 1
            dic2[str(d)] = {"lunDay": str(lunDay), "moonPhase": str(moonPhase)}
        dic1[str(m)] = dic2
    dic[str(y)] = dic1


{'2020': 
 {'1': 
  {'1': {'lunDay': '7', 'moonPhase': '2'}, 
   '2': {'lunDay': '8', 'moonPhase': '0'}, 
   '3': {'lunDay': '9', 'moonPhase': '0'}, 
   '4': {'lunDay': '10', 'moonPhase': '0'}, 
   '5': {'lunDay': '11', 'moonPhase': '0'}, 
   '6': {'lunDay': '12', 'moonPhase': '0'}, 
   '7': {'lunDay': '13', 'moonPhase': '0'}, 
   '8': {'lunDay': '14', 'moonPhase': '0'}, 
   '9': {'lunDay': '15', 'moonPhase': '3'}}}}