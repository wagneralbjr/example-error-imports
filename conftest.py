import sys
import os

utils_file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "pipelines/utilspipelinefolder/etls/utils" 
)

sys.path.insert(
    0, 
    utils_file_path
)

print(sys.path)