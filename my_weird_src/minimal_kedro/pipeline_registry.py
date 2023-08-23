"""Project pipelines."""
from typing import Dict

from .my_weird_pipeline import create_pipeline
from kedro.pipeline import Pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = {}
    pipelines["__default__"] = create_pipeline()
    return pipelines
