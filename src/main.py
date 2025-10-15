from fastmcp import FastMCP
from dotenv import load_dotenv
import os
from utils.weather import get_weather_img_list
from datetime import datetime
from typing import Any

load_dotenv()

mcp = FastMCP("YSG MCP Server")
print(f"PORT: {os.getenv('SERVER_PORT')}")


@mcp.tool
def get_current_weather_imgs() -> dict[str, Any]:
    """
    Returns the Korea weather images of the previous hour.
    The images are in mcp ImageContent format. Each image is a 15 minute interval.
    """
    now = datetime.now()
    minute = now.minute // 30 * 30
    hour = max(now.hour - 1, 0)
    date_str = now.strftime('%Y%m%d')
    weather_imgs = get_weather_img_list(date_str + f'{hour:02d}{minute:02d}')
    weather_imgs_dict = {}
    for enum, img_content in enumerate(weather_imgs):
        weather_imgs_dict[f"weather_img_{date_str}{enum*15}"] = {
            "image": img_content,
            "relative_time": f"{enum*15}분 후" if enum > 0 else "현재"
        }

    return weather_imgs_dict


@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0",
            port=int(os.getenv("SERVER_PORT")))
