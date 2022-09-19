from fastapi import FastAPI

from .routes.v1 import router_v1
from .database.models import user_model, user_profile_model
from .database.smw_db import smw_db


app = FastAPI(
    title='SaveMyWallet',
    version='0.0.1',
    description='API for manage spending on credit card purchases.',
)

app.router.prefix = '/api'
app.include_router(router_v1)


# CORS
# TODO: implements CORS

# Logging
# TODO: implements logger

# DB
smw_db.generate_tables()