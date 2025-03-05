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

match sys.argv:
    case [_, str(m)]:
        media_file = m
    case _:
        raise ValueError("Missing file argument")

streams = ffmpeg.probe(media_file)["streams"]
print(json.dumps([FileMeta(**meta, something="some value").dict() for meta in streams]))
