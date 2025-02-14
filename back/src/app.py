import sentry_sdk
from fastapi import FastAPI

from api.github.login import github_login_router
from api.user import user_router
from api.user.nfts import user_nfts_router
from api.vk.login import vk_login_router
from api.web3 import web3_router
from config import settings

sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=0.1,
)

# Create FastAPI instance
app = FastAPI(
    title="Iktomi API",
    description="This is a simple FastAPI application.",
    version="0.1.1",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.include_router(vk_login_router)
app.include_router(github_login_router)
app.include_router(user_router)
app.include_router(user_nfts_router)
app.include_router(web3_router)


# Root endpoint
@app.get("/api/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}
