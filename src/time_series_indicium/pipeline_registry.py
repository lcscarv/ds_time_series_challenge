"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from time_series_indicium.pipelines import preprocessing as pp
from time_series_indicium.pipelines import feature_engineering as fe
from time_series_indicium.pipelines import training,formating

# from kedro.framework.project import find_pipelines


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """

    return {
   "__default__":
            pp.create_pipeline()
            + fe.create_pipeline()
            + training.create_pipeline()
            + formating.create_pipeline()
        
    }
