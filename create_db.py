from config.database import Base, engine
from models import purchase

print ("Creating database .....")
Base.metadata.create_all(engine)