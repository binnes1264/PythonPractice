#n01445323 - Bethany Innes

import numpy as np
from scipy.stats import iqr

def printData(week5_data):
    print(week5_data[:5])
    print('Shape of the Data:', week5_data.shape,"\n")
    

def descriptiveStats(dataToCalc):
    print(f'Mean: {dataToCalc.mean():.2f}')
    print(f'Median: {np.median(dataToCalc):.2f}')
    print(f'Standard Deviation: {np.std(dataToCalc):.2f}')
    print(f'Interquartile Range: {iqr(dataToCalc):.2f}')
    print('\n')
    
    
def main():
    #opening file and reading it in 
    week5_data = np.genfromtxt('brfss-cdc.csv', delimiter=',', skip_header=1)
    
    #Displaying original data and shape
    print('First five rows of the Data:')
    printData(week5_data)
    
    
    #creation of weight change data
    weightyrago = week5_data[ :,3:4]
    currentweight = week5_data[ :, 2:3]
    change = currentweight - weightyrago
    week5_data = np.hstack((week5_data, change)) 
    
    #displaying weight change stats
    print('Descriptive Statistics for Weight Change Data:')
    descriptiveStats(change)
    
    #displaying weight change data
    print('First Five Rows of the Data with Weight Changes:')
    printData(week5_data)   
    
    
    #creation of male data
    male_data = week5_data[week5_data[:,5]==1]
    
    #displaying male stats           
    print('First Five Rows of the Data relevant to Males:')       
    printData(male_data)
    
    #displaying male data
    print('Descriptive Statistics for Data relevant to Males:')
    descriptiveStats(male_data)             
    
         
    #creation of female data
    female_data = week5_data[week5_data[:,5]==2]
    
    #displaying female stats           
    print('First Five Rows of the Data relevant to Females:')       
    printData(female_data)
    
    #displaying female data
    print('Descriptive Statistics for Data relevant to Females:')
    descriptiveStats(female_data)             
      
    
main()