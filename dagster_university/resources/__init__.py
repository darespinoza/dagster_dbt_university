from dagster_duckdb import DuckDBResource
from dagster import EnvVar
from dagster_dbt import DbtCliResource

from ..assets.constants import DBT_DIRECTORY
# the import lines go at the top of the file

## Lesson 6 and go over .env file 
database_resource = DuckDBResource(
    database=EnvVar("DUCKDB_DATABASE"),
)

# this can be defined anywhere below the imports
dbt_resource = DbtCliResource(
    project_dir=DBT_DIRECTORY,
)