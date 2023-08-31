"""This is a boilerplate pipeline 'serving' generated using Kedro 0.18.4."""

from kedro.pipeline import Pipeline, pipeline

from kedro.pipeline import node

from .nodes import long_to_wide_df, final_format


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=long_to_wide_df,
            inputs=["imf_dm_export_preds","imf_dm_export_long"],
            outputs="imf_dm_export_wide",
            name="Long_to_wide_df"
        ),
        node(
            func=final_format,
            inputs=["imf_dm_export_wide","imf_dm_export_pp"],
            outputs="imf_dm_export_final",
            name="Final_Format"
        )
    ])
