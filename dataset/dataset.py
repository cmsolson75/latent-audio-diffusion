import torch
import torchaudio
from torchaudio import transforms as T
# import tqdm
from glob import glob
from lad.utils import PadCrop, RandomPhaseInvert, Stereo


class DrumDataset(torch.utils.data.Dataset):
    def __init__(self, paths, global_args):
        super().__init__()
        # Create the bucket for files
        self.filenames = []

        # augment data: PadCrop, RandomPhaseInvert
        # Look at PadCrop --- is this shortening or just for random
        self.augs = torch.nn.Sequential(
            PadCrop(global_args.sample_size),  # Probobly get rid of Pad crop!!!!!!
            RandomPhaseInvert(),
        )
        # Re Channel data into stereo()
        self.encoding = torch.nn.Sequential(Stereo())

        # Put file names in the bucket
        #
        file_type = '.wav'
        for path in paths:
            self.filenames += glob(f'{path}/**/*{file_type}', recursive=True)  # recursive?

        self.sr = global_args.sample_rate

    # Load audio file --- torchaudio
    def load_files(self, filename):

        audio, sr = torchaudio.load(filename)
        # Resample audio files
        if sr != self.sr:
            resample_tf = T.Resample(sr, self.sr)
            resample_tf(audio)
        return audio

    # Return length of dataset
    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, idx):
        # Audio filename
        audio_filename = self.filenames[idx]

        # Load the audio file
        audio = self.load_file(audio_filename)

        # augmentation
        audio = self.augs(audio)

        # Normalize
        audio = audio.clamp(-1, 1)

        return audio, audio_filename


paths = ''
