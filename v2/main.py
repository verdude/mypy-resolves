import json
import sys

import ffmpeg
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal


class FileMeta(BaseModel):
    pascal_case: str
    model_config = ConfigDict(
        extra="allow",
        frozen=True,
        alias_generator=to_pascal,
        populate_by_name=True,
    )


match sys.argv:
    case [_, str(m)]:
        media_file = m
    case _:
        raise ValueError("Missing file argument")

streams = ffmpeg.probe(media_file)["streams"]
meta = [
    FileMeta(
        **meta,
        PascalCase="some value",
    ).dict()
    for meta in streams
]
print(json.dumps(meta))
