from django.db import models
from .base_model import BaseModel
class EarthquakeQuery(BaseModel):
    query_url = models.URLField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    min_magnitude = models.FloatField()
    type = models.CharField(max_length=64)
    order_by = models.CharField(max_length=64)
    metadata = models.JSONField()
    bbox = models.JSONField()
    features = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)    
