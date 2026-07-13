<img width="1872" height="901" alt="Screenshot 2026-07-13 162016" src="https://github.com/user-attachments/assets/8571840a-8336-49a4-a8ec-1fe4baf89d07" /># 🎬 AI Movie Recommendation System

An AI-powered movie recommendation web application built using **Python**, **Streamlit**, and **Machine Learning**. The system recommends movies similar to the one selected by the user and displays movie posters using the TMDB API.

## 🚀 Features

- Movie recommendations based on similarity
- Clean and interactive Streamlit interface
- Movie posters fetched using the TMDB API
- Fast recommendations using a precomputed similarity matrix

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Pickle
- TMDB API

## 📂 Project Structure

```
Movie-Recommendation-System/
│── app.py
│── movies.pkl
│── similarity.pkl
│── requirements.txt
│── style.css
│── .gitignore
│── README.md
```

## ▶️ Run Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Add your API key.

Create a `config.py` file (or use Streamlit Secrets if deploying):

```python
API_KEY = "YOUR_API_KEY"
```

4. Run the application:

```bash
streamlit run app.py
```
## 👩‍💻 Author

**Divya Chavhan**

GitHub: https://github.com/divyachavhan1610
TMDB API integration
Interactive Streamlit web application
Movie posters
Ratings
Release dates
Genres
Movie trailers
🛠 Technologies Used
Python
Pandas
NumPy
Scikit-learn
NLTK
Streamlit
Requests
Pickle
TMDB API
🤖 Machine Learning Concepts
Content-Based Recommendation System
NLP
Feature Engineering
CountVectorizer
Cosine Similarity
Stemming
📂 Dataset
TMDB 5000 Movie Dataset

▶️ How to Run
Clone the repository

Install requirements

pip install -r requirements.txt

Create config.py
API_KEY="YOUR_TMDB_API_KEY"

Run
streamlit run app.py

📌 Future Improvements
User Authentication
Collaborative Filtering
Hybrid Recommendation System
User Ratings
Watchlist
Movie Reviews
👩‍💻 Developed By
Divya Chavhan
