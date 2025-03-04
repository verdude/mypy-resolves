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


media_file = sys.argv[1]
streams = ffmpeg.probe(media_file)["streams"]
meta = [
    FileMeta(
        **meta,
        PascalCase="some value",
        pascal_case="snake value",
    ).dict()
    for meta in streams
]
print(json.dumps(meta))
