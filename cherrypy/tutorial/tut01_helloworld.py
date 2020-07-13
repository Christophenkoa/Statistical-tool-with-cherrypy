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
  


class HelloWorld:

    """ Sample request handler class. """

    # Expose the index method through the web. CherryPy will never
    # publish methods that don't have the exposed attribute set to True.
    #@cherrypy.expose
    #def index(self):
        # CherryPy will call this method for the root URI ("/") and send
        # its return value to the client. Because this is tutorial
        # lesson number 01, we'll just send something really simple.
        # How about...
        #return 'Hello world!'
    @cherrypy.expose
    def index(self):
        # Creating a sample of data 
        sample = [2.74, 1.23, 2.63, 2.22, 3, 1.98]
        # Function will automatically calculate 
        # it's mean and set it as xbar 
        return("Variance of sample set is % s" 
      %(statistics.variance(sample)))
    
    @cherrypy.expose
    def index(self):
        # creating a simple data - set 
        sample = [1, 2, 3, 4, 5] 
  
        # Prints standard deviation 
        # xbar is set to default value of 1 
        return("Standard Deviation of sample is % s " 
                % (statistics.stdev(sample)))

    @cherrypy.expose
    def index(self):
        x = np.array([[0, 3, 4], [1, 2, 4], [3, 4, 5]])
        # print("Shape of array:\n", np.shape(x)) 
        return("Covarinace matrix of x: \n", np.cov(x))
    
    @cherrypy.expose
    def Correlation(self):
        a = [1,4,6]
        b = [1,2,3] 
        #Correlation
        corrmat = np.corrcoef(a,b)
        print("The correlation coeficient is: "+ corrmat)

tutconf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(HelloWorld(), config=tutconf)
