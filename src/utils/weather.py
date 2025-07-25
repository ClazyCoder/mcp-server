import dotenv
import os
import requests
from PIL import Image
import base64
from io import BytesIO

dotenv.load_dotenv(dotenv.find_dotenv())

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
IMG_DIR = os.getenv("IMG_DIR")


def url_builder(tm):
    url_list = []
    for ef in range(0, 30, 15):
        url_list.append(
            f'https://apihub.kma.go.kr/api/typ03/cgi/dfs/nph-qpf_ana_img?eva=1&tm={tm}&qpf=B&ef={ef}&map=HR&grid=2&legend=1&size=600&zoom_level=0&zoom_x=0000000&zoom_y=0000000&stn=108&x1=470&y1=575&authKey={WEATHER_API_KEY}')
    return url_list


def get_weather_img_list(tm):
    """
    Parameters:
        tm: str
            The time in the format of YYYYMMDDHHMM.

    Returns:
        img_list: list[str]
            The weather images in base64 format.
            The images are in base64 format. Each image is a 15 minute interval.
    If IMG_DIR/{tm} directory does not exist, it will be created. and the images will be downloaded.
    If IMG_DIR/{tm} directory exists, the images will be loaded from the directory.
    """
    img_list = []
    if not os.path.exists(os.path.join(IMG_DIR, f'{tm}')):
        os.makedirs(os.path.join(IMG_DIR, f'{tm}'))
        url_list = url_builder(tm)
        for enum, url in enumerate(url_list):
            response = requests.get(url)
            with open(f'{IMG_DIR}/{tm}/{enum}.png', 'wb') as f:
                f.write(response.content)
            img = Image.open(f'{IMG_DIR}/{tm}/{enum}.png')
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_list.append(base64.b64encode(
                buffered.getvalue()).decode('utf-8'))
    else:
        for enum in range(3):
            img = Image.open(f'{IMG_DIR}/{tm}/{enum}.png')
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_list.append(base64.b64encode(
                buffered.getvalue()).decode('utf-8'))
    return img_list
