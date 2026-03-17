# proxy-gateway/Dockerfile

# שימוש בתמונת בסיס קלה של פייתון
FROM python:3.11-slim-bookworm

# התקנת כלי מערכת הכרחיים כדי שפייתון יוכל לדבר עם PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# הגדרת תיקיית העבודה בתוך המכולה
WORKDIR /app

# העתקת קובץ התלויות (ודא שיש לך requirements.txt בתיקיית proxy-gateway)
COPY requirements.txt .

# התקנת הספריות
RUN pip install --no-cache-dir -r requirements.txt

# העתקת קבצי הקוד שלנו (main.py ו- models.py)
COPY . .

# חשיפת הפורט
EXPOSE 8000

# הפעלת השרת
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]