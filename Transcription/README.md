# 🎙 AI-Powered Transcription, Diarization & Chat Note Bot 🤖📄

## **📌 Overview**  
This project is an **AI-driven transcription system** that performs **speech-to-text conversion, speaker diarization, and AI-generated structured note-taking**. Built for **meetings, podcasts, customer calls, and medical notes**, this bot ensures **highly accurate transcription** while labeling speakers and summarizing key discussions.  

## **✨ Features**  
✅ **Transcription** – Converts speech to text using **OpenAI’s Whisper**.  
✅ **Speaker Diarization** – Identifies and labels speakers in multi-speaker audio using **PyAnnote**.  
✅ **AI-Powered Summarization** – Structures conversation notes using **Gemini AI** (e.g., SOAP format for medical use).  
✅ **Cloud-Ready** – Supports **Azure, AWS, and GCP for scalable deployment**.  
✅ **Optimized AI Inference** – Uses **Torch & Torchaudio** for performance improvements.  
✅ **REST API Integration** – Seamlessly integrates with web and enterprise applications.  

---

## **🚀 Use Cases**  
🔹 **Meetings & Interviews** – Get speaker-labeled transcripts & key takeaways.  
🔹 **Medical Documentation** – Convert **doctor-patient conversations into SOAP notes**.  
🔹 **Podcasts & Lectures** – Generate speaker-differentiated transcripts.  
🔹 **Customer Support & Sales Calls** – Summarize interactions into actionable insights.  

---

## **🛠 Tech Stack**  
🔹 **FastAPI** – Backend API for seamless integration.  
🔹 **Whisper** – State-of-the-art **ASR (Automatic Speech Recognition)**.  
🔹 **PyAnnote** – Speaker **diarization & voice segmentation**.  
🔹 **Gemini AI** – Context-aware **summarization & chat structuring**.  
🔹 **Torch & Torchaudio** – **Deep learning** for high accuracy.  
🔹 **Docker** – **Containerized deployment** for scalability.  
🔹 **Cloud Storage** – Supports **Azure, AWS, and GCP**.  

---

## **📂 Installation & Setup**  

### **🔹 Clone the Repository**  
```bash
 git clone <your-repo-url>
 cd transcription-diarization-bot
```

### **🔹 Create a Virtual Environment**  
```bash
 python -m venv venv
```

### **🔹 Activate the Virtual Environment**  
**Mac/Linux:**  
```bash
 source venv/bin/activate
```
**Windows:**  
```powershell
 venv\Scripts\Activate.ps1
```

### **🔹 Install Dependencies**  
```bash
 pip install -r requirements.txt
```

### **🔹 Set Up API Keys**  
Export API keys for **Whisper, PyAnnote, and Gemini AI**:  
```bash
 export GEMINI_API_KEY="your-api-key"
 export PYANNOTE_API_KEY="your-api-key"
```

---

## **🚀 Running the Application**  

### **🔹 Start the FastAPI Server**  
```bash
 uvicorn app:main --host 0.0.0.0 --port 8000
```

### **🔹 Example API Request**  
Send an audio file for processing:  
```bash
 curl -X POST "http://localhost:8000/transcribe" -F "file=@sample_audio.wav"
```

---

## **🚧 Challenges & Solutions**  

### **🔥 Challenge 1: Large Model Optimization**  
- **Problem:** Whisper & PyAnnote models are **computationally expensive**.  
- **Solution:** Used **model quantization & GPU acceleration** for faster inference.  

### **🎯 Challenge 2: Speaker Misalignment in Diarization**  
- **Problem:** PyAnnote sometimes **mislabels speakers in noisy environments**.  
- **Solution:** **Fine-tuned diarization parameters** and used additional **post-processing techniques**.  

### **📊 Challenge 3: Summarization Accuracy**  
- **Problem:** Gemini AI sometimes **missed key details** in summarization.  
- **Solution:** Implemented **better prompt engineering & metadata-based filtering**.  

---

## **📢 What's Next?**  
🚀 **This is just the beginning!** I am continuously refining and expanding my work, pushing the boundaries of **AI-driven automation, knowledge retrieval, and real-world AI applications**. Whether it’s improving this project or exploring **new frontiers in Generative AI, NLP, and intelligent systems**, there’s much more to come! Stay tuned for even more powerful innovations.  

---

## **📚 Documentation**  
| Component | Purpose |
|-----------|---------|
| `app.py` | Main FastAPI backend |
| `transcriber.py` | Handles Whisper ASR transcription |
| `diarizer.py` | Implements PyAnnote speaker segmentation |
| `summarizer.py` | Uses Gemini AI for structuring notes |

---

## **📑 Acknowledgments**  
This project was inspired by **real-world challenges in transcription, diarization, and AI-driven documentation**. Thanks to **OpenAI, PyAnnote, and Google AI** for their contributions to the open-source community!  

---

## **📩 Contact**  
🔗 **Shaik Abdulla**  
📧 **aadilshaik.dtov@gmail.com**  
🔗 [LinkedIn](https://www.linkedin.com/in/aadil-shaik-dtov/)  
🔗 [GitHub](https://github.com/Aadil-Shaik)  

---

🎯 **If you find this project useful, give it a ⭐ on GitHub! Contributions & feedback are always welcome!** 🚀

