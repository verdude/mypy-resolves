import sys
import ffmpeg
from pydantic import BaseModel

class FileMeta(BaseModel):
    ...

media_file = sys.argv[1]
print(FileMeta(**ffmpeg.probe(media_file)["streams"]))
