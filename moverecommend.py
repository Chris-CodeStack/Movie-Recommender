import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Read dataset
df = pd.read_csv("movie_dataset.csv")

# Step 2: Select features
features = ["keywords", "cast", "genres", "director"]

# Step 3: Fill missing values
for feature in features:
    df[feature] = df[feature].fillna("")

# Step 4: Combine features into one string
def combine_features(row):
    return row["keywords"] + " " + row["cast"] + " " + row["genres"] + " " + row["director"]

df["combined_features"] = df.apply(combine_features, axis=1)

# Step 5: Convert text to count matrix
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

# Step 6: Compute cosine similarity
cosine_sim = cosine_similarity(count_matrix)

# Step 7: Helper function
def get_index_from_title(title):
    return df[df["title"] == title].index[0]

# Step 8: Input movie
movie_user_likes = "Avatar"
movie_index = get_index_from_title(movie_user_likes)

# Step 9: Get similarity scores
similar_movies = list(enumerate(cosine_sim[movie_index]))

# Step 10: Sort similar movies
sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

# Step 11: Print top recommendations
print("Top recommendations for", movie_user_likes + ":")
count = 0

for movie in sorted_similar_movies:
    index = movie[0]
    title = df.iloc[index]["title"]

    if title != movie_user_likes:
        print(title)
        count += 1

    if count >= 10:
        break