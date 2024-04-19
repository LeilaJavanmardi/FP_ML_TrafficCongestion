# Intelligent Flow: Leveraging Machine Learning  for Urban Traffic Management

### Introduction
By analyzing comprehensive traffic data from Heidelberg's public data portal, this project aims to decipher traffic patterns and predict future trends. Our objective is to optimize traffic flows, reduce congestion, and enhance urban planning. This involves using Time Series models to forecast traffic volumes. Through the integration of SARIMAX and Prophet models, I focus on predicting traffic intensity across different times and conditions, thereby contributing to smarter urban environments and sustainable city planning.


### Data Description
The dataset contains an observation of the traffic flow at a specific place and time. It contains current and past measurements from traffic cameras in the city of Heidelberg (measurement interval: 15 min).
In addition to general location information, each dataset contains, if available, information on the number of vehicles and vehicle types measured, the average distance between vehicles and their passing time.
A detailed description of the dataset,the specification, and the raw data can be found here: 
https://ckan.datenplattform.heidelberg.de/de/dataset/mobility_main_trafficcamera

### Research Questions and machine learning objective 
**How can we accurately predict traffic intensity variations across different times and locations?**
<br>What are the peak traffic hours, What extrenal factors contribute? How does traffic intensity fluctuate throughout the day?


### Data Gap Filling Strategy:
In the time series analysis, I addressed data gaps through two primary methods to ensure data integrity and reliability. Initially, gaps were filled using data from the exact same weekday and time from the previous week, leveraging historical consistency. This method significantly reduced the number of missing values. For any remaining gaps, linear interpolation was applied, which estimates missing entries based on the values of their neighbors. This dual approach maintained the continuity and accuracy of the traffic intensity dataset.

### Selection of Models for Traffic Analysis:
 **SARIMAX** and **Prophet** models were chosen to forecast traffic volumes across different frequencies—daily, weekly, and business days for two selected locatins: Bergheimer Street and Lessing Street.These case studies provide a granular look at urban traffic dynamics, offering actionable insights for urban development, transport management, and infrastructure planning. The chosen statistical time series models are integral for enhancing urban traffic management and aiding in strategic urban planning.

For Bergheimer Str.
The best Prophet model showed MAE: 36.84, RMSE: 46.016, MAPE: 28.95%, and MASE: 0.47%.
The best SARIMAX model had MAE: 33.35, RMSE: 43.861, MAPE: 42.60%, and MASE: 0.44%. Both models included holidays and special days as external factors.
For Lessingstr.
The optimized Prophet model recorded a MAPE of 16.615% and a MASE of 0.668%, also incorporating holidays and special events.
Future enhancements could involve including additional external factors such as weather conditions, and exploring hybrid models to further refine predictions, although suitable weather data was not available within the project timeframe.


### Repository Structure:
Data: Contains both the raw and cleaned datasets.
<br>JupyterNotebooks: Houses exploratory and final analysis notebooks.
<br>Slides: Provides a link to the presentation slides.