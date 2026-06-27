import time
import uuid
import logging

logger = logging.getLogger(__name__)

class IikoService:
    @staticmethod
    def create_write_off_act(request_data):
        """
        Simulates an API request to iiko to create a write-off act.
        Sleeps for 0.5s and returns a fake act ID.
        """
        # Simulate network latency
        time.sleep(0.5)
        
        # We can simulate failure if request_data lacks essential info,
        # but for an MVP, we return a successful fake response.
        fake_act_id = f"iiko-act-{uuid.uuid4().hex[:8].upper()}"
        
        logger.info(f"Successfully created write-off act in iiko. Generated Act ID: {fake_act_id}")
        
        return {
            "success": True,
            "iiko_act_id": fake_act_id,
            "message": "Write-off act synced with iiko successfully"
        }
