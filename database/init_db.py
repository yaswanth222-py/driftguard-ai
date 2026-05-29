from database.db_config import engine
from database.models import Base

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Database setup completed!")