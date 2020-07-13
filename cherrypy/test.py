import numpy as np
results = [-14.82381293, -0.29423447, -13.56067979, -1.6288903, -0.31632439,
          0.53459687, -1.34069996, -1.61042692, -4.03220519, -0.24332097]
# calculate mean
m = sum(results) / len(results)

# calculate variance using a list comprehension
var_res = sum((xi - m) ** 2 for xi in results) / len(results)
print('the variance is: ' + str(var_res))
print('The standard deviation is: ' + np.std(results))