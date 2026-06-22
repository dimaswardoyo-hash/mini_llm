import os
import json
from collections import defaultdict

from tokenizer import get_tokenizer

# ==================================
# PILIH TOKENIZER
# ==================================
TOKENIZER_NAME = "regex"

# ==================================
# LOAD CORPUS
# ==================================
with open(
    "corpus/laravel_corpus.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

# ==================================
# TOKENIZATION
# ==================================
tokenizer = get_tokenizer(TOKENIZER_NAME)

tokens = tokenizer(text)

print(f"Jumlah token: {len(tokens)}")

# ==================================
# MEMBUAT WORD PAIR
# ==================================
model = defaultdict(list)

for i in range(len(tokens)-1):
    current_word = tokens[i]
    next_word = tokens[i+1]

    model[current_word].append(next_word)

# ==================================
# SIMPAN MODEL
# ==================================
os.makedirs("models", exist_ok=True)

with open(
    "models/laravel_model.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(model, f, indent=4)

print("Model berhasil dibuat.")