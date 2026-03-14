---

---
title: Turkce Duygu Analizi
emoji: 🎯
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 6.9.0
app_file: app.py
pinned: false
license: mit
---

# 🎯 Türkçe Ürün Yorumu — Duygu Analizi

Türkçe e-ticaret yorumlarını **pozitif** veya **negatif** olarak sınıflandıran makine öğrenmesi projesi.

## 🌐 Canlı Demo
👉 [Uygulamayı Dene](https://huggingface.co/spaces/ruveydaisikk/turkce-duygu-analizi)

## 📊 Veri Seti
- **Kaynak:** HuggingFace — `turkish_product_reviews`
- **Boyut:** 235.165 Türkçe ürün yorumu
- **Etiketler:** Pozitif (1) / Negatif (0)

## 🔍 Yapılanlar
- Keşifsel veri analizi (EDA)
- Kelime bulutu ve frekans analizi
- Dengesiz veri problemi tespiti ve çözümü
- 3 farklı model karşılaştırması
- Gradio ile web arayüzü deploy edildi

## 📈 Model Sonuçları

| Model | Negatif F1 | Pozitif F1 | Accuracy |
|-------|-----------|-----------|----------|
| Logistic Regression | 0.46 | 0.98 | 0.95 |
| Logistic + Balanced | 0.44 | 0.93 | 0.87 |
| LinearSVC + Balanced | 0.53 | 0.96 | 0.92 ✅ |

## 🛠️ Kullanılan Teknolojiler
- Python, Pandas, Scikit-learn
- Matplotlib, Seaborn, WordCloud
- Gradio, HuggingFace Spaces

## 🚀 Lokal Çalıştırmak İçin
```bash
pip install -r requirements.txt
python app.py
```