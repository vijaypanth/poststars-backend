from pydantic import BaseModel

class CampaignBase(BaseModel):
    name: str
    goal: str | None = None
    platform: str | None = None

class CampaignCreate(CampaignBase):
    pass

class Campaign(CampaignBase):
    id: int

model_config = {
    "from_attributes": True
}
