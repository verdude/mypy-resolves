import json
import sys

import ffmpeg
from pydantic import BaseModel, Field, NoneStr


class FileMeta(BaseModel):
    something: str = Field(alias="SomeThing")
    other: NoneStr

    class Config:
        frozen = True
        extra = "allow"
        allow_population_by_field_name = True


media_file = sys.argv[1]
streams = ffmpeg.probe(media_file)["streams"]
print(json.dumps([FileMeta(**meta, SomeThing="some value").dict() for meta in streams]))
