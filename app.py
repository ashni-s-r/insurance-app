# fastapi

import logging
from typing import List, Optional

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from models.db_base import Base, engine, get_session
from repositories.insurance_repositories import Insurance_Repo
from serializers.insurance_serializers import (InsuranceCreate,
                                               InsuranceResponse,
                                               InsuranceUpdate)

Base.metadata.create_all(engine)

bearer_scheme = HTTPBearer()


app = FastAPI(
    title='Ash Insurance Service',
    description='Ash Insurance Service - FastAPI Application',
    version='1.0.0',
    openapi_url='/backend/openapi.json', docs_url='/backend/docs'
)
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'])


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %Z',
)
logger = logging.getLogger(__name__)
logger.info('WELCOME TO ASH INSURANCE SERVICE')


@app.get('/backend/docs', include_in_schema=True, tags=['app_default_apis'],)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url='/openapi.json',
        title='Fast API',
        oauth2_redirect_url='/docs/oauth2-redirect',
    )


@app.get('/backend/healthchecker', tags=['app_default_apis'])
def root():
    logging.info('Health Check Successfully.')
    return {'message': 'Hello World'}


@app.post('/backend/createinsurance/', response_model=InsuranceResponse, tags=['insurance_apis'])
def create_insurance_api(insurance: InsuranceCreate, db: Session = Depends(get_session)):
    return Insurance_Repo.create_insurance(db, insurance)


@app.get('/backend/getinsurance/{insurance_id}', response_model=Optional[InsuranceResponse], tags=['insurance_apis'], )
def get_insurance_api(insurance_id: int, db: Session = Depends(get_session)):
    return Insurance_Repo.get_insurance(db, insurance_id)


@app.get('/backend/getallinsurance/', response_model=List[InsuranceResponse], tags=['insurance_apis'])
def get_all_insurances_api(db: Session = Depends(get_session)):
    return Insurance_Repo.get_all_insurances(db)


@app.put('/backend/updateinsurance/{insurance_id}', response_model=Optional[InsuranceResponse], tags=['insurance_apis'])
def update_insurance_api(insurance_id: int, update_data: InsuranceUpdate, db: Session = Depends(get_session)):
    return Insurance_Repo.update_insurance(db, insurance_id, update_data)


@app.delete('/backend/deleteinsurance/{insurance_id}', tags=['insurance_apis'])
def delete_insurance_api(insurance_id: int, db: Session = Depends(get_session)):
    return {'deleted': Insurance_Repo.delete_insurance(db, insurance_id)}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080, keep_alive_timeout=150)
