# Title



## Data used

Using the data under 

https://www.kaggle.com/hellbuoy/car-price-prediction

we tried to get a new car prediction.

## Files

There are three python files:

1.  Columns_enhancement.py. Define two new features according to the branding positioning (remember that i.E a BMW with the same characteristics as a Dacia does not have the same value) and the type of car that is needed. These module also cleans some of the type that are in some model and brands.

2. Pipeline.py

   This one generates the model needed to make the evaluation and stores it in the data directory uin a pickle file.

3. app.py

   This is a streamlit app, that allow the user to introduce the values that it deems necessary to calculate the value.



