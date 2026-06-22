# 🤖 Mini Laravel LLM

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![NLP](https://img.shields.io/badge/NLP-Language_Model-green?style=for-the-badge)
![Data Mining](https://img.shields.io/badge/Course-Data_Mining-orange?style=for-the-badge)

### Mini Language Model Berbasis Corpus Laravel Menggunakan Python dan Streamlit

📚 Proyek Mata Kuliah **Data Mining**

🔗 **Demo Aplikasi:** https://minillm-laravel.streamlit.app/

</div>

---

## 📖 Deskripsi Proyek

**Mini Laravel LLM** merupakan proyek sederhana yang mengimplementasikan konsep **Natural Language Processing (NLP)** dan **Language Modeling** menggunakan pendekatan **Statistical Language Model (Markov Chain)**.

Model dilatih menggunakan kumpulan teks (corpus) bertema **Laravel Framework**, kemudian digunakan untuk menghasilkan teks baru berdasarkan kata awal yang diberikan pengguna.

Proyek ini bertujuan untuk memahami konsep dasar:

- Tokenization
- Text Mining
- Language Modeling
- Markov Chain
- Generative Text
- Natural Language Processing (NLP)

---

## 🎯 Tujuan Proyek

- Memahami proses preprocessing teks.
- Mempelajari teknik tokenisasi pada NLP.
- Membangun model generasi teks sederhana.
- Mengimplementasikan konsep Data Mining pada data teks.
- Membuat antarmuka interaktif menggunakan Streamlit.

---

## 🏗️ Arsitektur Sistem

```text
Corpus Laravel
       │
       ▼
Tokenizer
       │
       ▼
Training Model
       │
       ▼
Word Pair (Bigram)
       │
       ▼
Model JSON
       │
       ▼
Streamlit App
       │
       ▼
Text Generation
```

---

## 📂 Struktur Project

```bash
mini_llm/
│
├── corpus/
│   └── laravel_corpus.txt
│
├── models/
│   └── laravel_model.json
│
├── app.py
├── train.py
├── tokenizer.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Cara Kerja Sistem

### 1. Membaca Corpus

Sistem membaca dataset teks Laravel dari file:

```bash
corpus/laravel_corpus.txt
```

---

### 2. Tokenisasi

Tersedia tiga metode tokenisasi:

| Tokenizer | Deskripsi |
|-----------|------------|
| Simple | Memecah teks berdasarkan spasi |
| Regex | Menghapus tanda baca menggunakan Regular Expression |
| NLTK | Menggunakan library NLTK |

---

### 3. Training Model

Sistem membentuk pasangan kata (**Bigram Model**) dengan pola:

```text
kata_sekarang → kata_berikutnya
```

Contoh:

```text
laravel → adalah
adalah → framework
framework → php
```

---

### 4. Generasi Teks

Ketika pengguna memasukkan kata awal, model akan:

1. Mencari pasangan kata pada model.
2. Memilih kata berikutnya secara acak.
3. Menghasilkan kalimat hingga batas tertentu.

Contoh input:

```text
laravel
```

Contoh output:

```text
laravel adalah framework php yang digunakan untuk membangun aplikasi web modern
```

---

## 🧠 Metode yang Digunakan

- **Natural Language Processing (NLP)**
- **Text Mining**
- **Tokenization**
- **Bigram Language Model**
- **Markov Chain Orde-1**
- **Random Text Generation**

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Fungsi |
|-----------|--------|
| Python | Bahasa Pemrograman |
| Streamlit | User Interface |
| JSON | Penyimpanan Model |
| NLTK | Tokenisasi Teks |
| Regular Expression | Text Preprocessing |

---

## 🚀 Instalasi

Clone repository:

```bash
git clone https://github.com/dimaswardoyo-hash/mini_llm.git
```

Masuk ke folder project:

```bash
cd mini_llm
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Training

```bash
python train.py
```

Model hasil training akan disimpan pada:

```bash
models/laravel_model.json
```

---

## 🌐 Menjalankan Aplikasi

```bash
streamlit run app.py
```

Atau langsung akses aplikasi online:

### 🔗 https://minillm-laravel.streamlit.app/

---

## 📸 Tampilan Aplikasi

> Tambahkan screenshot aplikasi di sini.

```markdown
![Preview Aplikasi](images/preview.png)
```

---

## 📊 Hasil

Sistem mampu menghasilkan teks sederhana berdasarkan corpus Laravel yang telah dipelajari.

Walaupun model belum menggunakan arsitektur Transformer seperti GPT, proyek ini berhasil menunjukkan implementasi dasar dari **Language Model berbasis statistik**.

---

## 🔍 Kelebihan

✅ Mudah dipahami untuk pembelajaran NLP.  
✅ Arsitektur sederhana dan ringan.  
✅ Memiliki antarmuka web interaktif.  
✅ Mendukung beberapa metode tokenisasi.  
✅ Cocok untuk implementasi dasar Data Mining.

---

## ⚠️ Keterbatasan

- Hanya menggunakan Bigram Model.
- Belum memahami konteks kalimat secara penuh.
- Belum menggunakan embedding maupun Transformer.
- Hasil generasi masih bersifat acak.

---

## 👨‍🎓 Informasi Akademik

**Mata Kuliah:** Proyek Data Mining

**Program Studi:** Informatika

**Universitas:** Universitas Amikom Yogyakarta

**Nama:** Dimas Aryo Wardoyo

---

## 👨‍💻 Developer

**Dimas Aryo Wardoyo**

GitHub: https://github.com/dimaswardoyo-hash

---

<div align="center">

⭐ Jika project ini bermanfaat, jangan lupa berikan star pada repository ini.

</div>
