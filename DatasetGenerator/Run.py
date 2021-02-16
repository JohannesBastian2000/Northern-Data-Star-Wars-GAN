from GenerateDataset import GenerateDataset
from CleanDataSet import CleanDataSet
import os

dataset_generator = GenerateDataset(every_x_frame=13, set_fix_image_size=384)
dataset_generator.run()
