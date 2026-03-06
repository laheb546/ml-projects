#House price Exploratory Data Analysis (EDA)
## Project Overview
This Project explores a house price dataset to identify factors affecting property prices.
The goal is to uncover patterns, handle missing data, and visualize relationships between features and sale price.
_ _ _
## Tools used
- Python 
- Pandas 
- Numpy 
- Matplotlib 
_ _ _
## Analysis Workflow
###1 Feature Inspection and Missing Data
- Checked each feature for null values.
- Created binary columns :for null and not null.
- Grouped features and analyzed how missing values affect median saleprice.
- Observed that missing values sometimes slightly increase or decrease price ,tiny features have negligible effect.
###2 Year Feature Analysis
- Plotted 'yearsold' vs 'saleprice' but noticed unexpected negative trend.
- Investgated related year features. 
- Created derived features. 
- Observed if small differences in derived features it show higher price,if large differences in derived features it show small price. 
- This explained the earlier counterintuitive trend.
###3 Numerical Feature Analysis
- Separated numerical features in to :-
       - Discrete  < 25 unique values.
       - Continuous >= 25 unique values.
- Visualized both. 
- For continuous features it were skewed performed log transformation handling zeros to avoid errors.
###4 Outlier Detection 
- Used scatter and box plot to identify outliers. 
- Observed and documented extreme values.
###5 Categorical Feature Analysis
- Checking missing values in categorical features.
- Plot. 
- Replaced nan with missing.
- Numerical nan replaced with median.
###5 Rare Category Handling
- Identify categories less than 0.01% of total entries.
- Replaced them with 'Rarevalue' to simplify Analysis.
###7 Dataset Preparation 
- After cleaning and transformation saved final dataset as csv for further modeling.
### key insights 
- Missing data affects some feature slightly.
- Differences between 'yearsold' and other year feature strongly influence price.
- Continuous features often require log transformation to reduce skew.
- Proper handling of rare categories and outliers improves dataset quality.
