import streamlit as st
import pickle
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from datasets import load_dataset
import pandas as pd
import re

# Sayfa ayarları
st.set_page_config(
    page_title="Türkçe Duygu Analizi",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 Türkçe Ürün Yorumu — Duygu Analizi")
st.write("Bir ürün yorumu yaz, model pozitif mi negatif mi olduğunu tahmin etsin!")

@st.cache_resource
def modeli_yukle():
    # Veriyi yükle ve modeli eğit
    dataset = load_dataset("turkish_product_reviews")
    df = pd.DataFrame(dataset['train'])
    
    def temizle(metin):
        metin = metin.lower()
        metin = re.sub(r'[^\w\s]', '', metin)
        metin = re.sub(r'\d+', '', metin)
        return metin.strip()
    
    df['temiz'] = df['sentence'].apply(temizle)
    df = df[df['temiz'].str.len() > 0]
    
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(
            max_features=50000,
            ngram_range=(1, 2),
            min_df=2
        )),
        ('model', LinearSVC(
            class_weight='balanced',
            max_iter=2000
        ))
    ])
    pipeline.fit(df['temiz'], df['sentiment'])
    return pipeline

with st.spinner('Model yükleniyor, lütfen bekle...'):
    model = modeli_yukle()

st.success('Model hazır!')

# Kullanıcıdan yorum al
yorum = st.text_area(
    "Yorumunuzu buraya yazın:",
    placeholder="Örnek: Ürün çok kaliteli, hızlı kargo geldi..."
)

if st.button("Analiz Et"):
    if yorum.strip() == "":
        st.warning("Lütfen bir yorum yazın!")
    else:
        tahmin = model.predict([yorum])[0]
        if tahmin == 1:
            st.success("✅ POZİTİF yorum")
        else:
            st.error("❌ NEGATİF yorum")