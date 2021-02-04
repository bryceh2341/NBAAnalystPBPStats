import csv
import matplotlib.pyplot as plt 
import seaborn as sns; sns.set_theme(color_codes=True)
import numpy as np
#creates lists for the ratings and shot quality that will be used to graph
teamOffensiveRatings = []
teamOffShotQuality = []
teamDefensiveRatings = []
teamDefShotQuality = []

#opens CSV file for offense
with open('pbpstats 2019-2020 Team Data Offense.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    for row in csv_reader:
        #skips first line
        if line_count == 0: 
            pass
            line_count += 1
        
        else:
            #row 3 has total points data
            points = int(row[3])
            #row 2 has total possessions data
            possessions = int(row[2])
            #row 20 has shot quality data
            shotQuality = float(row[20])
            #calculates offensive rating
            offRating = (points/possessions)*100
            #adds the numbers found to the corresponding lists
            teamOffensiveRatings.append(offRating)
            teamOffShotQuality.append(shotQuality)
            
#opens CSV file for defense
with open('pbpstats 2019-2020 Team Data Defense.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    for row in csv_reader:
        #skips first line
        if line_count == 0: 
            pass
            line_count += 1
        
        else:
            #row 3 has total points allowed data
            points = int(row[3])
            #row 2 has total possessions data
            possessions = int(row[2])
            #row 20 has shot quality data
            shotQuality = float(row[20])
            #calculates defensive rating
            defRating = (points/possessions)*100
            #adds the numbers to the corresponding lists
            teamDefensiveRatings.append(defRating)
            teamDefShotQuality.append(shotQuality)
#creates variable which will be easier used for graphing           
x1 = teamOffensiveRatings
y1 = teamOffShotQuality
x2 = teamDefensiveRatings
y2 = teamDefShotQuality

correlation_matrix = np.corrcoef(x1, y1)
correlation_xy = correlation_matrix[0,1]
r_squaredOff = str(round(correlation_xy**2,4))

correlation_matrix = np.corrcoef(x2, y2)
correlation_xy = correlation_matrix[0,1]
r_squaredDef = str(round(correlation_xy**2,4))


#creates the plot for offense
ax = sns.regplot(x1, y1, color='firebrick')
# plotting the points
plt.scatter(x1, y1) 
# naming the x axis
plt.xlabel('Offensive Rating\n' + 'R-Squared: ' + r_squaredOff) 
# naming the y axis 
plt.ylabel('Shot Quality')
# giving a title to my graph 
plt.title('Offensive Rating vs. Shot Quality 2019-2020')
# function to show the plot
plt.show()    
#creates the plot for defense
ax = sns.regplot(x2, y2, color='firebrick')
# plotting the points
plt.scatter(x2, y2) 
# naming the x axis
plt.xlabel('Defensive Rating\n' + 'R-Squared: ' + r_squaredDef) 
# naming the y axis 
plt.ylabel('Opponent Shot Quality')
# giving a title to my graph 
plt.title('Defensive Rating vs. Shot Quality 2019-2020')
# function to show the plot
plt.show()  
            