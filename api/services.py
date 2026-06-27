import time
import uuid
import logging

logger = logging.getLogger(__name__)

class IikoService:
    @staticmethod
    def create_write_off_act(request_data):
        time.sleep(0.5)
        
        fake_act_id = f"iiko-act-{uuid.uuid4().hex[:8].upper()}"
        
        logger.info(f"Successfully created write-off act in iiko. Generated Act ID: {fake_act_id}")
        
        return {
            "success": True,
            "iiko_act_id": fake_act_id,
            "message": "Write-off act synced with iiko successfully"
        }
