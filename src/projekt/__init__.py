from pathlib import Path

# import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray


def load_data() -> tuple[NDArray, NDArray]:
    """loads data from `./data/` and returns loaded NDArray

    Returns
    -------
    NDArray
        loaded array from images.npy
    NDArray
        loaded array from segmentations.npy
    """
    data_path: Path = Path() / "data"
    imgs_path: Path = data_path / "images.npy"
    segm_path: Path = data_path / "segmentations.npy"
    imgs: NDArray = np.load(imgs_path)
    segm: NDArray = np.load(segm_path)
    segm.astype(bool)
    return imgs, segm


def main() -> None:
    imgs, segm = load_data()


if __name__ == "__main__":
    main()
