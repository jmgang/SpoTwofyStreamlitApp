import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


hale_songs_df = pd.read_csv('https://raw.githubusercontent.com/jmgang/SpoTwoFy-project-notebooks/main/data/hale/hale_songs.csv')
def load_no_ml_rec_pool():
    rec_pool_df = pd.read_csv("https://raw.githubusercontent.com/jmgang/SpoTwoFy-project-notebooks/main/data/recommender/spotify_tracks_hale_no_ml_rec_pool.csv")
    return pd.concat([rec_pool_df, hale_songs_df], axis=0, ignore_index=True)

def load_expanded_ml_rec_pool():
    return pd.read_csv("https://raw.githubusercontent.com/jmgang/SpoTwoFy-project-notebooks/main/data/recommender/spotify_tracks_hale_expanded_ml_rec_pool.csv")

def load_sentiment_ml_rec_pool():
    return pd.read_csv("https://raw.githubusercontent.com/jmgang/SpoTwoFy-project-notebooks/main/data/recommender/spotify_tracks_hale_sentiment_ml_rec_pool.csv")

rec_pool_no_ml_df = load_no_ml_rec_pool()
expanded_ml_rec_pool = load_expanded_ml_rec_pool()
sentiment_ml_rec_pool = load_sentiment_ml_rec_pool()

feature_cols = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness',\
                'liveness', 'valence', 'tempo']


def get_cosine_distance(matrix, vector):
    return 1 - cosine_similarity(matrix, vector)


def get_recommendations(seed_track, recommender_engine):
    if recommender_engine == 1:
        seed_track_data = rec_pool_no_ml_df[rec_pool_no_ml_df['track_name'] == seed_track].iloc[0][
            feature_cols].values.reshape(1, -1)
        all_distances = get_cosine_distance(rec_pool_no_ml_df[feature_cols].values, seed_track_data)
        rec_pool_no_ml_df['cosine_dist_features'] = all_distances
        recommendation_df = rec_pool_no_ml_df[rec_pool_no_ml_df['track_name'] != seed_track].nsmallest(10, 'cosine_dist_features')
        return recommendation_df.track_id.unique()
    elif recommender_engine == 2:
        genre_proba_cols = [col for col in expanded_ml_rec_pool.columns if col.startswith('genre_')]
        seed_track_data = expanded_ml_rec_pool[expanded_ml_rec_pool['track_name'] == seed_track].iloc[0][feature_cols + genre_proba_cols].values.reshape(1, -1)
        all_distances = get_cosine_distance(expanded_ml_rec_pool[feature_cols + genre_proba_cols].values, seed_track_data)
        expanded_ml_rec_pool['cosine_dist_features'] = all_distances
        recommendation_df = expanded_ml_rec_pool[(expanded_ml_rec_pool['track_name'] != seed_track)
                                                 & (~expanded_ml_rec_pool['track_id'].isin(hale_songs_df.track_id.unique()))].nsmallest(10,'cosine_dist_features')
        return recommendation_df.track_id.unique()
    else:
        genre_proba_cols = [col for col in sentiment_ml_rec_pool.columns if col.startswith('genre_')]
        seed_track_data = sentiment_ml_rec_pool[sentiment_ml_rec_pool['track_name'] == seed_track].iloc[0][
            feature_cols + genre_proba_cols].values.reshape(1, -1)
        all_distances = get_cosine_distance(sentiment_ml_rec_pool[feature_cols + genre_proba_cols].values,
                                            seed_track_data)
        sentiment_ml_rec_pool['cosine_dist_features'] = all_distances
        recommendation_df = sentiment_ml_rec_pool[(sentiment_ml_rec_pool['track_name'] != seed_track)
                                                  & (~sentiment_ml_rec_pool['track_id'].isin(hale_songs_df.track_id.unique()))].nsmallest(10,'cosine_dist_features')
        return recommendation_df.track_id.unique()