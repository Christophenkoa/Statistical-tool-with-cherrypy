"""
Tutorial - Hello World

The most basic (working) CherryPy application possible.
"""

import os.path

# Import CherryPy global namespace
import cherrypy

#import statsics
import statistics


# use of numpy.cov 
import numpy as np
import json
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
  


class HelloWorld:

    """ Sample request handler class. """

    # Expose the index method through the web. CherryPy will never
    # publish methods that don't have the exposed attribute set to True.



#To run the code, uncomment each method and run to test if it's works.
#First Uncomment the index method for the variance
#After test comment again and uncoment the next and so on.


    # @cherrypy.expose
    # def index(self):
    #     # Creating a sample of data 
    #     sample = [2.74, 1.23, 2.63, 2.22, 3, 1.98]
    #     # Function will automatically calculate 
    #     # it's mean and set it as xbar 
    #     return("Variance of sample set is % s" 
    #   %(statistics.variance(sample)))
    
    # @cherrypy.expose
    # def index(self):
    #     # creating a simple data - set 
    #     sample = [1, 2, 3, 4, 5] 
  
    #     # Prints standard deviation 
    #     # xbar is set to default value of 1 
    #     return("Standard Deviation of sample is % s " 
    #             % (statistics.stdev(sample)))

    # @cherrypy.expose
    # def index(self):
    #     a = [1, 4, 6]
    #     b = [1, 2, 3] 

    #     data = np.array([a, b])
    #     covMatrix = np.cov(data,bias=False)
    #     correlation = np.corrcoef(a,b)
    #     df = pd.DataFrame(covMatrix, index=['row_1', 'row_2'], columns=['col_1', 'col_2'])
    #     x = df.to_json(orient='index')
    #     return("Covariance matrix of x: \n", x)

    
    # @cherrypy.expose
    # def index(self):
    #     a = [1, 4, 6]
    #     b = [1, 2, 3] 
    #     #Correlation
    #     correlation = np.corrcoef(a,b)
    #     df = pd.DataFrame(correlation, index=['row_1', 'row_2'], columns=['col_1', 'col_2'])
    #     x = df.to_json(orient='index')

    #     return("The correlation coefficient is: ", x)

tutconf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(HelloWorld(), config=tutconf)
