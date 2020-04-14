import os

CONSTANTS = {
    "PORT": os.environ.get("PORT", 3001),
    "DB_URL": "mongodb://localhost:27017/",
    "DB_NAME": "graduation-project"
}