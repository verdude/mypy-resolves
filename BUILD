python_requirement(
    name="ffmpeg_target",
    modules=["ffmpeg"],
    requirements=["typed-ffmpeg"],
    resolve=parametrize("python-default","v2"),
)

python_requirement(
    name="pydantic-v1",
    modules=["pydantic"],
    requirements=["pydantic>=2.0.0"],
    resolve="v2",
)

python_requirement(
    name="pydantic-v2",
    modules=["pydantic"],
    requirements=["pydantic<2.0.0"],
    resolve="python-default",
)

python_requirement(
    name="pydantic-mypy",
    modules=["pydantic"],
    requirements=["pydantic>=2.0.0"],
    resolve="mypy",
)

python_requirement(
    name="mypy",
    requirements=["mypy"],
    resolve="mypy",
)
