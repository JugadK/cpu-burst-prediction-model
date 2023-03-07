import os
import pandas as pd
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader


class CPUBurstDataset(Dataset):
    def __init__(self, csv_file):
        # Load data from the CSV file using pandas
        self.data = pd.read_csv(csv_file)

        # Convert the data to PyTorch tensors
        self.X = torch.tensor(self.data.iloc[:, :-1].values, dtype=torch.float32)
        self.y = torch.tensor(self.data.iloc[:, -1].values, dtype=torch.float32)

    def __len__(self):
        # Return the number of samples in the dataset
        return len(self.data)

    def __getitem__(self, idx):
        # Return a sample from the dataset at the given index
        return self.X[idx], self.y[idx]


training_data = open("cpu_burst_training.csv", "w")
testing_data = open("cpu_burst_testing.csv", "w")

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
testing_dataloader = DataLoader(testing_data, batch_size=64, shuffle=True)


