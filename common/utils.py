



from datetime import datetime


def get_utc_now():

    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")