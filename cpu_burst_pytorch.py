
#TLDR a Neural net is not what you want for tabular data, it will also be slow and hard to import into the kernel


import os
import pandas as pd
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

class CPUBurstDataset(Dataset):
    def __init__(self, csv_file):
        # Load data from the CSV file using pandas
        self.data = pd.read_csv(csv_file)

        # Convert the data to PyTorch tensors


        print(self.data.values)
        self.X = torch.tensor(self.data.drop('pid', axis=1).values, dtype=torch.float32)
        self.y = torch.tensor(self.data['pid'].values, dtype=torch.float32)

    def __len__(self):
        # Return the number of samples in the dataset
        return len(self.data)

    def __getitem__(self, idx):
        # Return a sample from the dataset at the given index
        return self.X[idx], self.y[idx]


training_data = CPUBurstDataset(open("cpu_burst_training.csv", "r"))
testing_data = CPUBurstDataset(open("cpu_burst_testing.csv", "r"))

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
testing_dataloader = DataLoader(testing_data, batch_size=64, shuffle=True)




