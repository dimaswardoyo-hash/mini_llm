import json
import random
import streamlit as st

# ==================================
# LOAD MODEL
# ==================================
with open(
    "models/laravel_model.json",
    "r",
    encoding="utf-8"
) as f:
    model = json.load(f)

# ==================================
# UI
# ==================================
st.set_page_config(
    page_title="Mini Laravel LLM",
    layout="wide"
)

st.title("🤖 Mini Laravel LLM")

st.write(
    "Mini Language Model berbasis Corpus Laravel"
)

# ==================================
# STATISTIK CORPUS
# ==================================
token_count = sum(
    len(v)
    for v in model.values()
)

word_count = len(model)

st.sidebar.header("📊 Statistik Corpus")

st.sidebar.metric(
    "Jumlah Kata Unik",
    word_count
)

st.sidebar.metric(
    "Jumlah Relasi Kata",
    token_count
)

# ==================================
# INPUT USER
# ==================================
prompt = st.text_input(
    "Masukkan kata awal",
    placeholder="contoh: laravel"
)

# ==================================
# GENERATE
# ==================================
if st.button("Generate"):

    if prompt.strip() == "":
        st.warning("Masukkan kata terlebih dahulu")

    else:

        current = prompt.lower()

        generated = [current]

        for _ in range(30):

            if current not in model:
                break

            next_word = random.choice(
                model[current]
            )

            generated.append(next_word)

            current = next_word

        result = " ".join(generated)

        st.success(result)