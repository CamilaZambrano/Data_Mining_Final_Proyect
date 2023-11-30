

import torch


class Config:
    ROOT = 'ULTRALYTICS'
    DATASET = 'InBreast-YOLO'
    RUNS_DIR = 'runs_ultralytics'
    METRICS_FILE = 'metrics.csv'
    NUM_CLASSES = 1
    
    def set_local_settings():
        Config.DEVICE = 0
        Config.EPOCHS = 1
        Config.BATCH_SIZE = 4
        Config.FOLDS = [1,2]
        Config.THRESHOLDS = [0.001, 0.1]
        Config.YAML_FILE = 'data_docker.yaml'
        Config.MODEL_NAMES = [
            'yolov8n.pt',
            'yolov8s.pt'
        ]
    
        
    def set_benchmark_settings():
        gpu_available = torch.cuda.is_available()
        Config.DEVICE = 0 if gpu_available else 'cpu'
        Config.EPOCHS = 200
        Config.BATCH_SIZE = 16
        Config.FOLDS = range(1,11)
        Config.THRESHOLDS = [0.001, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        Config.YAML_FILE = 'data_docker.yaml'
        Config.MODEL_NAMES = [
            'yolov8n.pt', 
            'yolov8s.pt', 
        ]
        
