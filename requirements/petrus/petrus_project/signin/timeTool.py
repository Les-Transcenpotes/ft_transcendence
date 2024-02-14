from datetime import datetime, timedelta

def peremptiontime():
    return datetime.now() + timedelta(minutes=15)
