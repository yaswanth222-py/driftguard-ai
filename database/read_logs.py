import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./driftguard.db"

engine = create_engine(DATABASE_URL)

def fetch_prediction_logs():

    try:

        query = """
        SELECT * FROM prediction_logs
        ORDER BY id DESC
        """

        df = pd.read_sql(
            query,
            engine
        )

        return df

    except Exception:

        return pd.DataFrame(
            {
                "Message": [
                    "No prediction history available yet"
                ]
            }
        )