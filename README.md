# 📚 Book-Alchemy

Book-Alchemy is a Flask-based web application designed to manage a personal library. It allows you to add, search, and manage books and authors within a clean, user-friendly interface.

---

## 🚀 Features

* **Book Management:** Add titles including genre and publication year.
* **Author Management:** Capture and store author information.
* **Search Functionality:** Quickly find books by title or author.
* **Responsive UI:** Optimized layout for different screen sizes.

---

## 🛠️ Installation & Setup

To run the project locally, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/84edu/Book-Alchemy.git
    cd Book-Alchemy
    ```

2.  **Install Dependencies:**
    Make sure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Variables:**
    Create a `.env` file in the root directory and add a secret key:
    ```env
    APP_KEY=your_secret_key_here
    ```

4.  **Run the Application:**
    ```bash
    python3 app.py
    ```
    The app will be available at `http://127.0.0.1:5000`.

---

## 🗃️ Database
The project uses **SQLite** with **SQLAlchemy** as the ORM. The database file is automatically generated in the `data/` directory upon the first run.

## 📝 License
This project was created for educational purposes.