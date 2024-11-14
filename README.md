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

Dataset yang digunakan dalam proyek ini adalah **Movie Recommendation Data** yang diambil dari Kaggle. Dataset ini berisi informasi tentang film, rating yang diberikan oleh pengguna, serta metadata lain seperti genre film dan tautan terkait.

Beberapa variabel yang terdapat dalam dataset ini adalah:

- **links**: Tautan ke sumber daya terkait dengan film.
- **movies**: Informasi tentang film, seperti judul, genre, dll.
- **ratings**: Rating yang diberikan oleh pengguna terhadap film.
- **tags**: Kata kunci atau genre yang terkait dengan film tersebut.

Proses pertama dalam pengolahan data adalah **Exploratory Data Analysis (EDA)**, di mana saya menganalisis hubungan antar variabel untuk memahami pola dan distribusi data. Setelah itu, saya menggabungkan data berdasarkan **movieId** untuk film dan **userId** untuk pengguna, sehingga informasi terkait film dan rating bisa diintegrasikan.

### Data Preparation

Proses persiapan data yang dilakukan adalah sebagai berikut:

- **Mengatasi Missing Values**: Memeriksa data yang hilang atau kosong. Jika ada data yang kosong, saya menghapusnya untuk memastikan kualitas data yang digunakan dalam model.
- **Pembagian Data**: Membagi data menjadi dua set, yaitu **data pelatihan** dan **data validasi**, untuk melatih model dan menguji kinerjanya.
- **Penggabungan Variabel**: Menggabungkan beberapa variabel yang relevan berdasarkan ID unik, seperti **movieId** dan **userId**.
- **Pengurutan Data**: Menyusun data berdasarkan **movieId** dalam urutan menaik untuk mempermudah proses pemodelan.
- **Penghapusan Duplikasi**: Menghapus data yang terduplikasi agar tidak mempengaruhi hasil analisis dan model.
- **Konversi Data ke Format List**: Mengubah data menjadi format list agar dapat diproses lebih mudah oleh algoritma.
- **Pembuatan Dictionary**: Membuat struktur data berbentuk kamus untuk memudahkan pencarian berdasarkan ID.
- **Penggunaan TfidfVectorizer**: Menggunakan teknik pembobotan untuk teks (seperti deskripsi film atau genre) untuk menghitung kemiripan antar film.
- **Preprocessing**: Mengatasi masalah yang mungkin ada dalam data seperti teks yang tidak konsisten, noise, atau format yang salah.
- **Mapping Data**: Mencocokkan data untuk memastikan semua variabel sesuai dengan format yang dibutuhkan oleh model.

### Modeling and Results

Dalam tahap pemodelan, saya menggunakan dua algoritma utama:

1. **Content-Based Filtering**: Algoritma ini merekomendasikan film kepada pengguna berdasarkan genre atau karakteristik dari film yang telah mereka tonton atau beri rating tinggi sebelumnya. Sistem ini memperhitungkan hubungan antara film yang sudah disukai oleh pengguna dan film lain yang memiliki kesamaan.
   
2. **Collaborative Filtering**: Algoritma ini memberikan rekomendasi berdasarkan kesukaan pengguna lain yang memiliki pola preferensi serupa. Sistem ini menggunakan data rating untuk menemukan pola-pola umum di antara pengguna yang berbeda.

#### Hasil Content-Based Filtering
Jika pengguna menyukai film seperti **Jumanji (1995)** yang bergenre **Adventure, Children, Fantasy**, sistem akan merekomendasikan film serupa dengan genre yang sama. 

![output-cbf-1user](https://github.com/user-attachments/assets/23efadf2-a231-4013-8306-bd7b25e811c6)


Top 5 rekomendasi film yang diberikan oleh sistem berdasarkan algoritma Content-Based Filtering adalah sebagai berikut:

![output-cbf-2recommend](https://github.com/user-attachments/assets/6e99a0d3-a5fe-4491-989e-1ae97afb72ec)


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
