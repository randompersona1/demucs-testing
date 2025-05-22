import demucs.separate

import torch

print(torch.__version__)
print(torch.cuda.is_available())


demucs.separate.main([
    "--two-stems=vocals",
    "-n", "htdemucs",
    "-o", ".",
    "song.mp3",
])
