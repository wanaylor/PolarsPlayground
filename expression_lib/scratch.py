import polars as pl
from expression_lib import Language

df = pl.DataFrame(
    {
        "convert": ["pig", "latin", "is", "silly"],
    }
)


out = df.with_columns(
    pig_latin=pl.col("convert").language.pig_latinnify(),
)
