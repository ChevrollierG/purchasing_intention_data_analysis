# purchasing_intention_data_analysis

This project concerns the dataset 'Online Shoppers Purchasing Intention' that can be found here: https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset  

The project contains a preliminary data cleaning, data exploration, dimensionality reduction, data preprocessing, data modeling.  
All those can be found in the jupyter notebook.

The project also includes a Flask API for deployment, see after for more information.  

A report is also given in PDF format.


#### To launch the API, you need to :  

-install the 2.0.2 version of Flask and Pandas.  
-you need to stock the directories "templates" and "static" at the same place than the file "app.py".  
-you need to change the global variable "path" in app.py to set the path to the files "model.pickle" and "data.csv".  
-open the cmd and launch the app.py file with "python app.py".  
-it shows you an ip adress (your local ip followed by :5000), browse it.  
-it's done, you can use it.  

