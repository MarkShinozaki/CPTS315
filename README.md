# Course Project 

## [Project Proposal - Predictive Model on NYC Lottery](https://github.com/MarkShinozaki/CPTS315-IntroductionToDataMining/tree/Project/Project%20Work/Project%20Proposal)

#### Data Mining Task:
- The project's primary data mining task is to perform exploratory data analysis on the winning numbers of the New York State Power Ball and Mega Millions. The ultimate goal is to build a predictive model that can forecast future winning numbers. The motivation stems from a desire to uncover any discernible patterns in the lottery data that might aid in prediction, despite acknowledging the inherent randomness of lottery number draws.

#### Dataset:
- The dataset for this project is sourced from Data.gov, an open data platform provided by the United States government. It encompasses the winning numbers for Power Ball and Mega Millions in New York State, covering draws from late September 2020 to late March 2023. This dataset provides a substantial volume of data to analyze trends and build predictive models.

#### Methodology:
- The approach to solving the data mining task involves:

  - Utilizing Python as the primary programming language, along with libraries like pandas for data manipulation, numpy for numerical operations, and potentially seaborn for data visualization and scikit-learn for machine learning.
  - Exploratory data analysis will be conducted to understand the data's structure, characteristics, and underlying patterns.
  - Predictive modeling techniques will be employed, potentially including regression models and other statistical or machine learning methods to attempt to predict future lottery numbers.
  - The methodology may evolve based on feedback and the effectiveness of initial tools and approaches in handling the dataset and achieving the project objectives.

#### Final Product and Success Measurement:
- The final product of the project will be a predictive model capable of forecasting future winning numbers for the Power Ball and Mega Millions lottery games in New York State. The success of the project will be measured by:

  - The accuracy of the predictive model in forecasting winning numbers.
  - The depth of insights gained from the exploratory data analysis.
  - The project's ability to help explore and learn new data mining techniques, thus applying theoretical knowledge to a practical, real-world problem.

#### Learning Objectives:

- The project aims to provide a hands-on experience in applying data mining techniques to a real-world dataset.
- It is expected to enhance understanding of how to manipulate large datasets, apply exploratory data analysis, and develop predictive models using modern data science tools and techniques.

This proposal outlines a structured approach to tackling a complex data mining task with a clear set of tools and objectives, recognizing the challenges inherent in predicting outcomes in a random system like a lottery. The exploration of such a dataset will help in sharpening data science skills and potentially uncovering interesting patterns that could inform future studies or similar projects.


---


## Final Project Report

## [Overview of the Final Project: Predictive Model Using Regression for NYC Lottery, Power Ball & Mega Ball](https://github.com/MarkShinozaki/CPTS315-IntroductionToDataMining/tree/Project/Project%20Work/Final%20-%20Project%20Report)


### Project Motivation and Objectives:
- The project aimed to develop a predictive model for forecasting winning lottery numbers for Power Ball and Mega Ball. The motivation was driven by the prospect of assisting lottery participants in making informed choices, potentially enhancing their chances of securing a win. The primary goals were to:

  - Analyze historical data of winning numbers.
  - Identify common winning numbers and patterns.
  - Develop a model capable of predicting future winning numbers.

### Data Mining Questions Investigated:
- Identification of frequently drawn numbers.
- Examination of patterns or trends in winning numbers.
- Investigation of numbers that frequently appear together.
- Feasibility of using past numbers to predict future draws.

### Personal Motivation:
- The project served as a practical application of data mining techniques to a real-world scenario, aiming to understand and perhaps predict seemingly random events such as lottery draws.

### Challenges and Approach:
- The primary challenge was the inherent randomness of lottery numbers, coupled with ensuring that the model did not overfit the data. The approach involved:
  - Data cleaning and preparation.
  - Exploratory data analysis to understand patterns.
  - Utilizing logistic regression to develop the predictive model.

### Results Summary:
- The models produced high Mean Squared Error (MSE) values, indicating large prediction errors and low accuracy. Specifically, MSE values were 121.364 for Power Ball and 114.839 for Mega Ball, suggesting the model's poor performance in capturing the underlying patterns or randomness of the draw results.

### Detailed Project Components:

**Data Mining Task**:
- The task utilized lottery data from NYC, specifically covering Power Ball and Mega Ball draws. The primary output was the predictive model's ability to forecast winning numbers based on historical data.

**Algorithmic Approach**:
- A regression model was developed using historical lottery data. Features were selected based on their correlation with winning numbers, and the model was trained using a subset of the data. Challenges like large data volumes and feature selection were addressed using Python's pandas library and regularization techniques to mitigate overfitting.

**Evaluation Methodology**:
- Data from Data.gov provided historical winning numbers for model training and testing.
- Model performance was assessed using Mean Squared Error (MSE), a common metric for evaluating regression models that reflects the average squared difference between predicted and actual values.

**Results and Analysis**:
- The model's predictions, along with high MSE values, highlighted its limitations in accurately predicting lottery numbers, attributed to the random nature of lottery draws.
- Visualization tools like Seaborn were used to identify frequently occurring numbers, although this did not significantly improve predictive accuracy.

**Lessons Learned and Reflections**:
- The project highlighted the complexities of modeling and predicting outcomes based on random processes like lottery draws.
- Insights were gained into the application of machine learning algorithms and data analysis techniques. The experience suggested potential improvements, such as incorporating additional datasets or exploring different modeling techniques to enhance prediction accuracy.

**Acknowledgments**:
- Data sources and tools used in the project included datasets from Data.Gov and Google Colab for coding and model development.

In conclusion, while the predictive model developed during the project did not achieve high accuracy, the process provided valuable insights into the challenges and potential strategies for modeling random events using data mining and machine learning techniques.













