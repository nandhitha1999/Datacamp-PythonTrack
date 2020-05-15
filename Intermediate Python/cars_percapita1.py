# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
car_maniac = cars[cpc > 500]

# Print car_maniac
print(car_maniac)
