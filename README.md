# Cut Off Grade Calculator

This Python script is designed to calculate the cut-off grade for use in Mining Economics. It begins by calculating the recovery using a logistic model based on the weighted average grade. Next, it estimates the processing cost through a regression model derived from actual cost data. Using the calculated recovery, processing cost, and net price, the script determines the cut-off grade. Finally, all calculations are visualized through a graph for better interpretation.

Cut-Off Grade = Processing Cost / ((Net Price) * Recovery)

Recovery = Rmax * (1 - e^(-k * G))

Processing Cost = a + b * G


# Author

Made by Batuhan Berk Başoğlu