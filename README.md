# **Ash Insurance Service**

## **Overview**
Ash Insurance Service is a FastAPI-based application that provides CRUD operations for managing insurance data.

## **Features**
- CRUD operations for insurance records.
- FastAPI framework.
- SQLAlchemy ORM for database management.
- Pydantic for request validation.
- Pre-commit hooks for code quality.

## **Installation**
### **Prerequisites**
- Python 3.8+
- pip

### **Setup**
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd ash_insurance_service
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the database settings in `utils/config.py`.

## **Running the Application**
```bash
python -m models.db_base
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

Access API documentation:
- **Swagger UI**: [http://localhost:8080/backend/docs](http://localhost:8080/backend/docs)
- **OpenAPI JSON**: [http://localhost:8080/backend/openapi.json](http://localhost:8080/backend/openapi.json)

## **API Endpoints**
| **Method** | **Endpoint** | **Description** |
|-----------|------------|----------------|
| **POST**   | `/backend/createinsurance/` | Create a new insurance record |
| **GET**    | `/backend/getinsurance/{insurance_id}` | Get an insurance record by ID |
| **GET**    | `/backend/getallinsurance/` | Get all insurance records |
| **PUT**    | `/backend/updateinsurance/{insurance_id}` | Update an insurance record |
| **DELETE** | `/backend/deleteinsurance/{insurance_id}` | Delete an insurance record |
| **GET**    | `/backend/healthchecker` | Health check API |

## **Pre-commit Hooks**
Install pre-commit hooks:
```bash
pre-commit install
pre-commit run --all-files
```

