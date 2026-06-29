import gradio as gr
import pickle

# Load Data
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Recommendation Function
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return "\n".join(recommended_movies)

# Interface
demo = gr.Interface(
    fn=recommend,
    inputs=gr.Dropdown(
        choices=movies["title"].values.tolist(),
        label="Select Movie"
    ),
    outputs=gr.Textbox(label="Recommended Movies"),
    title="🎬 Movie Recommendation System",
    description="Select a movie and get 5 similar movie recommendations."
)

demo.launch()
