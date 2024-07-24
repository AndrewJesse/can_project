from .models import CANMessage
from datetime import datetime

def read_can_message():
    # Simulate reading a CAN message
    message = CANMessage(
        timestamp=datetime.now(),
        message_id="123",
        data="Some CAN data"
    )
    return message
