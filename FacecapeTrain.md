# 如何使用facescape数据集训练[3dheads](https://github.com/xubaixinxbx/3dheads.git)

## 1.环境安装

    create an anaconda environment by referring to [VolSDF](https://github.com/lioryariv/volsdf.git).
    使用Volsdf的[environment.yaml]https://github.com/lioryariv/volsdf/blob/main/environment.yml)
    cmd ['conda env create -f environment.yaml']



## 2.数据预处理

    Our method is also evaluated on the Facescape dataset, which is processed as in [NeuFace](https://github.com/aejion/NeuFace/tree/master).
    facescape的人脸数据需要用NeuFace里面的数据处理脚本提取可用数据，需要用到NeuFace/data_preprocess/cut_mesh.py和NeuFace/data_preprocess/render_mask.py 两个脚本文件
    cut_mesh.py

#### cut_mesh.py
