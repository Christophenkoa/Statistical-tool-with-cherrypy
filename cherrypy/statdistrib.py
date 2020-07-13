import statistics # Importing Statistics module 
import numpy as np # use of numpy.cov

class statdistrib:
    def variance():
        sample = [2.74, 1.23, 2.63, 2.22, 3, 1.98] # Creating a sample of data 
        print("Variance of sample set is % s"
	%(statistics.variance(sample))) # Prints variance of the sample set 
    # Function will automatically calculate 
    # it's mean and set it as xbar 
     
     def covariance():
         x = np.array([[0, 3, 4], [1, 2, 4], [3, 4, 5]]) 
         print("Shape of array:\n", np.shape(x)) 
         print("Covarinace matrix of x:\n", np.cov(x))
    
    def stdev():
        # creating a simple data - set 
        sample = [1, 2, 3, 4, 5] 
        # Prints standard deviation 
        # xbar is set to default value of 1 
        print("Standard Deviation of sample is % s "
				% (statistics.stdev(sample))) 
