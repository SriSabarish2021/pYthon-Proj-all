# import yt_dlp
# from pprint import pprint

# print("This is the YouTube Video Accesor APP".center(80,'-'))
# print("")
# # url=input('Enter Youtube URL: ')
# def get_vid_info(url):
    
#     with yt_dlp.YoutubeDL() as ytl:
#         get_vid=ytl.extract_info(url,download=False)
#         print("Length (seconds):", get_vid["duration"])
#         pprint(get_vid)

    

# get_vid_info("https://youtu.be/NpmFbWO6HPU?si=KPElpG-pGNVpnNRq")


# VERY EASY 

# VERY EASY 
# VERY EASY 
# VERY EASY 
# VERY EASY 


import shutil

source="F:/vettikaran"
desit="F:/vid/mm"

def file_copy(source,desti):
    shutil.copytree(source,desti)
    print("file copied")

file_copy(source,desit)
