import torch
from torch import nn
# import math
# from torch import optim
import random


class PadCrop(nn.Module):
    def __init__(self, n_samples, randomize=True):
        super().__init__()
        self.n_samples = n_samples
        self.randomize = randomize

    def __call__(self, signal):
        n, s = signal.shape
        start = 0 if (not self.randomize) else torch.randint(0, max(0, s - self.n_samples) + 1, []).item()
        end = start + self.n_samples
        output = signal.new_zeros([n, self.n_samples])
        output[:, :min(s, self.n_samples)] = signal[:, start:end]
        return output


class RandomPhaseInvert(nn.Module):
    def __init__(self, p=0.5):
        super().__init__()
        self.p = p

    def __call__(self, signal):
        return -signal if (random.random() < self.p) else signal


class Stereo(nn.Module):
    def __call__(self, signal):
        signal_shape = signal.shape
        # Check if it's mono
        if len(signal_shape) == 1:  # s -> 2, s
            signal = signal.unsqueeze(0).repeat(2, 1)
        elif len(signal_shape) == 2:
            if signal_shape[0] == 1:  # 1, s -> 2, s
                signal = signal.repeat(2, 1)
            elif signal_shape[0] > 2:  # ?, s -> 2,s
                signal = signal[:2, :]

        return signal
