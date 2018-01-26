import cv2
import os


def convert_vid_to_frames(src,dst,fps):
    '''
    Converts src video to frames in the dst folder

    @param src: video file
    @param dst: destination folder to save images in
    @return: True if the function has finished executing
    '''

    if(not os.path.exists(dst)):
        os.makedirs(dst)

    ffmpeg_command = 'ffmpeg -i ' + src + ' -r ' + str(fps) + ' ' + os.path.join(dst,'frame_%06d.png')

    print ffmpeg_command

    run_stat = os.system(ffmpeg_command)

    if(not run_stat):
        return True

    else:
        return False
