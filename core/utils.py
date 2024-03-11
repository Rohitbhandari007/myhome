from .models import Light, LightningConfigurations
from channels.db import database_sync_to_async


@database_sync_to_async
def save_light_data(text_data_json):
    """
    Save the received light data to the database.

    Args:
        text_data_json (dict): The received light data in JSON format.

    Returns:
        None
    """
    light = Light.objects.get(pk=text_data_json["light_id"])
    configuration = LightningConfigurations.objects.filter(light__id=text_data_json["light_id"]).first()
    if configuration:
        configuration.brightness = text_data_json["brightness"]
        configuration.color = text_data_json["color"]
    else:
        configuration = LightningConfigurations(
            light=light,
            brightness=text_data_json["brightness"],
            color=text_data_json["color"]
        )
    light.is_online = True if text_data_json["switch"] == "on" else False
    light.save()
    configuration.save()

    return light
