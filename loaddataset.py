import sys
!{sys.executable} -m pip install datasets

from datasets import load_dataset

ds = load_dataset(
    "geraldmc/plantvillage-full",
    revision="v0.1.0"
)

ds.save_to_disk("plantvillage_dataset")
