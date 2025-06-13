# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: settings.py
# Desc: Application configuration settings

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Booking Synchronizer"
    admin_email: str = "filip@polsakiewicz.net"
    database_url: str = "sqlite:///./booking_sync.db"

    class Config:
        env_file = ".env"

settings = Settings()
