import logging
import os

from pydantic import BaseSettings
from functools import lru_cache

log = logging.getLogger('uvicorn')


class Settings(BaseSettings):
    environment:str = os.getenv("ENVIRONMENT", "dev")
    testing:bool = os.getenv("TESTING", 0)
    

@lru_cache() 
def get_settings()-> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()


# note that all paths are relative to project_root/backend directory
EXAMPLE_PATH = "./app/models/"

# other configurations
STYLES = {
    "candy": "candy",
    "composition 6": "composition_vii",
    "feathers": "feathers",
    "la_muse": "la_muse",
    "mosaic": "mosaic",
    "starry night": "starry_night",
    "the scream": "the_scream",
    "the wave": "the_wave",
    "udnie": "udnie",
}