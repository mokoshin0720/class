from .runner.runner import main
from .dataset.dataset import trn_df, val_df

main(trn_df, val_df)