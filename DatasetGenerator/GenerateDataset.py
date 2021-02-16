from pytube import YouTube

# misc
import os
import time
from FrameExtractor import FrameExtractor
from FaceExtractor import FaceExtractor
from CleanDataSet import CleanDataSet
from StarWarsURLS import VIDEOURLS

every_x_frame = 10


class GenerateDataset:
    def __init__(
        self,
        video_urls: [str] = VIDEOURLS,
        every_x_frame: int = 10,
        set_fix_image_size: int = None,
    ):
        self.video_urls = video_urls
        self.every_x_frame = every_x_frame
        self.face_extractor = FaceExtractor()
        self.set_fix_image_size = set_fix_image_size

    def run(self):
        print("Starting dataset generation.....")
        time.sleep(1)
        print("Generating dataset from: ", ", \n".join(self.video_urls))
        total_videos = len(self.video_urls)
        for i, video_url in enumerate(self.video_urls):
            video = YouTube(video_url)
            print("Downloading video %s from: %s" % (i + 1, total_videos))
            try:
                pathe = video.streams.get_by_itag(22).download()
            except:
                print("Video download failed Going to next video")
                continue
            print("Face extraction started")
            extractor = FrameExtractor(pathe, self.face_extractor)
            extractor.get_n_images(every_x_frame=every_x_frame)
            extractor.extract_frames(every_x_frame=every_x_frame)
            os.remove(pathe)
        print("Cleaning data Set")
        time.sleep(3)
        clean = CleanDataSet()
        path = os.path.dirname(__file__) + "/faces"
        clean.clean(path)
        time.sleep(3)
        print("Normalising and resizing data set")
        clean.resize(path, fix_size=self.set_fix_image_size)
        print("Dataset generation complete!")
