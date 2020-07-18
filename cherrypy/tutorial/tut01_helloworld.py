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


    def index(self) :
        output = '''
        <!doctype html>
        <html lang="fr">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Titre de la page</title>
            </head>
            <body style="background-color:blue; color : white; text-align:center;">
                <div style="font-family: courier;">
                    <div style="width:80%; margin :auto;">
                        <h1 style="margin : 50px; font-family: verdana;border: 2px solid powderblue;padding: 30px;"> Welcome to our Home page </h1>
                        <h2 style="margin : 30px"> Functions Implemented :  </h2>


                        <a href="variance"> <h4><font color = "white">Variance</font></h4> </a>
                        <a href="standardDeviation"> <h4><font color = "white">Standard deviation</font></h4> </a>
                        <a href="covariance"> <h4><font color = "white">Covariance</font></h4> </a>
                        <a href="correlation"> <h4><font color = "white">Correlation</font></h4> </a>


                    </div>
                    <style>
                        .footer {
                        position: fixed;
                        left: 0;
                        bottom: 0;
                        width: 100%;
                        background-color: green;
                        color: white;
                        text-align: center;
                        padding: 15px;
                        }
                    </style>

                    <div class="footer">
                        <p>Statistical tools : Cloud computing assignment</p>
                    </div>
                </div>
            </body>
        </html>
        '''
        return output
    index.exposed = True


    @cherrypy.expose
    def variance(self):
        # Creating a sample of data 
        sample = [2.74, 1.23, 2.63, 2.22, 3, 1.98]
        # Function will automatically calculate 
        # it's mean and set it as xbar 
        return("<h2>Variance of sample set is : </h2> <h3> %s </h3>" 
      %(statistics.variance(sample)))
    
    @cherrypy.expose
    def standardDeviation(self):
        # creating a simple data - set 
        sample = [1, 2, 3, 4, 5] 
  
        # Prints standard deviation 
        # xbar is set to default value of 1
        # 
        standardDeviation = (statistics.stdev(sample))

        return("<h2>standard deviation is: </h2> <h3>%s</h3>"  % standardDeviation)

    @cherrypy.expose
    def covariance(self):
  
        # list  1 
        a = [2, 3, 2.7, 3.2, 4.1] 
        
        # list 2 
        b = [10, 14, 12, 15, 20] 
        
        # storing average of a 
        av_a = sum(a)/len(a) 
        
        # storing average of b 
        av_b = sum(b)/len(b) 
        
        # making series from list a 
        a = pd.Series(a) 
        
        # making series from list b 
        b = pd.Series(b) 
            
        # covariance through pandas method 
        covar = a.cov(b) 
        return("<h2>Covariance is:</h2> <h3>%s</h3>"  % covar)

    
    @cherrypy.expose
    def correlation(self):
        a = [1, 4, 6]
        b = [1, 2, 3] 
        #Correlation
        correlation = np.corrcoef(a,b)
        return("<h2>The correlation coefficient is:</h2> <h3>%s</h3>" % correlation[0,1])

tutconf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(HelloWorld(), config=tutconf)