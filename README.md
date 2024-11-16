### Project Overview

Sistem rekomendasi film adalah teknologi yang digunakan untuk memberikan saran film kepada pengguna berdasarkan preferensi mereka, yang diterapkan pada platform streaming seperti Netflix, IQIYI, dan WeTV. Dalam proyek ini, saya mengembangkan sistem rekomendasi yang memanfaatkan dua pendekatan utama: **Content-Based Filtering** dan **Collaborative Filtering**, yang bertujuan untuk memberikan saran film yang relevan berdasarkan rating dan aktivitas pengguna di masa lalu.

Di era modern ini, sistem rekomendasi menjadi sangat penting untuk mengatasi masalah informasi berlebihan, dengan menyarankan produk yang relevan dan personal. Untuk media seperti film, sistem rekomendasi berbasis kolaborasi berusaha membantu pengguna menemukan film berdasarkan kesukaan orang lain yang memiliki pola preferensi serupa. Namun, sistem ini harus menghadapi tantangan data yang jarang, di mana dengan bertambahnya jumlah pengguna dan film, sulit untuk menemukan pengguna yang memiliki pola kesukaan yang sangat mirip.

Referensi terkait proyek ini dapat ditemukan dalam artikel di [Journal of Visual Languages & Computing](https://www.sciencedirect.com/science/article/abs/pii/S1045926X14000901).

### Business Understanding

#### Problem Statements
Bagaimana cara merekomendasikan film yang disukai oleh pengguna kepada pengguna lain yang belum menonton film tersebut, dengan tingkat akurasi yang tinggi?

#### Goals
Tujuan utama dari proyek ini adalah untuk mengembangkan sistem rekomendasi yang dapat memberikan saran film berdasarkan rating dan aktivitas pengguna di masa lalu, sehingga pengguna dapat menemukan film yang relevan dengan preferensi mereka.

#### Solution Approach
Pendekatan yang saya gunakan dalam proyek ini mengintegrasikan dua algoritma pembelajaran mesin, yaitu:

1. **Content-Based Filtering**: Algoritma ini merekomendasikan film berdasarkan kesukaan pengguna sebelumnya, dengan memperhatikan genre atau karakteristik lain dari film yang telah ditonton atau diberikan rating tinggi oleh pengguna.
   
2. **Collaborative Filtering**: Algoritma ini mengandalkan pola kesukaan yang ada di komunitas pengguna. Dengan menggunakan informasi rating dari banyak pengguna, sistem ini memberikan rekomendasi film berdasarkan apa yang disukai oleh pengguna lain yang memiliki pola kesukaan serupa, tanpa memerlukan informasi detail tentang film tersebut.

### Data Understanding
- **Links dataset**: 
  - Jumlah baris: 9,742
  - Jumlah kolom: 3
  - Dataset ini berisi informasi tentang ID film dan ID eksternal lainnya (misalnya, IMDb ID).
  
- **Movies dataset**: 
  - Jumlah baris: 9,742
  - Jumlah kolom: 3
  - Dataset ini berisi ID film, judul, dan genre film.

- **Ratings dataset**: 
  - Jumlah baris: 100,836
  - Jumlah kolom: 4
  - Dataset ini berisi rating yang diberikan oleh pengguna, dengan kolom `movieId`, `userId`, `rating`, dan `timestamp`.

- **Tags dataset**: 
  - Jumlah baris: 3,683
  - Jumlah kolom: 4
  - Dataset ini berisi tag yang diberikan oleh pengguna untuk setiap film, dengan kolom `movieId`, `userId`, `tag`, dan `timestamp`.

**Jumlah Data (Baris dan Kolom)**
- Terdapat **45.5 ribu baris data** yang mewakili setiap film, dan sejumlah kolom yang mencakup berbagai atribut dari setiap film.

**Kondisi Data**
- **Missing Values**: Ada beberapa atribut dengan nilai yang hilang. Contoh:
  - **belongs_to_collection**: 90% data kosong (tidak masuk koleksi).
  - **homepage**: 83% data kosong.
  - **overview**: 2% data kosong.
  - **imdb_id**: 17 baris tidak memiliki nilai.
- **Duplicate Values**: Berdasarkan informasi ini, tidak disebutkan adanya nilai duplikat dalam dataset.

**Tautan Sumber Data**
- Tautan sumber data dapat diunduh dari sumber resmi **Kaggle**  [disini](https://www.kaggle.com/datasets/rohan4050/movie-recommendation-data).

**Uraian Seluruh Fitur pada Data**

1. **adult**: Menunjukkan apakah film memiliki konten dewasa. Nilai `true` (dewasa) hanya muncul pada 9 baris (0%), sedangkan `false` pada 45,454 baris (100%).
   
2. **belongs_to_collection**: Menunjukkan apakah film termasuk dalam suatu koleksi atau seri. Sekitar 90% data tidak memiliki informasi ini (`null`), sedangkan 10% lainnya memiliki koleksi tertentu, seperti “The Bowery Boys.”
   
3. **budget**: Menampilkan anggaran produksi film, yang umumnya berkisar dari $0 hingga $380 juta. Rata-rata anggaran adalah $4.22 juta dengan deviasi standar $17.4 juta.

4. **genres**: Daftar genre yang dimiliki oleh setiap film, seperti Drama (11%) dan Komedi (8%). Ada 4,069 kombinasi genre unik dalam dataset ini.

5. **homepage**: URL yang mengarahkan ke halaman utama film jika tersedia. Sekitar 83% data kosong untuk atribut ini, dengan sebagian besar data yang tersedia memiliki URL unik.

6. **id**: Identifikasi numerik unik untuk setiap film. Data ini beragam mulai dari 2 hingga 469 ribu, dengan rata-rata ID sebesar 108 ribu.

7. **imdb_id**: ID unik untuk setiap film dalam format IMDb, dengan 45.4 ribu nilai unik dan beberapa nilai yang kosong.

8. **original_language**: Bahasa utama yang digunakan dalam film, dengan bahasa Inggris (71%) paling dominan, diikuti oleh bahasa Prancis (5%).

9. **original_title**: Judul asli dari setiap film, dengan 43.4 ribu judul unik.

10. **overview**: Deskripsi singkat atau sinopsis film, dengan sekitar 2% data yang hilang dan “No overview found” sebagai deskripsi paling umum.

Proses pertama dalam pengolahan data adalah **Exploratory Data Analysis (EDA)**, di mana saya menganalisis hubungan antar variabel untuk memahami pola dan distribusi data. Setelah itu, saya menggabungkan data berdasarkan **movieId** untuk film dan **userId** untuk pengguna, sehingga informasi terkait film dan rating bisa diintegrasikan.

### Data Preparation
#### 1. Penanganan Data Kosong dan Duplikat  
- Dilakukan pengecekan nilai kosong pada dataset menggunakan metode `isnull().sum()`. Semua baris yang memiliki nilai kosong dihapus menggunakan `dropna()`.  
- Dataset diurutkan berdasarkan kolom `movieId` secara ascending menggunakan `sort_values()`.  
- Data duplikat dihapus dengan menggunakan metode `drop_duplicates()` pada kolom `movieId`.

#### 2. Konversi Kolom menjadi List  
- Kolom `movieId`, `title`, dan `genres` dikonversi menjadi list menggunakan metode `tolist()`.  
- Data ini kemudian disusun ulang menjadi DataFrame baru dengan nama kolom `id`, `movie_name`, dan `genre`.

#### 3. Encoding `userId` dan `movieId`  
- Kolom `userId` diubah menjadi list unik menggunakan metode `unique()`. Dilakukan encoding dengan membuat mapping `userId` ke nilai numerik dan sebaliknya.  
- Kolom `movieId` juga diubah menjadi list unik, lalu dilakukan encoding serupa dengan mapping ke nilai numerik dan sebaliknya.  

#### 4. Mapping Nilai yang Sudah Di-encode ke DataFrame  
- Hasil encoding `userId` dimasukkan ke kolom `genres`, dan encoding `movieId` dimasukkan ke kolom `movies` pada dataset utama untuk memastikan konsistensi data.

#### 5. Normalisasi Kolom `rating`  
- Kolom `rating` diubah menjadi tipe data `float32`. Nilai `rating` dinormalisasi menggunakan rumus `(rating - min_rating) / (max_rating - min_rating)`, dengan `min_rating` dan `max_rating` merupakan nilai minimum dan maksimum dari kolom `rating`.

#### 6. Pemrosesan Data dengan TF-IDF  
- Kolom `genres` diubah menjadi representasi numerik menggunakan teknik TF-IDF (Term Frequency-Inverse Document Frequency).  
- Teknik ini digunakan untuk memproses teks dalam kolom `genres` agar dapat digunakan dalam model pembelajaran mesin.

#### 7. Pengacakan Dataset  
- Dataset diacak menggunakan metode `sample(frac=1, random_state=42)` untuk memastikan data terdistribusi secara acak namun tetap dapat direproduksi dengan nilai `random_state`.

#### 8. Pembagian Dataset  
- Dataset dibagi menjadi data latih dan data validasi. Sebanyak 80% data digunakan sebagai data latih, dan 20% sebagai data validasi.  
- Pemisahan dilakukan pada variabel fitur (`x`) yang merupakan gabungan kolom `genres` dan `movies`, serta target (`y`) yang merupakan kolom `ratings`. 

#### 9. Ringkasan Data  
- Jumlah pengguna unik (`userId`): **`num_users`**  
- Jumlah film unik (`movieId`): **`num_movie`**  
- Rating minimum: **`min_rating`**  
- Rating maksimum: **`max_rating`**

#### 10. Dataset Siap untuk Model  
Setelah proses di atas, dataset telah siap untuk digunakan dalam pembuatan model pembelajaran mesin dengan data yang telah dibersihkan, diencoding, dinormalisasi, serta dibagi untuk data latih dan data validasi.

Pada tahap Data Preparation ini, terdapat dua pendekatan utama dalam pemrosesan data: **Content-Based Filtering** dan **Collaborative Filtering**. Proses yang dilakukan mencakup pembersihan data, penggabungan data, pengurutan data, dan penghapusan duplikasi. 

### 1. Content-Based Filtering

#### Menggabungkan Data
Proses pertama yang dilakukan adalah menggabungkan data berdasarkan ID unik. Data yang digunakan adalah dataset yang berisi informasi tentang film dan rating yang diberikan oleh pengguna.


```python
movie_all = np.concatenate((
    links.movieId.unique(),
    movies.movieId.unique(),
    ratings.movieId.unique(),
    tags.movieId.unique(),
))
```

#### Mengatasi Missing Values
Setelah menggabungkan data, langkah selanjutnya adalah memeriksa missing values dalam dataset. Kolom yang ditemukan memiliki missing value adalah kolom `tag`, dan langkah yang dilakukan adalah menghapus baris yang memiliki nilai kosong.

```python
all_movie_clean = all_movie.dropna()
```

Setelah pembersihan, seluruh kolom dalam dataset `all_movie_clean` tidak mengandung nilai kosong.

#### Mengurutkan Data
Setelah pembersihan data, langkah selanjutnya adalah mengurutkan dataset berdasarkan `movieId` untuk mempermudah analisis lebih lanjut. Hasil dari pengurutan ini disalin ke dalam variabel `fix_movie`.

```python
fix_movie = all_movie_clean.sort_values('movieId', ascending=True)
```

Hasilnya adalah dataset yang telah diurutkan dengan 233,213 baris.

#### Menghapus Duplikasi
Langkah berikutnya adalah menghapus duplikasi pada dataset berdasarkan kolom `movieId`. Hal ini penting untuk memastikan bahwa setiap film hanya muncul satu kali dalam dataset, yang disalin ke dalam variabel `preparation`.

```python
preparation = fix_movie.drop_duplicates('movieId')
```

Jumlah data yang tersisa setelah penghapusan duplikat adalah 1,554 baris.

### 2. Collaborative Filtering

#### Konversi Data Menjadi List
Setelah data siap, langkah selanjutnya adalah mengonversi kolom `movieId`, `title`, dan `genres` menjadi list. Hal ini memungkinkan pemrosesan data yang lebih efisien dalam algoritma collaborative filtering.

```python
movie_id = preparation['movieId'].tolist()
movie_name = preparation['title'].tolist()
movie_genre = preparation['genres'].tolist()
```

Jumlah elemen dalam masing-masing list adalah 1,554, sesuai dengan jumlah data unik yang ada.

#### Pembuatan Dictionary
Pada tahap ini, dibuatkan sebuah dictionary untuk memetakan `movieId`, `movie_name`, dan `genres` dalam format DataFrame. Ini akan memudahkan pencarian dan pemrosesan data lebih lanjut.

```python
movie_new = pd.DataFrame({
    'id': movie_id,
    'movie_name': movie_name,
    'genre': movie_genre
})
```

Dataset `movie_new` ini terdiri dari 1,554 baris dan 3 kolom, yaitu `id`, `movie_name`, dan `genre`, yang siap digunakan dalam tahap pemodelan.

#### Sub bab data preparation 
1. **Mengubah userID menjadi list tanpa nilai yang sama**
   Langkah pertama adalah mengubah kolom `userId` menjadi sebuah list yang hanya berisi nilai unik. Ini dilakukan untuk mempermudah proses encoding user ID dalam tahap selanjutnya.

   ```python
   user_ids = df['userId'].unique().tolist()
   ```

   Setelah langkah ini, dihasilkan sebuah list yang berisi ID pengguna yang unik, yang mencakup nilai dari 1 hingga 610, sebagaimana ditunjukkan di bawah ini.

   ```plaintext
   list userID:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., 610]
   ```

2. **Melakukan Encoding userID**
   Setelah memperoleh daftar user ID yang unik, langkah berikutnya adalah melakukan encoding terhadap `userId` menjadi angka. Proses ini memungkinkan algoritma untuk memproses data secara lebih efisien.

   ```python
   user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
   ```

   Hasilnya adalah sebuah dictionary yang memetakan setiap `userId` yang unik menjadi sebuah angka yang sesuai, seperti berikut:

   ```plaintext
   encoded userID:  {1: 0, 2: 1, 3: 2, ..., 610: 609}
   ```

3. **Melakukan Proses Encoding Angka ke userID**
   Langkah selanjutnya adalah membuat dictionary untuk mengonversi angka kembali ke `userId` yang sesuai. Hal ini diperlukan saat kita ingin memetakan hasil prediksi kembali ke ID pengguna asli.

   ```python
   user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
   ```

   Dengan cara ini, setiap angka yang di-encode dapat dikembalikan ke ID pengguna asli.

   ```plaintext
   encoded angka ke userID:  {0: 1, 1: 2, 2: 3, ..., 609: 610}
   ```
Pada tahap Data Preparation ini, dilakukan serangkaian langkah untuk mempersiapkan data, baik untuk **Content-Based Filtering** maupun **Collaborative Filtering**. Proses yang dilakukan meliputi pembersihan data, pengurutan, penghapusan duplikasi, konversi data ke dalam format yang lebih efisien, dan pembuatan struktur data yang siap digunakan dalam model rekomendasi. Dengan data yang sudah siap, tahap berikutnya adalah memulai pemodelan menggunakan kedua pendekatan tersebut.

### Model Development and Results
#### **1. Content-Based Filtering**

Pendekatan Content-Based Filtering digunakan untuk memberikan rekomendasi film berdasarkan genre film yang pernah disukai oleh pengguna. 

1. **Representasi Data Genre**  
   Model memanfaatkan metode TF-IDF (*Term Frequency-Inverse Document Frequency*) untuk merepresentasikan genre film dalam bentuk vektor. Setiap genre dalam dataset diubah menjadi nilai-nilai bobot yang menunjukkan pentingnya setiap genre dalam data film tersebut. TF-IDF Vectorizer mengidentifikasi 24 fitur unik yang merepresentasikan genre di dalam dataset ini, termasuk genre seperti 'action', 'comedy', 'fantasy', dan lainnya.

2. **Pengukuran Kemiripan Antar Film**  
   Setelah data genre diubah menjadi vektor, model menghitung kemiripan antar film menggunakan *cosine similarity*. Hasilnya adalah sebuah matriks berukuran 1554 x 1554, di mana setiap elemen matriks menunjukkan nilai kemiripan antara sepasang film berdasarkan genre mereka. Nilai kemiripan berkisar antara 0 (tidak mirip sama sekali) hingga 1 (sangat mirip).

3. **Penyusunan Rekomendasi**  
   Berdasarkan matriks kemiripan, model mengambil lima film dengan skor kemiripan tertinggi sebagai rekomendasi. Model juga memastikan bahwa film yang direkomendasikan tidak termasuk film awal yang digunakan sebagai input.  

    ![output-cbf-1user](https://github.com/user-attachments/assets/23efadf2-a231-4013-8306-bd7b25e811c6)

   Sebagai contoh, rekomendasi untuk film "Jumanji (1995)" menghasilkan film-film dengan genre yang sama, seperti:

   ![output-cbf-2recommend](https://github.com/user-attachments/assets/6e99a0d3-a5fe-4491-989e-1ae97afb72ec)
   
**Parameter Model**:  
- *TF-IDF Vectorizer*: Tidak menggunakan *stopwords* dan menggunakan semua fitur unik yang terdapat pada genre film.
- *Cosine Similarity*: Digunakan untuk mengukur kesamaan antar film berdasarkan vektor genre yang dihasilkan.
- Jumlah rekomendasi (*k*): Menyediakan 5 film dengan skor kemiripan tertinggi sebagai rekomendasi.

Hasil rekomendasi menunjukkan bahwa model berhasil menemukan film yang genre-nya serupa, memberikan pengalaman menonton yang sesuai dengan preferensi film awal pengguna.

#### 2. **Collaborative Filtering**
Pendekatan Collaborative Filtering dilakukan menggunakan model *neural network* berbasis *embedding* untuk memberikan rekomendasi film berdasarkan preferensi pengguna dan film yang pernah mereka nilai. 

1. **Arsitektur Model**  
   Model ini dirancang dengan menggunakan kelas khusus bernama `RecommenderNet`, yang berisi beberapa lapisan embedding. Lapisan embedding ini memungkinkan model untuk memetakan informasi pengguna dan film ke dalam vektor berdimensi tertentu (embedding) yang dapat membantu menangkap pola kesukaan antar pengguna dan film berdasarkan data rating yang tersedia. Model terdiri dari empat lapisan embedding utama:
   
   - **User Embedding**: Mewakili setiap pengguna dalam bentuk vektor embedding dengan ukuran tertentu (*embedding_size*).
   - **User Bias**: Lapisan bias untuk pengguna, yang menambahkan nilai bias pada setiap embedding pengguna untuk mengakomodasi perbedaan rata-rata rating antar pengguna.
   - **Movie Embedding**: Mewakili setiap film dalam bentuk vektor embedding.
   - **Movie Bias**: Lapisan bias untuk setiap film yang menyesuaikan rating rata-rata tiap film.

2. **Proses Perhitungan Skor Rekomendasi**  
   Pada saat pemanggilan (*call*), model menerima input yang berupa pasangan (pengguna, film). Tahapan perhitungan skor rekomendasi dilakukan sebagai berikut:
   
   - Model memanggil embedding dari lapisan `user_embedding` dan `movie_embedding` untuk setiap pasangan pengguna dan film.
   - Hasil embedding pengguna dan film kemudian dikalikan dengan operasi *dot product* untuk mendapatkan skor awal.
   - Model menambahkan nilai bias dari `user_bias` dan `movie_bias` ke skor awal untuk menyesuaikan prediksi rating agar lebih akurat.
   - Aktivasi *sigmoid* digunakan pada hasil akhir untuk membatasi nilai keluaran dalam rentang 0 hingga 1, memberikan perkiraan probabilitas kecocokan antara pengguna dan film.

3. **Parameter Model**
   
   - **Jumlah Pengguna** (*num_users*): Jumlah unik pengguna yang terdapat dalam dataset.
   - **Jumlah Film** (*num_movie*): Jumlah unik film yang terdapat dalam dataset.
   - **Ukuran Embedding** (*embedding_size*): Ukuran vektor embedding yang dipilih untuk representasi pengguna dan film.  
   - **Regularisasi L2**: Untuk mengurangi risiko *overfitting*, lapisan embedding diinisialisasi dengan regularisasi L2 sebesar 1e-6. Ini membantu menjaga bobot dalam skala yang stabil.

Model ini memanfaatkan informasi dari seluruh pengguna dan rating yang diberikan untuk menemukan pola umum dalam preferensi pengguna terhadap berbagai film.

#### Hasil Collaborative Filtering
Sistem juga memberikan rekomendasi berdasarkan rating yang diberikan oleh pengguna lain. Berdasarkan rating tinggi, film dengan genre **Comedy** dan **Drama** muncul sebagai rekomendasi utama.

![output-ccf](https://github.com/user-attachments/assets/d17cfaac-d0bc-41a4-a4a9-74ef1f64325e)


### Evaluation

#### Evaluasi Content-Based Filtering
Evaluasi dilakukan dengan menggunakan **Precision**, yang mengukur akurasi rekomendasi. Dalam hal ini, jika film **Jumanji (1995)** disukai oleh pengguna, maka sistem akan memeriksa seberapa banyak dari rekomendasi yang diberikan memiliki genre serupa.

Precision dihitung dengan rumus:

![dos_819311f78d87da1e0fd8660171fa58e620211012160253 (1)](https://github.com/user-attachments/assets/909cd185-5b03-45fb-a4cd-c18402443f7f)



Jika tiga dari lima rekomendasi memiliki genre yang serupa, precision sistem adalah 60%.

#### Evaluasi Collaborative Filtering
Untuk Collaborative Filtering, evaluasi dilakukan menggunakan **Root Mean Squared Error (RMSE)**. RMSE mengukur seberapa akurat model dalam memprediksi rating yang diberikan oleh pengguna.

Formula RMSE adalah:

![rumusRMSE](https://github.com/user-attachments/assets/21642acc-6e80-448d-9c50-9a59ea221c67)


Di mana:
- \( A_i \) adalah nilai aktual
- \( P_i \) adalah nilai yang diprediksi
- \( N \) adalah jumlah data

![hasilmodelmatric](https://github.com/user-attachments/assets/808c8017-fea4-4323-9f76-ed42d5c7e238)

Semakin kecil nilai RMSE, semakin akurat model tersebut. Dalam evaluasi ini, model menghasilkan RMSE sekitar 0.19 untuk data pelatihan dan 0.20 untuk data validasi, yang menunjukkan akurasi yang cukup baik.

Proses pelatihan model menunjukkan bahwa model konvergen dalam sekitar 100 epoch, dengan error yang semakin mengecil, menunjukkan bahwa model berhasil mengurangi kesalahan prediksi secara signifikan.

**Bagaimana cara merekomendasikan film yang disukai oleh pengguna kepada pengguna lain yang belum menonton film tersebut dengan tingkat akurasi yang tinggi.**

Model yang dikembangkan berhasil menjawab permasalahan ini dengan mengintegrasikan **Content-Based Filtering** dan **Collaborative Filtering**, yang keduanya memberikan rekomendasi film berdasarkan preferensi pengguna dan pola kesukaan pengguna lain. Evaluasi menggunakan **Precision** dan **RMSE** menunjukkan bahwa kedua model ini dapat memberikan rekomendasi yang relevan dan akurat, dengan **Precision** yang cukup tinggi dan **RMSE** yang rendah.

- **Content-Based Filtering** memberikan rekomendasi berdasarkan genre film yang serupa dengan yang telah disukai oleh pengguna, sedangkan
- **Collaborative Filtering** merekomendasikan film berdasarkan kesamaan rating antara pengguna.

Kedua pendekatan ini saling melengkapi dan mengarah pada solusi yang lebih akurat untuk memberikan rekomendasi film.

### Apakah Berhasil Mencapai Goals yang Diharapkan?
Goals dari proyek ini adalah untuk mengembangkan sistem rekomendasi yang dapat memberikan saran film yang relevan dengan preferensi pengguna, berdasarkan aktivitas mereka di masa lalu. Berdasarkan hasil evaluasi, model ini berhasil mencapai tujuan tersebut. **Precision** yang cukup tinggi menunjukkan bahwa rekomendasi film yang diberikan cenderung relevan dengan film yang disukai pengguna sebelumnya. Sementara itu, **RMSE** yang rendah mengindikasikan bahwa model dapat memprediksi rating film dengan akurasi yang baik.

Dengan demikian, sistem rekomendasi ini dapat membantu pengguna menemukan film yang sesuai dengan preferensi mereka, baik berdasarkan kesukaan mereka sendiri (Content-Based Filtering) maupun berdasarkan pola kesukaan pengguna lain (Collaborative Filtering).

### Apakah Solusi yang Ditetapkan Berdampak?
Solusi yang digunakan dalam proyek ini memiliki dampak yang signifikan terhadap pengalaman pengguna. Dengan menggabungkan kedua pendekatan **Content-Based Filtering** dan **Collaborative Filtering**, sistem rekomendasi ini lebih fleksibel dan dapat memberikan rekomendasi yang lebih baik untuk berbagai jenis pengguna. Dampaknya terhadap business adalah:

1. **Peningkatan Retensi Pengguna:** Pengguna yang mendapatkan rekomendasi film yang relevan cenderung lebih sering menggunakan aplikasi atau platform, meningkatkan retensi pengguna.
2. **Peningkatan Kepuasan Pengguna:** Dengan rekomendasi yang lebih tepat, pengguna merasa bahwa sistem memahami preferensi mereka, yang dapat meningkatkan kepuasan pengguna.
3. **Optimalisasi Pengalaman Pengguna:** Sistem rekomendasi yang akurat membantu pengguna menemukan film yang lebih sesuai dengan preferensi mereka, meningkatkan engagement dengan platform.

Dengan hasil evaluasi yang menunjukkan akurasi yang baik, model ini dapat dianggap sebagai solusi yang efektif dalam meningkatkan pengalaman pengguna dalam mencari film yang sesuai dengan selera pengguna.
