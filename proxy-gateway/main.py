# קובץ: proxy-gateway/main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

# ייבוא הרכיבים שיצרנו בקובץ המודלים שלנו
from models import SessionLocal, create_tables, Metric

# יצירת מופע האפליקציה של ה-Gateway
app = FastAPI(title="Proxy Gateway")

# =============================================================================
# Pydantic Model - אימות נתונים
# =============================================================================
# מחלקה זו מגדירה לאיזה מבנה נתונים השרת שלנו מצפה.
# אם מישהו ישלח לנו בקשה בלי 'value' או עם טקסט במקום מספר, 
# FastAPI תחסום את הבקשה אוטומטית ותחזיר לו שגיאה, עוד לפני שזה מגיע למסד הנתונים.
class MetricInput(BaseModel):
    server_type: str
    metric_name: str
    value: float

# =============================================================================
# ניהול חיבורים למסד הנתונים
# =============================================================================
# פונקציה זו פותחת "חלון" (Session) למסד הנתונים עבור כל רגע שצריך, וסוגרת אותו בסוף.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# בעת הפעלת השרת, אנו מוודאים שהטבלה שלנו (metrics) נוצרת במסד הנתונים
@app.on_event("startup")
def startup_event():
    create_tables()

# =============================================================================
# נתיבים (Routes)
# =============================================================================

# נתיב בדיקת בריאות פשוט
@app.get("/health")
def health_check():
    return {"status": "Proxy Gateway is healthy and running"}

# הנתיב המרכזי: מקבל נתונים חדשים ושומר אותם במסד הנתונים
@app.post("/api/metrics")
def save_metric(metric: MetricInput, db: Session = Depends(get_db)):
    # 1. יצירת אובייקט חדש מהמחלקה של מסד הנתונים שלנו
    new_metric = Metric(
        server_type=metric.server_type,
        metric_name=metric.metric_name,
        value=metric.value
    )
    
    # 2. הוספת האובייקט לחלון העבודה (עדיין לא נשמר פיזית)
    db.add(new_metric)
    
    # 3. ביצוע השמירה הפיזית למסד הנתונים
    db.commit()
    
    return {"status": "success", "message": "הנתון נשמר בהצלחה במסד הנתונים!"}