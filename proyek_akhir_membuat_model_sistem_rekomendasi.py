# -*- coding: utf-8 -*-
"""Proyek Akhir : Membuat Model Sistem Rekomendasi

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18nXgoj07nfNifqFVNU0z8Q5QIWJzB51C

# Sistem Rekomendasi Movie - Nimas Ristiya Rahma
"""



"""## Project Overview

Sistem rekomendasi movie merupakan sistem yang merekomendasikan movie kepada penonton atau pengguna lainnya, rekomendasi ini contohnya diterapkan pada situs seperti netflix, iqiyi, dan wetv. Sistem rekomendasi yang saya buat ini didasarkan dengan peferensi kesukaan pengguna dimasa lalu, serta rating dari movie tersebut.
Sistem rekomendasi telah menjadi lazim dalam beberapa tahun terakhir karena mereka menangani masalah kelebihan informasi dengan menyarankan pengguna produk yang paling relevan dari sejumlah besar data. Untuk produk media, rekomendasi film kolaboratif online berupaya membantu pengguna mengakses film pilihan mereka dengan menangkap tetangga yang persis sama di antara pengguna atau film dari peringkat umum historis mereka. Namun, karena data yang jarang, pemilihan tetangga menjadi lebih sulit dengan meningkatnya film dan pengguna dengan cepat. Dalam makalah ini, diusulkan sistem rekomendasi film berbasis model hibrida yang memanfaatkan pengelompokan K-means yang ditingkatkan ditambah dengan algoritma genetika (GAs) untuk mempartisi ruang pengguna yang ditransformasikan. Ini menggunakan teknik reduksi data analisis komponen utama (PCA) untuk memadat ruang populasi film yang juga dapat mengurangi kompleksitas komputasi dalam rekomendasi film cerdas. Hasil eksperimen pada dataset Movielens menunjukkan bahwa pendekatan yang diusulkan dapat memberikan kinerja tinggi dalam hal akurasi, dan menghasilkan rekomendasi film yang lebih andal dan personal jika dibandingkan dengan metode yang ada.

referensi dari proyek overview yang saya buat dapat dilihat dari tautan berikut :
[Journal of Visual Languages & Computing](https://www.sciencedirect.com/science/article/abs/pii/S1045926X14000901)

## Business Understanding

### Problem Statements

1. Bagaimana cara merekomendasikan movie yang disukai pengguna lain dapat direkomendasikan kepada pengguna lainnya juga ?

### Goals

Dapat membuat sistem rekomendasi yang akurat berdasarkan ratings dan aktivitas pengguna pada masa lalu.

### Solution approach

Solusi yang saya buat yaitu dengan menggunakan 2 algoritma Machine Learning sistem rekomendasi,yaitu :

- **Content Based Filtering** adalah algoritma yang merekomendasikan item serupa dengan apa yang disukai pengguna, berdasarkan tindakan mereka sebelumnya atau umpan balik eksplisit.
- **Collaborative Filtering**. adalah algoritma yang bergantung pada pendapat komunitas pengguna. Dia tidak memerlukan atribut untuk setiap itemnya.

Algoritma Content Based Filtering digunakan untuk merekemondesikan movie berdasarkan aktivitas pengguna pada masa lalu, sedangkan algoritma Collabarative Filltering digunakan untuk merekomendasikan movie berdasarkan ratings yang paling tinggi.

Install opendatasets yaitu library untuk mendownload dataset
"""

!pip install opendatasets

"""Import library opendatasets"""

import opendatasets as od

"""## Data Understanding

Data atau dataset yang digunakan pada proyek machine learning ini adalah data **Movie Recommendation Data** yang didapat dari situs kaggle. Link dataset dapat dilihat dari tautan berikut [movie-recommendation-data](https://www.kaggle.com/rohan4050/movie-recommendation-data)

download dataset yang dibutuhkan, dengan menambah baris code seperti berikut :
"""

od.download('https://www.kaggle.com/rohan4050/movie-recommendation-data?select=ml-latest-small')

"""Selanjutnya, baca data-data di atas dengan menggunakan fungsi pandas.read_csv"""

import pandas as pd

links = pd.read_csv('/content/movie-recommendation-data/ml-latest-small/links.csv')
movies = pd.read_csv('/content/movie-recommendation-data/ml-latest-small/movies.csv')
ratings = pd.read_csv('/content/movie-recommendation-data/ml-latest-small/ratings.csv')
tags = pd.read_csv('/content/movie-recommendation-data/ml-latest-small/tags.csv')

print('Jumlah data link movie : ', len(links.movieId.unique()))
print('Jumlah data movie : ', len(movies.movieId.unique()))
print('Jumlah data ratings dari user : ', len(ratings.userId.unique()))
print('Jumlah data ratings dari user : ', len(ratings.movieId.unique()))
print('Jumlah data : ', len(tags.movieId.unique()))

"""### Univariate Exploratory Data Analysis
Variabel-variabel pada movie-recommendation-data adalah sebagai berikut :

- links : merupakan daftar link movie tersebut.
- movies : merupakan daftar movie yang tersedia.
- ratings : merupakan daftar penilaian yang diberikan pengguna terhadap movie.
- tags : merupakan daftar kata kunci dari movie tersebut

####  Link Variabel
 eksplorasi variabel links, merupakan daftar link movie tersebut.
"""

links.info()

"""####  movies Variabel
 eksplorasi variabel movies yang merupakan daftar movie yang tersedia.
"""

movies.info()

"""#### Ratings
 eksplorasi data yang akan digunakan pada model yaitu data ratings.
"""

ratings.head()

"""cek nilai data dari data ratings"""

ratings.describe()

"""Dari output di atas, diketahui bahwa nilai maksimum ratings adalah 5 dan nilai minimumnya adalah 0.5. Artinya, skala rating berkisar antara 0.5 hingga 5.

## Data Preprocessing


### Menggabungkan Movie
menggabungkan beberapa file dengan fungsi concatenate berdasarkan pada movieId, gabungkan seluruh data pada variabel movie_all
"""

import numpy as np

# Menggabungkan seluruh movieID pada kategori movie
movie_all = np.concatenate((
    links.movieId.unique(),
    movies.movieId.unique(),
    ratings.movieId.unique(),
    tags.movieId.unique(),
))

# Mengurutkan data dan menghapus data yang sama
movie_all = np.sort(np.unique(movie_all))

print('Jumlah seluruh data movie berdasarkan movieID: ', len(movie_all))

"""### Menggabungkan Seluruh User
menggabungkan beberapa file dengan fungsi concatenate berdasarkan pada userId, gabungkan seluruh data pada variabel user_all
"""

# Menggabungkan seluruh userId
user_all = np.concatenate((
    ratings.userId.unique(),
    tags.userId.unique(),

))

# Menghapus data yang sama kemudian mengurutkannya
user_all = np.sort(np.unique(user_all))

print('Jumlah seluruh user: ', len(user_all))

"""Menggabungkan file links, movies, ratingsm tags ke dalam dataframe movie_info. Serta menggabungkan dataframe ratings dengan movie_info berdasarkan nilai movieId"""

movie_info = pd.concat([links, movies, ratings, tags])
movie = pd.merge(ratings, movie_info , on='movieId', how='left')
movie

"""seperti yang dilihat dari hasil diatas terdapat banyak sekali missing value maka lakukan cek missing value

"""

movie.isnull().sum()

"""menggabungkan rating berdasarkan movieId"""

movie.groupby('movieId').sum()

"""### Menggabungkan Data dengan Fitur Nama Movie

mendefinisikan variabel all_movie_rate dengan variabel ratings
"""

all_movie_rate = ratings
all_movie_rate

"""Menggabungkan all movie_rate dengan dataframe movies berdasarkan movieId"""

all_movie_name = pd.merge(all_movie_rate, movies[['movieId','title','genres']], on='movieId', how='left')
all_movie_name

"""Menggabungkan dataframe tags dengan all_movie_name berdasarkan movieId dan memasukkannya ke dalam variabel all_movie"""

# Menggabungkan dataframe genres dengan all_movie_name dan memasukkannya ke dalam variabel all_movie
all_movie = pd.merge(all_movie_name, tags[['movieId','tag']], on='movieId', how='left')
all_movie

"""## Data Preparation


### Mengatasi Missing Value
Mencari data apakah ada data kosong atau tidak
"""

all_movie.isnull().sum()

"""ternyata dari data diatas terdapat data kosong pada kolom tag yaitu 52549, maka dilakukanlah pembersihan missing value dengan fungsi dropna()"""

all_movie_clean = all_movie.dropna()
all_movie_clean

"""data di atas beruabh menjadi 233213 baris yang awalnya 285762 baris.
cek kembali missing value pada variabel all_movie_clean

"""

all_movie_clean.isnull().sum()

"""Mengurutkan movie berdasarkan movieId kemudian memasukkannya ke dalam variabel fix_movie"""

fix_movie = all_movie_clean.sort_values('movieId', ascending=True)
fix_movie

"""Mengecek berapa jumlah fix_movie"""

len(fix_movie.movieId.unique())

"""Membuat variabel preparation yang berisi dataframe fix_movie kemudian mengurutkan berdasarkan movieId"""

preparation = fix_movie
preparation.sort_values('movieId')

"""Selanjutnya, gunakan data unik untuk dimasukkan ke dalam proses pemodelan.
serta hapus data duplicate dengan fungsi drop_duplicates() berdasarkan movieId
"""

# Membuang data duplikat pada variabel preparation
preparation = preparation.drop_duplicates('movieId')
preparation

"""Selanjutnya,  melakukan konversi data series menjadi list. Dalam hal ini, menggunakan fungsi tolist() dari library numpy. Implementasikan"""

# Mengonversi data series ‘movieId’ menjadi dalam bentuk list
movie_id = preparation['movieId'].tolist()

# Mengonversi data series ‘title’ menjadi dalam bentuk list
movie_name = preparation['title'].tolist()

# Mengonversi data series ‘genres’ menjadi dalam bentuk list
movie_genre = preparation['genres'].tolist()

print(len(movie_id))
print(len(movie_name))
print(len(movie_genre))

"""membuat dictionary untuk menentukan pasangan key-value pada data movie_id, movie_name, dan movie_genre yang telah disiapkan sebelumnya."""

# Membuat dictionary untuk data ‘movie_id’, ‘movie_name’, dan ‘movie_genre’
movie_new = pd.DataFrame({
    'id': movie_id,
    'movie_name': movie_name,
    'genre': movie_genre
})
movie_new

"""## Modeling and Result

- Proses modeling yang saya lakukan pada data ini adalah dengan membuat algoritma machine learning, yaitu content based filtering dan collabrative filtering. untuk algoritma content based filtering saya buat dengan apa yang disukai pengguna pada masa lalu, sedangkan untuk content based filtering, saya buat dengan memanfaatkan tingkat rating dari movie tersebut.


1. Model Development dengan Content Based Filtering


 menggukan fungsi TFIDFVectorizer()

"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data genre
tf.fit(movie_new['genre'])

# Mapping array dari fitur index integer ke fitur nama
feature_names = tf.get_feature_names_out()
print(feature_names)

"""Selanjutnya, lakukan fit dan transformasi ke dalam bentuk matriks."""

tfidf_matrix = tf.fit_transform(movie_new['genre'])
tfidf_matrix.shape

"""
 menghasilkan vektor tf-idf dalam bentuk matriks, menggunakan fungsi todense()."""

tfidf_matrix.todense()

"""lihat matriks tf-idf untuk beberapa movie (movie_name) dan genre"""

import pandas as pd

# Assuming tfidf_matrix is already created by transforming the genre data with tfidf
tfidf_matrix = tf.transform(movie_new['genre'])

# Create the DataFrame with the correct method
df = pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),  # Use get_feature_names_out() instead
    index=movie_new['movie_name']
)

# Display a random sample of 10 rows and 22 columns
df.sample(22, axis=1).sample(10, axis=0)

""" **Cosine Similarity**
 menghitung derajat kesamaan (similarity degree) antar movie dengan teknik cosine similarity.
"""

from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

"""Membuat dataframe dari variabel cosine_sim_df dengan baris dan kolom berupa nama movie, serta melihat kesamaan matrix dari setiap movie"""

cosine_sim_df = pd.DataFrame(cosine_sim, index=movie_new['movie_name'], columns=movie_new['movie_name'])
print('Shape:', cosine_sim_df.shape)

cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""## Mendapatkan Rekomendasi
 membuat fungsi movie_recommendations dengan beberapa parameter sebagai berikut:

- Nama_movie : Nama judul dari movie tersebut (index kemiripan dataframe).  
- Similarity_data : Dataframe mengenai similarity yang telah kita didefinisikan sebelumnya
- Items : Nama dan fitur yang digunakan untuk mendefinisikan kemiripan, dalam hal ini adalah ‘movie_name’ dan ‘genre’.  
- k : Banyak rekomendasi yang ingin diberikan.  



"""

def movie_recommendations(nama_movie, similarity_data=cosine_sim_df, items=movie_new[['movie_name', 'genre']], k=5):


    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,nama_movie].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama_movie agar nama movie yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama_movie, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

"""
 terapkan kode di atas untuk menemukan rekomendasi movie yang mirip dengan Jumanji (1995)."""

movie_new[movie_new.movie_name.eq('Jumanji (1995)')]

"""dari hasil di atas dapat dilihat bahwa pengguna menyukai movie yang berjudul jumanji (1995) yang bergenre Adventure, Children, Fantasy.  
Mendapatkan rekomendasi movie yang mirip dengan Jumanji (1995).


"""

movie_recommendations('Jumanji (1995)')

"""Dari hasil rekomendasi di atas, diketahui bahwa Jumanji (1995) termasuk ke dalam genre  Adventure|Children|Fantasy. Dari 5 item yang direkomendasikan, 3 item memiliki genre Adventure|Children|Fantasy (similar). Artinya, precision sistem kita sebesar 3/5 atau 60%.

2. Model Development dengan Collaborative Filtering

Import semua library yang dibutuhkan
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path
import matplotlib.pyplot as plt

"""ubah nama variabel ratings yang telah dibuat sebelumnya menjadi df."""

df = ratings
df

"""## Data Preparation
melakukan tahapan prepocessing
"""

# Mengubah userID menjadi list tanpa nilai yang sama
user_ids = df['userId'].unique().tolist()
print('list userID: ', user_ids)

# Melakukan encoding userID
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded userID : ', user_to_user_encoded)

# Melakukan proses encoding angka ke ke userID
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke userID: ', user_encoded_to_user)

"""Selanjutnya, lakukan hal yang sama pada fitur ‘movieId’."""

# Mengubah movieId menjadi list tanpa nilai yang sama
movie_ids = df['movieId'].unique().tolist()

# Melakukan proses encoding movieId
movie_to_movie_encoded = {x: i for i, x in enumerate(movie_ids)}

# Melakukan proses encoding angka ke movieId
movie_encoded_to_movie = {i: x for i, x in enumerate(movie_ids)}

# Selanjutnya, petakan userId dan movieId ke dataframe yang berkaitan.

# Mapping userId ke dataframe genres
df['genres'] = df['userId'].map(user_to_user_encoded)

# Mapping movieD ke dataframe movies
df['movies'] = df['movieId'].map(movie_to_movie_encoded)

"""Terakhir, cek beberapa hal dalam data seperti jumlah user, jumlah movie, dan mengubah nilai rating menjadi float, cek nilai minimum dan maximum"""

num_users = len(user_to_user_encoded)
print(num_users)

num_movie = len(movie_encoded_to_movie)
print(num_movie)

df['ratings'] = df['rating'].values.astype(np.float32)

min_rating = min(df['rating'])

max_rating = max(df['rating'])

print('Number of User: {}, Number of movie: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_movie, min_rating, max_rating
))

"""**Membagi Data untuk Training dan Validasi**

"""

# Mengacak dataset
df = df.sample(frac=1, random_state=42)
df

"""membagi data train dan validasi dengan komposisi 80:20."""

# Membuat variabel x untuk mencocokkan data genres  dan movies menjadi satu value
x = df[['genres', 'movies']].values

# Membuat variabel y untuk membuat ratings dari hasil
y = df['ratings'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * df.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

"""lakukan proses training

"""

class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_movie, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_movie = num_movie
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.movie_embedding = layers.Embedding( # layer embeddings movies
        num_movie,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.movie_bias = layers.Embedding(num_movie, 1) # layer embedding movies bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    movie_vector = self.movie_embedding(inputs[:, 1]) # memanggil layer embedding 3
    movie_bias = self.movie_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_movie = tf.tensordot(user_vector, movie_vector, 2)

    x = dot_user_movie + user_bias + movie_bias

    return tf.nn.sigmoid(x) # activation sigmoid

"""## Evaluation
Selanjutnya, lakukan proses compile terhadap model. serta menggunakan matrix evaluasi RMSE


"""

model = RecommenderNet(num_users, num_movie, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""Memulai proses training dengan batch size sebesar 64 serta epoch 100 kali"""

# Memulai training

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 64,
    epochs = 100,
    validation_data = (x_val, y_val)
)

"""**Visualisasi Metrik**  
Untuk melihat visualisasi proses training
"""

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""dari visualisasi proses training model di atas cukup smooth dan model konvergen pada epochs sekitar 100. Dari proses ini, kita memperoleh nilai error akhir sebesar sekitar 0.19 dan error pada data validasi sebesar 0.20.

***Mendapatkan Rekomendasi movie***
"""

movie_df = movie_new
df = pd.read_csv('movie-recommendation-data/ml-latest-small/ratings.csv')


user_id = df.userId.sample(1).iloc[0]
movie_watched_by_user = df[df.userId == user_id]


movie_not_watched = movie_df[~movie_df['id'].isin(movie_watched_by_user.movieId.values)]['id']
movie_not_watched = list(
    set(movie_not_watched)
    .intersection(set(movie_to_movie_encoded.keys()))
)

movie_not_watched = [[movie_to_movie_encoded.get(x)] for x in movie_not_watched]
user_encoder = user_to_user_encoded.get(user_id)
user_movie_array = np.hstack(
    ([[user_encoder]] * len(movie_not_watched), movie_not_watched)
)

"""untuk memperoleh rekomendasi movies, gunakan fungsi model.predict() dari library Keras dengan menerapkan kode berikut."""

ratings = model.predict(user_movie_array).flatten()

top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_movie_ids = [
    movie_encoded_to_movie.get(movie_not_watched[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('movie with high ratings from user')
print('----' * 8)

top_movie_user = (
    movie_watched_by_user.sort_values(
        by = 'rating',
        ascending=False
    )
    .head(5)
    .movieId.values
)

movie_df_rows = movie_df[movie_df['id'].isin(top_movie_user)]
for row in movie_df_rows.itertuples():
    print(row.movie_name, ':', row.genre)

print('----' * 8)
print('Top 10 movie recommendation')
print('----' * 8)

recommended_movie = movie_df[movie_df['id'].isin(recommended_movie_ids)]
for row in recommended_movie.itertuples():
    print(row.movie_name, ':', row.genre)

"""dari hasi di atas movie yang bergenre comedy menjadi movie yang paling tinggi ratingsnya. Kemudian top 10 movie yang direkomendasikan sistem adalah movie dengan genre comedy dan drama."""