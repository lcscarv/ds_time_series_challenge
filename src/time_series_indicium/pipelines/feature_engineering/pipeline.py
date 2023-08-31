"""This is a boilerplate pipeline 'feature_engineering' generated using Kedro
0.18.4."""

from kedro.pipeline import Pipeline, pipeline

from kedro.pipeline import node

from .nodes import missing_data_imputation, feature_engineering


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=missing_data_imputation,
            inputs=["imf_dm_export_pp","mice_groups","economic_groups","missing_countries", "continents_regions"],
            outputs="imf_dm_export_full",
            name="Missing_data_imputation"
        ),
        node(
            func=feature_engineering,
            inputs="imf_dm_export_full",
            outputs="imf_dm_export_long",
            name="Feature_engineering"
        )
    ]
)

