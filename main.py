import streamlit as st
import pickle
import numpy as np

st.set_page_config(layout="wide")
st.title('Book recommendation system')
st.info(
    'This project is a basic implementation of a book recommendation system, aimed at suggesting books to users based on their preferences. The system employs data analysis techniques to examine user interactions with books, such as ratings and genres. It uses collaborative filtering or content-based filtering to identify patterns and suggest books that align with a users interests.')
# st.info('It is important to note that this project is a foundational prototype and not the final form of the code. As a work in progress, it can be expanded with more sophisticated algorithms, enhanced data sources, and a more user-friendly interface. The current version serves as a stepping stone towards a more advanced, personalized recommendation system.')
data = pickle.load(open('/home/chilltoast/PycharmProjects/MajorProjectFlaskApplication/popular.pkl', 'rb'))
pt = pickle.load(open('/home/chilltoast/PycharmProjects/MajorProjectFlaskApplication/pt.pkl', 'rb'))
similarity_scores = pickle.load(
    open('/home/chilltoast/PycharmProjects/MajorProjectFlaskApplication/similarity_scores.pkl', 'rb'))
books = pickle.load(open('/home/chilltoast/PycharmProjects/MajorProjectFlaskApplication/books.pkl', 'rb'))
colA, cloB = st.columns([1, 2])
with colA:
    bookName = st.text_input("Enter your book:")
book_name = bookName
recommend_button = st.button('Recommend')
def recommend():
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        # item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        data.append(item)

    print(data)
    return data

if recommend_button:
    try:
        recommendations = recommend()
        st.table(recommendations)

    except:
        st.warning("!!Choose another book!!")
