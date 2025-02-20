# fastapi

import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.security import HTTPBearer

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


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080, keep_alive_timeout=150)
