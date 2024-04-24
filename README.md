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

### Test and Train sets:
Since we have a sufficient amount of data, I have decided to allocate a larger portion of it, specifically 80%, to the training set. This approach is based on observations from different results which indicate that giving the model more historical data to learn from can effectively capture the underlying patterns and seasonality. Consequently, this has been found to lead to better model performance.

### Selection of Models for Traffic Analysis:
 **SARIMAX** and **Prophet** models were chosen to forecast traffic volumes with daily frequency for two selected locatins: Bergheimer Street and Lessing Street.These case studies provide a granular look at urban traffic dynamics, offering actionable insights for urban development, transport management, and infrastructure planning. The chosen statistical time series models are integral for enhancing urban traffic management and aiding in strategic urban planning.

For **Bergheimer Str.** Between the two selected time serries models, the optimized and and fine-tuned SARIMAX Modelperformed better with the following metrics with the following metrics:
Mean Absolute Error (MAE): 33.35, Root Mean Squared Error (RMSE): 43.861, Mean Absolute Scaled Error (MASE): 0.44%

For **Lessingstr.** Between the two selected time serries models, the optimized and and fine-tuned Prophet model performed better  and recorded a MAPE of 16.62% and a MASE of 0.44%, MAE of 8.26 and RMSE of 9.927

Future enhancements could involve including additional external factors such as weather conditions, and exploring hybrid models to further refine predictions, although suitable weather data was not available within the project timeframe.


### Repository Structure:
Data: Contains both the raw and cleaned datasets.
<br>JupyterNotebooks: Houses exploratory and final analysis notebooks.
<br>Slides: Provides a link to the presentation slides.
