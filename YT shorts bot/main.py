from program_assets.cleanup import cleanup
from program_assets.videoEditor import makeVideo
from program_assets.memeDownloader import downloadMemes
from program_assets.videoUploader import upload_video

downloadMemes()
makeVideo()
cleanup()
upload_video()
