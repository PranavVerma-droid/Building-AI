"""Edit the code so that it prints out the prices of multiple cabins in one go."""

# input values for three mökkis: 
#  - size [m^2], 
#  - size of the sauna [m^2], 
#  - distance to water [m], 
#  - number of indoor bathrooms, 
#  - proximity of neighbors [m]
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]

# coefficient values
c = [3000, 200 , -50, 5000, 100]

def predict(X, c):
    # write a loop that goes over the cabin data and for each cabin prints out 
    # the predicted price of the cabin you can assume that the number of inputs
    # and the number of coefficients are the same
    for i in X:   
        price =  i[0] * c[0] + i[1] * c[1] + i[2] * c[2] + i[3] * c[3] + i[4] * c[4]          
        print(price)

predict(X, c)
