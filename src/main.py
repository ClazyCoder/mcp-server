from fastmcp import FastMCP
from dotenv import load_dotenv
from utils.weather import get_weather_img_list
from datetime import datetime

load_dotenv()

mcp = FastMCP("YSG MCP Server")


@mcp.tool
def get_current_weather_imgs() -> dict[str, str]:
    """
    Returns the current weather images.
    The images are in base64 format. Each image is a 15 minute interval.
    """
    now = datetime.now()
    minute = now.minute // 30 * 30
    weather_imgs = get_weather_img_list(
        now.strftime('%Y%m%d%H') + f'{minute:02d}')
    weather_imgs_dict = {}
    for enum, img_base64 in enumerate(weather_imgs):
        weather_imgs_dict[f"weather_img_{enum}"] = img_base64

    return weather_imgs_dict


if __name__ == "__main__":
    mcp.run()
