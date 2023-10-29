import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
!yolo train data="DatasetV2\data.yaml" model=yolov8m.yaml epochs=30 batch=16 save=True mode='train' task='detect'
