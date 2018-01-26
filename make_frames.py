import os
from video_processor.vprocess import convert_vid_to_frames

convert_vid_to_frames(src=os.path.join('..','data_folder','videos','webcam2.mkv'),
                      dst=os.path.join('..','data_folder','frames','webcam2_frames'),fps=3)
