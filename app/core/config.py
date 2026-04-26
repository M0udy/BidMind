from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/bidmind"
    
    # Admin
    ADMIN_TOKEN: str = "your_secret_admin_token"
    
    # Scraper
    SCRAPE_INTERVAL_HOURS: int = 4
    ALERT_INTERVAL_MINUTES: int = 30
    WHATSAPP_DRY_RUN: bool = True
    
    # API Keys
    GEMINI_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    
    # Twilio
    TWILIO_ACCOUNT_SID: Optional[str] = None
    TWILIO_AUTH_TOKEN: Optional[str] = None
    TWILIO_PHONE_NUMBER: Optional[str] = None
    TWILIO_TEST_NUMBER: Optional[str] = None
    
    # Debug
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
