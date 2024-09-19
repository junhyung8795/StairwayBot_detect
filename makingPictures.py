import cv2
import os
import glob

video = 'stair_videos'

# 디렉토리 경로
path_dir = '/Users/junhyeong8795/workspace/stairwaybot-Capstone/yolov5/'
folder_list = os.listdir(path_dir+video)

count = 0
# 디렉토리 안 영상들 프레임 추출
for i in folder_list:
    file_list = glob.glob('/Users/junhyeong8795/workspace/stairwaybot-Capstone/yolov5/'+video+'/'+i+'/*.mp4')
    # print(file_list)
    for j in file_list:

    #     print("@")
    #     vidcap = cv2.VideoCapture(j)
        
    #     print(j+" 영상 총 프레임 수 : %f" %vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    #     count = 1
    #     success = True

    #     while success:
    #         success, image = vidcap.read()
        
    #         # 프레임
    #         frame = int(vidcap.get(1))
    #         if(frame % 2 == 0):

    #         # 이미지 사이즈 변경
    #             image = cv2.resize(image, (960, 540))
            
    #             title = '/Users/junhyeong8795/workspace/stairwaybot-Capstone/yolov5/img/'+video+'/'+os.path.basename(j)+"_%d_frame_%d.jpg" % (count, frame)
    #             cv2.imwrite(title, image)
    #             print(title+" 저장")
            
    #             count += 1