"""
tokenizer.py

Modul tokenizer untuk Mini LLM.

Tersedia 3 tokenizer:
1. simple_tokenizer
2. regex_tokenizer
3. nltk_tokenizer
"""

import re

# ==========================
# Simple Tokenizer
# ==========================
def simple_tokenizer(text):
    """
    Tokenizer paling sederhana.
    Memecah teks berdasarkan spasi.

    Contoh:
    Input:
        "Halo Dunia AI"

    Output:
        ['halo', 'dunia', 'ai']
    """
    return text.lower().split()


# ==========================
# Regex Tokenizer
# ==========================
def regex_tokenizer(text):
    """
    Tokenizer menggunakan Regular Expression.

    Menghapus tanda baca dan hanya mengambil kata.

    Contoh:
    Input:
        "Halo, Dunia AI!"

    Output:
        ['halo', 'dunia', 'ai']
    """
    return re.findall(r'\b\w+\b', text.lower())


# ==========================
# NLTK Tokenizer
# ==========================
def nltk_tokenizer(text):
    """
    Tokenizer menggunakan library NLTK.

    Sebelum digunakan:
        pip install nltk

    Jalankan sekali:
        import nltk
        nltk.download('punkt')
    """
    try:
        import nltk
        from nltk.tokenize import word_tokenize

        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')

        return word_tokenize(text.lower())

    except ImportError:
        raise ImportError(
            "NLTK belum terinstall. Jalankan: pip install nltk"
        )


# ==========================
# Tokenizer Factory
# ==========================
def get_tokenizer(tokenizer_name):
    """
    Mengembalikan fungsi tokenizer sesuai pilihan.

    Parameter:
        tokenizer_name (str)

    Pilihan:
        simple
        regex
        nltk
    """

    tokenizer_name = tokenizer_name.lower()

    tokenizers = {
        "simple": simple_tokenizer,
        "regex": regex_tokenizer,
        "nltk": nltk_tokenizer
    }

    if tokenizer_name not in tokenizers:
        raise ValueError(
            f"Tokenizer '{tokenizer_name}' tidak tersedia. "
            f"Gunakan: {list(tokenizers.keys())}"
        )

    return tokenizers[tokenizer_name]


# ==========================
# Testing Langsung
# ==========================
if __name__ == "__main__":

    sample_text = """
    Laravel adalah framework PHP yang populer.
    Python digunakan untuk Machine Learning!
    """

    print("=" * 50)
    print("TEXT ASLI")
    print(sample_text)

    print("\nSIMPLE TOKENIZER")
    print(simple_tokenizer(sample_text))

    print("\nREGEX TOKENIZER")
    print(regex_tokenizer(sample_text))

    try:
        print("\nNLTK TOKENIZER")
        print(nltk_tokenizer(sample_text))
    except Exception as e:
        print("Error:", e)