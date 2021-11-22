
"""fine-tuningしていないDialoGPTを試す"""

from transformers import (
    MODEL_WITH_LM_HEAD_MAPPING,
    WEIGHTS_NAME,
    AdamW,
    AutoConfig,
    AutoModelWithLMHead,
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizer,
    get_linear_schedule_with_warmup,
)
from pathlib import Path
from tqdm.notebook import tqdm, trange
from torch.utils.data.distributed import DistributedSampler
from torch.utils.data import DataLoader, Dataset, RandomSampler, SequentialSampler
from torch.nn.utils.rnn import pad_sequence
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple
import shutil
import re
import random
import pickle
import os
import logging
import glob
from transformers import AutoModelWithLMHead, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelWithLMHead.from_pretrained("microsoft/DialoGPT-small")

args = Args()

main(trn_df, val_df)
