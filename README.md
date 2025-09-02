# Netflix Titles Analysis 🎬

This project analyzes the **Netflix Titles dataset** (from Kaggle) using Python and Pandas.  
The dataset contains information about TV shows and movies available on Netflix, including release year, cast, country, and date added.

## 📂 Project Structure
- `netflix_analysis.py` → Main Python script for data cleaning and analysis  
- `netflix_cleaned.csv` → Cleaned dataset with missing values handled  
- `netflix_titles.csv` → Original dataset

## Dataset  
The dataset used in this project is the [Netflix Movies and TV Shows dataset](https://www.kaggle.com/shivamb/netflix-shows) from Kaggle.  
(It is not uploaded here to keep the repository lightweight. You can download it directly from Kaggle if you want to reproduce the analysis.)


## 🔍 Key Steps
- Loaded and explored dataset using Pandas (`.info()`, `.describe()`)  
- Handled missing values (`fillna("Unknown")`)  
- Converted `date_added` and `release_year` to datetime format  
- Extracted **year, month, day, weekday** from `date_added`  
- Prepared cleaned dataset for further analysis and visualization  

## 🚀 Next Steps
- Perform exploratory data analysis (EDA)  
- Visualize trends (e.g., number of shows per year, genre distribution, etc.)  
- Share insights about Netflix content library growth  

## 🛠️ Tools Used
- Python 🐍  
- Pandas  
- Matplotlib / Seaborn (planned for visualization)  

---
👨‍💻 Author: Anshumaan Mishra  
