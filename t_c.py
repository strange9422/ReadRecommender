import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import warnings

warnings.filterwarnings("ignore")

books = pd.read_csv('Books.csv', delimiter=';', error_bad_lines=False, encoding='ISO-8859-1', warn_bad_lines=False)
users = pd.read_csv('Users.csv', delimiter=';', error_bad_lines=False, encoding='ISO-8859-1', warn_bad_lines=False)
ratings = pd.read_csv('Book-Ratings.csv', delimiter=';', error_bad_lines=False, encoding='ISO-8859-1',
                      warn_bad_lines=False)


def topbook():
    ratings_with_name = ratings.merge(books, on='ISBN')
    num_rating_df = ratings_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
    num_rating_df.rename(columns={'Book-Rating': 'num_ratings'}, inplace=True)

    avg_rating_df = ratings_with_name.groupby('Book-Title').mean()['Book-Rating'].reset_index()
    avg_rating_df.rename(columns={'Book-Rating': 'num_ratings'}, inplace=True)

    popular_df = num_rating_df.merge(avg_rating_df, on='Book-Title')
    popular_df = popular_df[popular_df['num_ratings_x'] > 250].sort_values('num_ratings_y', ascending=False).head(50)
    popular_df = popular_df.merge(books, on='Book-Title').drop_duplicates('Book-Title')[
        ['Book-Title', 'Book-Author', 'Image-URL-M', 'num_ratings_x', 'num_ratings_y']]

    dic = {}
    name = popular_df['Book-Title'].tolist()
    for i in range(50):
        dic[name[i]] = popular_df[popular_df['Book-Title'] == name[i]]['Image-URL-M'].values[0]

    return dic


def recommendBook(book_name, n):
    try:
        ratings_with_name = ratings.merge(books, on='ISBN')
        # collaborative
        # ratings_with_name.groupby('User-ID').count()
        x = ratings_with_name.groupby('User-ID').count()['Book-Rating'] > 200  # user who have rated more than 200 books
        ed_user = x[x].index  # took boolean index

        filtered_rating = ratings_with_name[
            ratings_with_name['User-ID'].isin(ed_user)]  # got user who rated more than 200 books

        y = filtered_rating.groupby('Book-Title').count()['Book-Rating'] >= 50
        famous_books = y[y].index

        final_ratings = filtered_rating[filtered_rating['Book-Title'].isin(
            famous_books)]  # we will search book that are in famous book data frame fromm filterd data frame

        pt = final_ratings.pivot_table(index='Book-Title', columns='User-ID',
                                       values='Book-Rating')  # here we created pivot table for user and book one book value is point in 810 columns

        pt.fillna(0, inplace=True)

        similarity_score = cosine_similarity(
            pt)  # here we find ecludian distance of books to another books that is 706 books to another 706 books

        index = np.where(pt.index == book_name)[0][0]  # find the index no in pt data frame with high rated book
        similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:n+1]
        # find similarity score of that book with other and sort in descending order enumarate it to get item with index

        dic = {}
        name = []
        for i in similar_items:
            name.append(pt.index[i[0]])

        for i in range(len(name)):
            dic[name[i]] = ratings_with_name[ratings_with_name['Book-Title'] == name[i]]['Image-URL-M'].values[0]


        return dic

    except:
        a="Unfortunately don't have enough rating to this book try another one or else you misspelled"
        return a


dic=recommendBook('Harry Potter and the Goblet of Fire (Book 4)',10)
# print(type(dic))