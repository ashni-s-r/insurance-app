from typing import List, Optional

from sqlalchemy.orm import Session

from models.insurance_models import Insurance_Model
from serializers.insurance_serializers import InsuranceCreate, InsuranceUpdate


class Insurance_Repo():
    def create_insurance(db: Session, insurance_data: InsuranceCreate) -> Insurance_Model:
        insurance = Insurance_Model(**insurance_data.dict())
        db.add(insurance)
        db.commit()
        db.refresh(insurance)
        return insurance

    def get_insurance(db: Session, insurance_id: int) -> Optional[Insurance_Model]:
        return db.query(Insurance_Model).filter(Insurance_Model.id == insurance_id).first()

    def get_all_insurances(db: Session) -> List[Insurance_Model]:
        return db.query(Insurance_Model).all()

    def update_insurance(db: Session, insurance_id: int, update_data: InsuranceUpdate) -> Optional[Insurance_Model]:
        insurance = db.query(Insurance_Model).filter(
            Insurance_Model.id == insurance_id).first()
        if insurance:
            for key, value in update_data.dict(exclude_unset=True).items():
                setattr(insurance, key, value)
            db.commit()
            db.refresh(insurance)
        return insurance

    def delete_insurance(db: Session, insurance_id: int) -> bool:
        insurance = db.query(Insurance_Model).filter(
            Insurance_Model.id == insurance_id).first()
        if insurance:
            db.delete(insurance)
            db.commit()
            return True
        return False
