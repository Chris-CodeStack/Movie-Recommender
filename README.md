# Movie Recommendation System

## Overview
This project is a **content-based movie recommendation system** built in Python. Its purpose is to recommend movies that are similar to a movie a user already likes. Instead of using popularity alone, this system compares the actual content of movies, such as their **keywords, cast, genres, and director**, and then suggests the closest matches.

For example, if a user likes **Avatar**, the program searches through the dataset, finds movies with similar content features, and returns a list of recommended titles.

---

## What the Project Does
The recommendation system:
- Takes a movie title as input
- Searches for that movie in the dataset
- Combines important features of every movie into one text representation
- Converts those text features into numerical vectors
- Uses **cosine similarity** to measure how similar movies are
- Outputs the top recommended movies that are most similar to the chosen title

This is an example of a **content-based recommender system**, meaning it recommends items based on their own attributes rather than based on other users’ behavior.

---

## How It Was Made
The project was built step by step using Python and machine learning tools from **scikit-learn**.

### Main steps:
1. **Imported the required libraries**
   - `pandas` for reading and handling the CSV dataset
   - `CountVectorizer` from `sklearn` for converting text into count vectors
   - `cosine_similarity` from `sklearn` for comparing movies

2. **Loaded the dataset**
   - Read the movie dataset CSV file into a pandas DataFrame

3. **Selected important features**
   - The project uses:
     - `keywords`
     - `cast`
     - `genres`
     - `director`

4. **Cleaned the data**
   - Missing values in the selected columns were replaced with empty strings to prevent errors

5. **Combined the selected features**
   - All chosen movie features were merged into one text string for each row

6. **Converted text into vectors**
   - `CountVectorizer` was used to transform the combined text into numerical form

7. **Calculated similarity**
   - `cosine_similarity` was applied to compare all movie vectors

8. **Generated recommendations**
   - The input movie’s similarity scores were sorted from highest to lowest
   - The most similar movies were returned as recommendations

---

## Tools and Technologies Used
- **Python**
- **pandas**
- **scikit-learn**
- **CountVectorizer**
- **cosine similarity**
- **CSV dataset**

