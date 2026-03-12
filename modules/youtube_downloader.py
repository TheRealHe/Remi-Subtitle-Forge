from yt_dlp import YoutubeDL as yd

# This function download videos from Youtube. It uses the input url to download
# and the input name to name the video file.

def download_youtube(url, name):

    # Setting options for the downloader object

    settings = {

    "format": "best[ext=mp4]",           
    "outtmpl": f"videos/{name}.%(ext)s", 
    "quiet": False,
    "skip_unavailable_fragments": False,

    "extractor_args": {
            "youtube": {
                "player_client": ["android"],
                "player_skip": ["web", "web_safari"],
            }
        } 

}
    # Exceptions handling

    try:
    
        # Creating downloader

        with yd(settings) as downloader:
        
            # Donwload the video

            downloader.download([url])

            print()
            print(f"The Video ({name}) has been downloaded successfully (press enter to continue)")
            input()

            return name

    except Exception as ae:

        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        input("Press enter to continue ")
        
        return None


    