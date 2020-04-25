import numpy as np
import pandas as pd
import math

data = pd.read_csv("mushrooms.csv")
#data=data.dropna() #removing missing values
print(data.shape)
# >> (8124, 23)

cls, cls_cnt = np.unique(
	data["class"].values, return_counts=True
)
print(cls)
print(cls_cnt)
# >> ['e' 'p']
# >> [4208 3916]

print("Mushroom cap shape classification:")
capshape, capshape_cnt = np.unique(
	data["cap-shape"].values, return_counts=True
)
capshape_pers = capshape_cnt / data.shape[0]
print("Capshapes statistics:")
for i in range(capshape.size):
	print (str(capshape[i]) + " -> " + str(round(capshape_pers[i]*100,int(math.log(capshape_pers[i])/math.log(0.1)))) + "%")
# >> Mushroom cap shape classification:
# >> b -> 5.6%
# >> c -> 0.49%
# >> f -> 39.0%
# >> k -> 10.0%
# >> s -> 0.39%
# >> x -> 45.0%




