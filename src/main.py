# Import everything needed to edit video clips
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *
#
# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
part1 = VideoFileClip("D:\\Projects\\Video_splitter\\res\\I am here.mp4").subclip(0,540)
part2 = VideoFileClip("D:\\Projects\\Video_splitter\\res\\I am here.mp4").subclip(541,1082)
#
# Write the result to a file (many options available !)
part1.write_videofile("D:\\Projects\\Video_splitter\\res\\Part_1.mp4")
part2.write_videofile("D:\\Projects\\Video_splitter\\res\\Part_2.mp4")