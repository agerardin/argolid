from argolid import PyramidGenerartor
"""Package entrypoint for the precompute_slide package."""

# Base packages
import logging
from os import environ
from pathlib import Path
from typing import Any, Optional
import typer
from argolid  import PyramidGenerartor
import json


logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)

logger = logging.getLogger(__name__)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="Graph generator.")


@app.command()
def main(  # noqa: PLR0913
    inp_dir: Path = typer.Option(
        ...,
        "--inpDir",
        "-i",
        help="inpDir.",
        case_sensitive=False,
        resolve_path=True,
        exists=True,
        file_okay= True
    ),
    out_dir: Path = typer.Option(
        ...,
        "--outDir",
        "-o",
        help="outDir.",
        case_sensitive=False,
        exists=True,
        writable=True,
        file_okay=False,
        resolve_path=True,
    ),
    image_name: str = typer.Option(
        "pyramid",
        "--name",
        "-n",
        help="image name.",
    ),
    filepattern: str = typer.Option(
        "x{x:d+}_y{y:d+}_c{c:d}.ome.tiff",
        "--filepattern",
        "-f",
        help="Filepattern for laying out graphs in final pyramid.",
        case_sensitive=False,
        exists=True,
        readable=True,
        file_okay=False,
        resolve_path=True,
    ),
    min_dim: int = typer.Option(
        ...,
        "--minDim",
        "-d",
        help="min_dim?",
    ),
    vis_type: str = typer.Option(
        ...,
        "--visType",
        "-v",
        help="vis_type?"
    ),
    ds: str = typer.Option(
        ...,
        "--ds",
        "-d",
        help="ds_dict?",
    )
) -> None:
    """Command line."""

    logger.info(f"inp dir: {inp_dir}")
    logger.info(f"out dir: {out_dir}")
    logger.info(f"filePattern: {filepattern}")
    logger.info(f"image name: {image_name}")
    logger.info(f"min dim: {min_dim}")
    logger.info(f"vis type: {vis_type}")
    logger.info(f"ds dict: {ds}")


    ds_dict = json.loads(ds)
    logger.warning(f"parsed dict : {ds_dict}")
    for key in list(ds_dict):
        ds_dict[int(key)] = ds_dict.pop(key)
    logger.warning(f"turned string to int {ds_dict}")

    image_name = "pyramid"
    min_dim = 1024
    pyr_gen = PyramidGenerartor()
    pyr_gen.generate_from_image_collection(
        str(inp_dir),
        filepattern,
        image_name,
        str(out_dir),
        min_dim,
        vis_type,
        ds_dict
    )

    


if __name__ == "__main__":
    app()
