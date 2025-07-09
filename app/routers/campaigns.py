from http.client import HTTPException
from fastapi import APIRouter, Depends # type: ignore
from sqlalchemy.orm import Session # type: ignore
from app import models, schemas
from app.database import get_db
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/campaigns",
    tags=["Campaigns"]
)

@router.post("/", response_model=schemas.Campaign)
def create_campaign(campaign: schemas.CampaignCreate, db: Session = Depends(get_db)):
    db_campaign = models.Campaign(**campaign.dict())
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign

@router.get("/", response_model=list[schemas.Campaign])
def read_campaigns(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    campaigns = db.query(models.Campaign).offset(skip).limit(limit).all()
    return campaigns

@router.get("/campaigns/protected")
def read_protected_campaigns(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello user {current_user}, these are your protected campaigns."}

# Get all campaigns
@router.get("/", response_model=list[schemas.Campaign])
def get_campaigns(db: Session = Depends(get_db)):
    return db.query(models.Campaign).all()

@router.get("/{campaign_id}", response_model=schemas.Campaign)
def get_campaign(campaign_id: int, db: Session = Depends(get_db)):
    campaign = db.query(models.Campaign).filter(models.Campaign.id == campaign_id).first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign

# Update campaign
@router.put("/{campaign_id}", response_model=schemas.Campaign)
def update_campaign(campaign_id: int, campaign: schemas.CampaignCreate, db: Session = Depends(get_db)):
    db_campaign = db.query(models.Campaign).filter(models.Campaign.id == campaign_id).first()
    if not db_campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    db_campaign.name = campaign.name
    db_campaign.goal = campaign.goal
    db_campaign.platform = campaign.platform
    db.commit()
    db.refresh(db_campaign)
    return db_campaign

# Delete campaign
@router.delete("/{campaign_id}")
def delete_campaign(campaign_id: int, db: Session = Depends(get_db)):
    db_campaign = db.query(models.Campaign).filter(models.Campaign.id == campaign_id).first()
    if not db_campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    db.delete(db_campaign)
    db.commit()
    return {"message": "Campaign deleted successfully"}

