import logging
import json
from utils.intent_checkin_date import process_check_in_date
# from utils.intent_number_of_guests import process_number_of_nights

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(f"event: {event}")
    next_state = event.get("proposedNextState", {})
    dialog_action = next_state.get("dialogAction", {})
    slot_to_elicit = dialog_action.get("slotToElicit")

    session_state = event.get("sessionState", {})
    intent = session_state.get("intent", {})
    slots = intent.get("slots", {})

    dialog_action = session_state.get("dialogAction", {})
    current_slot = dialog_action.get("slotToElicit", None)

    if current_slot:
        current_slot_value = (
            slots.get(current_slot, {}).get("value", {}).get("interpretedValue", None)
        )
    else:
        current_slot_value = None

    if current_slot_value:
        message = f"現在のスロット '{current_slot}' の値は {current_slot_value} です。"
    else:
        message = f"現在のスロット '{current_slot}' に値が設定されていません。"
    print(message)

    if slot_to_elicit == "CheckInDate":
        check_in_date = process_check_in_date(event)
        return check_in_date
