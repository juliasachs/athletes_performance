# athletes_performance
How does pressure influence the performance of athletes?

Some athletes perform at their best during high pressure situations as e.g. LeBron James for Cleveland delivered an outstanding performance (Game 7 of the NBA Finals between Golden State and Cleveland) and wins with Cleveland the first championship in the Franchise history. Whereas the other athletes struggle to perform at their best as e.g. Drew Brees Quarterback of New Orleans. An outstanding quarterback with great stats during the regular Season shows a different performance in the play offs.  Why was he not able to keep up with the level he performed on the entire Season?

It is not a secret that a player of the level as LeBron James can perform under pressure and actually raise his level to perform on his peak. But what is with all the other players and role players whose come in from time to time? Many players struggle with pressure and their performance decreases. Missing shots they would usually make or taking bad decisions that cause turnover are the most obvious signs. 
To win a championship as a team, you need players to perform well under different levels of pressure. So I asked myself what indicators you have to measure if players can hold up to it, to put the optimal team for different phases in a game together, which is able to raise their overall level under pressure.

AIM : Provide a framework to evaluate the performance of NBA players under pressure which can also used for recruitment of players from College  Basketball (NCAA). 

The project will use the Play-by-Play dataset which includes detailed information about all events of the game including their time of occurrence for all NBA games. This includes e.g. the type of shot, fouls. So for Play-by-Play data for season 2016/2017 (90MB) was analyzed but will be extended to include data of several NBA seasons which will be gathered via available APIs:
https://drive.google.com/file/d/0B5QcyddjOpKOODZjZ0FJU3JSakU/view
https://github.com/bradleyfay/py-goldsberry
https://github.com/ethanluoyc/statsnba-playbyplay

The project is structured to answer the following four key questions:
1)	How can we measure pressure?
The effect of several indicators as score, minutes remaining in game, position of teams in league, games in season remaining, fouls in game, missed shoots in a row,… and their effect on the performance (points, missed shots, …) will be analyzed across all teams via a feature selection method to identify the key criteria which define a situation with high pressure.
2)	How does the performance of teams and players change under pressure?
The key criteria will be used to analyze the performance of teams and players separately to identify how it changes in different situations.
3)	Which teams and player belong to the same category?
Using a cluster analysis the teams and player will be assigned to different categories based on the effect of different criteria on their performance. 
4)	Which type of player would improve the performance of a certain team?

## First findings


![Shots missed (red) and made (blue) by quater and time.](miss_make.png)]

![a) Influence of time.](miss_make_1.png) ![a) Influence of number of quater.](miss_make_2.png)

The Iinfluence of time within each quarter can be noted in an increase in missed shots in the beginning and end of each quater following a parabolic shape. The number of quaters on the other hand shows a linear patter with an increase of missed shots for a later quater.


![](free_thows.png)] ![](free_thows2.png)

The effect of the score difference on the numbers of free throws missed shows itself in particular in the first and fourth quater. In the first quater, an increased score difference (e.g. one team being ahead early in the game) leads to a higher number of free thows missed. In contrast to that, the number of missed free throws for a lower score difference is higher in the forth quater. Looking at the distribution for all teams, we see a high variance which indicated that the performance of teams highly varies.

