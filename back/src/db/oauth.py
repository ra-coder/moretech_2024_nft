from db.connect import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func


class OAuthProvider(Base):
    __tablename__ = "oauth_providers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)  # e.g., Google, Facebook
    client_id = Column(String, nullable=False)
    client_secret = Column(String, nullable=False)
    redirect_uri = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class OAuthAccount(Base):
    __tablename__ = "oauth_accounts"

    id = Column(Integer, primary_key=True, index=True)
    # user_id = Column(Integer, ForeignKey("users.id"))  # Assuming you have a `users` table
    provider_id = Column(Integer, ForeignKey("oauth_providers.id"))
    provider_user_id = Column(String, index=True)  # ID provided by OAuth provider
    access_token = Column(String, nullable=False)
    refresh_token = Column(String, nullable=True)
    expires_at = Column(DateTime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
