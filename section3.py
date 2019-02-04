
import numpy as np
import pandas as pd
import os as os
from mpl_toolkits.mplot3d import Axes3D

path = "C:/Users/media1/Desktop/DataIncubator_challenge/2016-17/2016-17/"
os.chdir(path)
files = os.listdir()

all_games = pd.DataFrame([])
for i,fname in enumerate(files):    
    data = pd.read_csv(fname,low_memory=False)
    all_games = all_games.append(data)

all_games['Minute'] = pd.to_datetime(all_games['PCTIMESTRING'], format = '%M:%S').apply(lambda x: x.minute)

make = all_games[all_games['EVENTMSGTYPE'] == 1]
miss = all_games[all_games['EVENTMSGTYPE'] == 2]

make_period = make[make['PERIOD'] <= 4]
miss_period = miss[miss['PERIOD'] <= 4]

time_shot_make =  make_period.groupby(['Minute','PERIOD']).count()
time_shot_miss =  miss_period.groupby(['Minute','PERIOD']).count()

import matplotlib.pyplot as plt

plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = time_shot_make.index.labels[0]
Y = time_shot_make.index.labels[1]

ax.scatter(X, Y , time_shot_make.values[:,0]/(time_shot_make.values[:,0]+time_shot_miss.values[:,0])*100, c='b', marker= 'o')

X = time_shot_miss.index.labels[0]
Y = time_shot_miss.index.labels[1]

ax.scatter(X, Y , time_shot_miss.values[:,0]/(time_shot_make.values[:,0]+time_shot_miss.values[:,0])*100, c='r', marker= 'o')

ax.set_zlabel('point (blue) & miss (red) [%]')
ax.set_xlabel('Time in quater [min]')
ax.set_ylabel('Quater')

ax.set_xlim([-0.0001,12])
ax.set_ylim([0,4])


my_yticks = ['1st', '2nd', '3rd', '4th']
plt.yticks([1,2,3,4], my_yticks)

plt.savefig('miss_make.png')
plt.savefig('miss_make.pdf')
    
plt.show()

last_period = all_games[all_games['PERIOD'] == 4]
last_period = last_period.replace({'SCOREMARGIN': 'TIE'}, 0)
last_period['SCOREMARGIN'].fillna(method='ffill', inplace=True)
last_period['SCOREMARGIN'] =abs(last_period['SCOREMARGIN'].apply(float))
last_period['scorechange'] = last_period['SCOREMARGIN'].diff()

score_diff_small  = last_period[last_period['SCOREMARGIN']<10]

free_throws = score_diff_small[score_diff_small['EVENTMSGTYPE'] == 3]

free_thows_made= free_throws[free_throws['scorechange'] !=0]
free_thows_missed= free_throws[free_throws['scorechange'] ==0]

free_thows_made_score = free_thows_made.groupby(['SCOREMARGIN']).count()
free_thows_missed_score = free_thows_missed.groupby(['SCOREMARGIN']).count()

import matplotlib.pyplot as plt

plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111)

X = abs(free_thows_made_score.index.values.astype(float))
Y = free_thows_made_score.values[:,0]/(free_thows_made_score.values[:,0]+free_thows_missed_score.values[:,0])

ax.scatter(X, Y, c='b', marker= 'o')

X = abs(free_thows_made_score.index.values.astype(float))
Y = free_thows_missed_score.values[:,0]/(free_thows_made_score.values[:,0]+free_thows_missed_score.values[:,0])

ax.scatter(X, Y , c='r', marker= 'o')

ax.set_xlabel('Score maragin in 4th Quater')
ax.set_ylabel('Free throws made (blue) & missed (red) [%]')

ax.set_xlim([0,10])
ax.set_ylim([0,1])

plt.savefig('free_thows.png')
plt.savefig('free_thows.pdf')

plt.show()