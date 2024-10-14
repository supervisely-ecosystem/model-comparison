import os

from dotenv import load_dotenv

import supervisely as sly

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))


api = sly.Api.from_env()

STORAGE_DIR = sly.app.get_data_dir()

team_id = sly.env.team_id()
task_id = sly.env.task_id(raise_not_found=False)

selected_classes = None