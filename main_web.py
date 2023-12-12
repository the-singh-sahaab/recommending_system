import streamlit as st
import pickle
import pandas as pd
import requests

movie_dict= pickle.load(open("movie_dict.pkl","rb"))
movie_list = pd.DataFrame(movie_dict)
simp= pickle.load(open("similarity.pkl","rb"))

def get_poster(movie_id):
    new = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=dd277b2bf33a5310b6c1e1d700e7a6f9&language=en-US")
    data_json = new.json()
    return "https://image.tmdb.org/t/p/w500"+data_json["poster_path"]#complete path for the poster image


def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = simp[movie_index]
    sorted_distance = sorted(list(enumerate(distances)),reverse= True ,key = lambda x:x[1])[1:6]
    recommend_movie_list = []
    movie_poster = []
    for i in sorted_distance:
        movie_poster.append(get_poster(movie_list.iloc[i[0]].movie_id))
        recommend_movie_list.append(movie_list.iloc[i[0]].title)
    return recommend_movie_list, movie_poster
    
    
st.title("GET YOUR STYLE OF MOVIE")
name_of_movie = st.selectbox("Please give a refrence for your movies:", movie_list["title"].values, placeholder="Choose an option", label_visibility="visible")

if st.button("Recommend"):
    t, poster_of_movie = recommend(name_of_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        b = "+".join(t[0].split())
        c = "https://www.google.com/search?q="
        st.link_button(t[0], c+b, use_container_width=True)
        # st.header(t[0])
        st.image(poster_of_movie[0])

    with col2:
        b = "+".join(t[1].split())
        c = "https://www.google.com/search?q="
        st.link_button(t[1], c+b, use_container_width=True)
        st.image(poster_of_movie[1])

    with col3:
        b = "+".join(t[2].split())
        c = "https://www.google.com/search?q="
        st.link_button(t[2], c+b, use_container_width=True)
        st.image(poster_of_movie[2])
    with col4:
        b = "+".join(t[3].split())
        c = "https://www.google.com/search?q="
        st.link_button(t[3], c+b, use_container_width=True)
        st.image(poster_of_movie[3])
    with col5:
        b = "+".join(t[4].split())
        c = "https://www.google.com/search?q="
        st.link_button(t[4], c+b, use_container_width=True)
        st.image(poster_of_movie[4])
    # for i in t:
    #     b = "+".join(i.split())
    #     c = "https://www.google.com/search?q="
    #     st.link_button(i, c+b, use_container_width=True)

