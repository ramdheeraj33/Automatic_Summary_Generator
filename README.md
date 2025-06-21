# Automatic Summary Generator using BiLSTM (Hybrid Abstractive + Extractive NLP)

A web-based application that takes YouTube video links or text-based files and automatically generates concise summaries using a hybrid deep learning model. Built using a combination of extractive (LSA) and abstractive (BiLSTM-based sequence-to-sequence) summarization techniques.

---

## 🚀 Features

- Accepts YouTube URLs, PDFs, and plain text input  
- Converts audio to text using `youtube-transcript-api` and Vosk (speech-to-text)  
- Uses **LSA (Latent Semantic Analysis)** for extractive summarization  
- Uses **BiLSTM** sequence-to-sequence model for abstractive summarization  
- Clean web interface built with Flask  
- Real-time summary generation and output display  

---

## 🖥 Tech Stack

**Frontend:** HTML, CSS (via Jinja templates)  
**Backend:** Python, Flask  
**ML/NLP:** BiLSTM, Sumy (LSA), TensorFlow/Keras  
**Audio/Text Processing:** youtube-transcript-api, moviepy, pydub, vosk, textract  

---

## 📂 Project Structure

```
AutoSummary-BiLSTM/
├── app/
│   ├── server.py
│   ├── Generate_Summary.py
│   ├── URL_TextTranscription.py
│   └── templates/
│       └── home.html
├── screenshots/
│   ├── input_page.png
│   ├── output_summary.png
├── requirements.txt
├── README.md
```

---

## 📸 Screenshots

> 📥 Input Page  
![Input](screenshots/input_page.png)

> 📤 Output Summary  
![Output](screenshots/output_summary.png)

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/ramdheeraj33/Automatic_Summary_Generator.git
cd AutoSummary-BiLSTM
```

### 2. Create a Virtual Environment
```bash
conda create -n autosummary python=3.11
conda activate autosummary
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Server
```bash
cd app
python server.py
```

### 5. Access the App
Open your browser and go to:  
👉 `http://127.0.0.1:5000`

---

## 📄 Manual Requirements (if needed)

If you’re installing without `requirements.txt`, run:
```bash
pip install flask youtube-transcript-api moviepy librosa pydub vosk nltk PyPDF2 textract sumy transformers
```

And then:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## 🧠 Summary Methodology

- **Extractive summarization**: LSA via `sumy` selects most relevant sentences  
- **Abstractive summarization**: BiLSTM-based encoder-decoder generates novel sentences  
- **Hybrid output**: Combines both approaches for a balanced summary  

---

## 👨‍💻 Contributors

- **Ram Dheeraj Kamarajugadda**

---

## 💡 Future Enhancements

- Multilingual support  
- Host on Heroku/Vercel  
- Mobile-friendly interface  
- More transformer model options (e.g., Mistral, T5)
