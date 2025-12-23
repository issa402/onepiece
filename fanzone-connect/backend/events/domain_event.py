import uuid from uuid4, UUID
from datetime import datetime, timezone   
from typing import Any, Dict   
import json      

class DomainEvent:
    def__init__(self, event_type:str, entity_id:UUID, data:Dict[str, Any]):   
        self.event_id: UUID = uuid4()    
        self.event_type:str = event_type           
        self.entity_id:UUID = entity_id  
        self.data: Dict[str, Any] = data  
        self.timestamp: datetime = datetime.now(timezone.utc)

    def to_dict(self) -> Dict[str,Any]:
        return{ 
            "event_id" : str(self.event_id),  
            "event_type:": str(self.event_type),
            "entity_id": str(self.entity_id),
            "data": self.data,
            "timestamp": self.timestamp.isoformat()
        }
    def to_json(self) ->str:  
        return json.dumps(self.to_dict())
