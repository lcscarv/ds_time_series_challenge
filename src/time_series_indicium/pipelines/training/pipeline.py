"""This is a boilerplate pipeline 'training' generated using Kedro 0.18.4."""

from kedro.pipeline import Pipeline, pipeline

from kedro.pipeline import node

from .nodes import forecasting



def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=forecasting,
            inputs="imf_dm_export_long",
            outputs="imf_dm_export_preds",
            name="Forecasting"
        )])
