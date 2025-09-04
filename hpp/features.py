from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

import pandas as pd

from hpp.config import PROCESSED_DATA_DIR

def encode_home_func_binary(df: pd.DataFrame) -> pd.DataFrame:
    df['Functional'] = df['Functional'].apply(lambda val: 1 if val in ['Maj2', 'Severe'] else 0)
    return df

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "features.csv",
    # -----------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Generating features from dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Features generation complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
