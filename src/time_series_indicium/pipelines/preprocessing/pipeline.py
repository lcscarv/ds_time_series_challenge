"""This is a boilerplate pipeline 'preprocessing' generated using Kedro
0.18.4."""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocessing

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func = preprocessing,
                inputs = 'imf_dm_export_raw',
                outputs = 'imf_dm_export_pp',
                name = 'Preprocessing'
            )
        ]
    )
