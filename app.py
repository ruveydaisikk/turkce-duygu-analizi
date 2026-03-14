import gradio as gr
import pandas as pd
import re
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from datasets import load_dataset

def metni_temizle(metin):
    metin = metin.lower()
    metin = re.sub(r'[^\w\s]', '', metin)
    metin = re.sub(r'\d+', '', metin)
    return metin.strip()

def modeli_yukle():
    dataset = load_dataset("turkish_product_reviews")
    df = pd.DataFrame(dataset['train'])
    df['temiz'] = df['sentence'].apply(metni_temizle)
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

print("Model eğitiliyor...")
model = modeli_yukle()
print("Model hazır!")

def analiz_et(yorum):
    if not yorum.strip():
        return "Lütfen bir yorum yazın!"
    temiz = metni_temizle(yorum)
    tahmin = model.predict([temiz])[0]
    if tahmin == 1:
        return "✅ POZİTİF yorum"
    else:
        return "❌ NEGATİF yorum"

arayuz = gr.Interface(
    fn=analiz_et,
    inputs=gr.Textbox(
        placeholder="Ürün yorumunuzu buraya yazın...",
        label="Yorum"
    ),
    outputs=gr.Textbox(label="Sonuç"),
    title="🎯 Türkçe Ürün Yorumu — Duygu Analizi",
    description="Türkçe ürün yorumlarını pozitif veya negatif olarak sınıflandırır."
)

arayuz.launch()