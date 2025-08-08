
## How to use this repo

1. Use this template to create your GitHub project repo  
2. In your new repo click on the green Code button  
3. Then, from the Codespaces tab, click Create codespace on main  
5. Wait for the workspace to open. This can take a few minutes  
6. Open a new terminal and `pip3 install -r requirements.txt`  
7. Open the jupyter_notebooks directory and click on the notebook you want to open 
8. Click the kernel button and choose Python Environments.

Note that the kernel says Python 3.12.1 as it inherits from the workspace so it will be Python-3.12.1 as installed by Codespaces. To confirm this you can use `! python --version` in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In your Cloud IDE, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with *Regenerate API Key*.

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Business Requirements

As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## Hypothesis and how to validate?

* We hypothesize that:
    1. House size, quality, and condition are highly correlated to sale price.
    2. Garage size, kitchen quality, and basement finish also play a significant role.
* Validation Strategy:
    - Correlation matrix (Pearson, Spearman)
    - Predictive Power Score (PPS)
    - Visualization (scatter plots, box plots)
    - Feature importance after model training

## The rationale to map the business requirements to the Data Visualisations and ML tasks

**Business Requirement 1**: Identify which house attributes most strongly affect price  
  - Action: Correlation analysis, PPS matrix, data visualizations  
  - Tools: pandas, seaborn, matplotlib, `ppscore`

**Business Requirement 2**: Predict house sale prices from input attributes  
  - Action: Build a regression pipeline using conventional ML algorithms  
  - Tools: Scikit-learn, GridSearchCV, pipeline, joblib, XGBoost/RandomForest

## ML Business Case

**ML Task**: Regression  
**Target Variable**: `SalePrice`  
**Learning Method**: Supervised ML  
**Ideal Outcome**: An ML model with at least **R² ≥ 0.75** on both train and test sets  
**Success Metrics**:
- R² score ≥ 0.75
- Visual match on actual vs predicted plots
- Low RMSE and MAE

**Model Output**:
- Predicted sale price for any house
- Sum of sale price for Lydia's four houses

**Relevance**:
- Helps Lydia maximize property value and future investments in Ames

## Dashboard Design

- **Page 1: Project Summary**
  - Summary of dataset
  - Description of Lydia’s situation
  - Project goals
  - Display sample rows (first 5)

- **Page 2: Price Correlation Study**
  - Show the most correlated variables to SalePrice
  - Display plots (scatter/box/...) for top features vs sale price
  - Summary interpretation below plots

- **Page 3: Predict Lydia's Houses**
  - Display the 4 houses' attributes
  - Show predicted price per house
  - Show sum of 4 predicted sale prices

- **Page 4: Live Price Prediction Tool**
  - Streamlit form for user to input house features
  - Button to trigger prediction from trained model
  - Display predicted sale price for input house

- **Page 5: Model Performance**
  - Show pipeline steps
  - Show actual vs predicted plots (train/test)
  - Show R², MAE, RMSE
  - Feature importance plot

- **Page 6: Project Hypothesis & Validation**
  - Restate hypotheses
  - Describe how each was tested and validated

## Unfixed Bugs

- None known at this point. This section will be updated during project development.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the .python-version Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- `pandas` – Data wrangling
- `numpy` – Numerical computations
- `matplotlib`, `seaborn` – Data visualization
- `scikit-learn` – ML pipeline, model training & evaluation
- `xgboost` – Advanced regression model
- `joblib` – Model serialization
- `streamlit` – Dashboard web app

Example usage:
### python
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)

## Credits
    
### Content

* Machine Learning Full Course [YouTube Tutorial](https://www.youtube.com/watch?v=i_LwzRVP7bg&list=PLWKjhJtqVAblfum5WiQblKPwIbqYXkDoC&index=5)
* Additional resources to the CodeInstitute learning platform came from DataCamp
    * [Machine Learning Cheat Sheet](https://www.datacamp.com/cheat-sheet/machine-learning-cheat-sheet)
    * [The Beginner's Guide to The Machine Learning Workflow](https://www.datacamp.com/blog/a-beginner-s-guide-to-the-machine-learning-workflow)
    * [10 Top Machine Learning Algorithms & Their Use-Cases](https://www.datacamp.com/blog/top-machine-learning-use-cases-and-algorithms)
    * [Data Visualization Cheat Sheet](https://www.datacamp.com/cheat-sheet/data-viz-cheat-sheet)
    * [Scikit-Learn Cheat Sheet: Python Machine Learning](https://www.datacamp.com/cheat-sheet/scikit-learn-cheat-sheet-python-machine-learning)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)


* In case you would like to thank the people that provided support through this project.

