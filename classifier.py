import numpy as np
import pandas as pd
import math

data = pd.read_csv("mushrooms.csv")
#data=data.dropna() #removing missing values
print(data.shape)
# >> (8124, 23)

def round_custom(num) :
	return round(num,int(math.log(num)/math.log(0.1))+2)

edibility, edibility_cnt = np.unique(
	data["class"].values, return_counts=True
)
print(edibility)
print(edibility_cnt)
# >> ['e' 'p']
# >> [4208 3916]

print("Mushroom cap shape classification:")
capshape, capshape_cnt = np.unique(
	data["cap-shape"].values, return_counts=True
)
capshape_pers = capshape_cnt / data.shape[0] * 100
for i in range(capshape.size):
	print (str(capshape[i]) + " -> " + str(round_custom(capshape_pers[i])) + "%")
# >> Mushroom cap shape classification:
# >> b -> 5.6%
# >> c -> 0.49%
# >> f -> 39.0%
# >> k -> 10.0%
# >> s -> 0.39%
# >> x -> 45.0%

print("Edible mushrooms color classification:")
data_edible = data.loc[data["class"]=="e"]
edible_color, edible_color_cnt = np.unique(
	data_edible["cap-color"].values, return_counts=True
)
edible_color_pers = edible_color_cnt / data_edible.shape[0] * 100
for i in range(edible_color.size):
	print (str(edible_color[i]) + " -> " + str(round_custom(edible_color_pers[i])) + "%")

max_pers = max(edible_color_pers)
max_color = edible_color[list(edible_color_pers).index(max_pers)]
min_pers = min(edible_color_pers)
min_color = edible_color[list(edible_color_pers).index(min_pers)]

print("Most common color is " + str(max_color) + " , amount is " + str(round_custom(max_pers)) + "%")
print("Less common color is " + str(min_color) + " , amount is " + str(round_custom(min_pers)) + "%")

# >> b -> 1.14%
# >> c -> 0.76%
# >> e -> 14.8%
# >> g -> 24.5%
# >> n -> 30.0%
# >> p -> 1.33%
# >> r -> 0.38%
# >> u -> 0.38%
# >> w -> 17.1%
# >> y -> 9.51%
# >> Most common color is n , amount is 30.0%
# >> Less common color is r , amount is 0.38%

# According to statistics, 30% of edible mushrooms are BROWN ('n')
# Also, only 0.38% of edible mushrooms are GREEN ('r')