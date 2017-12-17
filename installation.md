# Tricky to Install Tensorflow at times
* Install Cuda First and then Cudnn
  1. Register in Nvidia
  2. Download latest Cuda Toolkit from here [link text](link).
  : 1513127298:0;pip install keras
: 1513127356:0;python
: 1513127373:0;clear
: 1513127380:0;pip install tensorflow
: 1513127395:0;pip install tensorflow-gpu
: 1513127558:0;clear
: 1513127562:0;python
: 1513127607:0;deactivate
: 1513127614:0;python
: 1513128036:0;. venv/bin/activate
: 1513128039:0;clear
: 1513128044:0;sudo python
: 1513128378:0;sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
: 1513128385:0;python
: 1513128520:0;~/.bashrc
: 1513128527:0;sudo ~/.bashrc
: 1513128536:0;sudo cat ~/.bashrc
: 1513128661:0;python
: 1513162340:0;python
: 1513162805:0;sudo cp /usr/local/cuda ~/Desktop/iitd
: 1513163329:0;clear
: 1513163345:0;. venv/bin/activate
: 1513163351:0;cd ...
: 1513163361:0;cd iitd
: 1513163366:0;. venv/bin/activate
: 1513163375:0;python
: 1513164000:0;sudo apt-get install libcupti-dev
: 1513164155:0;nvidia-smi
: 1513164320:0;nvcc --version
: 1513164347:0;cd /usr/local/cuda
: 1513164353:0;nvcc --version
: 1513164355:0;ls
: 1513164359:0;cd bin
: 1513164361:0;nvcc --version
: 1513164412:0;ls
: 1513164417:0;nvcc
: 1513164436:0;run nvcc
: 1513164478:0;cuda
: 1513164484:0;nvcc
: 1513164495:0;. nvcc
: 1513164891:0;sys --version
: 1513164894:0;python
: 1513165234:0;nvidia-smi
: 1513165657:0;cd ..
: 1513165677:0;cd ls
: 1513165681:0;ls
: 1513165689:0;cd prakhar
: 1513165690:0;ls
: 1513165702:0;cd Downloads
: 1513165704:0;clear
: 1513165705:0;ls
: 1513165730:0;sudo dpkg -i cuda-repo-ubuntu1604-9-1-local_9.1.85-1_amd64.deb
: 1513165802:0;sudo apt-key add /var/cuda-repo-9-1-local/7fa2af80.pub
: 1513165808:0;sudo dpkg -i cuda-repo-ubuntu1604-9-1-local_9.1.85-1_amd64.deb
: 1513165896:0;sudo apt-get update
: 1513165962:0;sudo apt-get install cuda-libraries-9-1
: 1513166147:0;sudo apt-get install cuda
: 1513166502:0;sudo apt-get install cuda --fix-missing
: 1513167066:0;nvidia-smi
: 1513167145:0;nvcc --version
: 1513167668:0;sudo reboot
: 1513167860:0;nvidia-smi
: 1513168464:0;cd Downloads/
: 1513168466:0;ls
: 1513168522:0;tar -xzvf libcudnn7-dev_7.0.5.15-1+cuda9.1_amd64.deb
: 1513168798:0;tar -xzvf cudnn-9.1-linux-x64-v7.tgz
: 1513168988:0;sudo cp cuda/include/cudnn.h /usr/local/cuda-9.1/include
: 1513169051:0;sudo cp cuda/lib64/libcudnn* /usr/local/cuda-9.1/lib64
: 1513169095:0;sudo chmod a+r /usr/local/cuda-9.1/include/cudnn.h
: 1513169129:0;cd /usr/src/cudnn_samples_v7
: 1513169367:0;sudo dpkg -i libcudnn7-doc_7.0.3.11-1+cuda9.0_amd64.deb
: 1513169388:0;sudo dpkg -i libcudnn7-doc_7.0.5.15-1+cuda9.1_amd64.deb
: 1513169896:0;sudo dpkg -i libcudnn7-dev_7.0.5.15-1+cuda9.1_amd64.deb
: 1513170059:0;sudo dpkg -i libcudnn7_7.0.5.15-1+cuda9.1_amd64.deb
: 1513170097:0;sudo dpkg -i libcudnn7-dev_7.0.5.15-1+cuda9.1_amd64.deb
: 1513170120:0;sudo dpkg -i libcudnn7-doc_7.0.5.15-1+cuda9.1_amd64.deb
: 1513170193:0;cp -r /usr/src/cudnn_samples_v7/ $HOME
: 1513170202:0;cd  $HOME/cudnn_samples_v7/mnistCUDNN
: 1513170210:0;make clean && make
: 1513170229:0;./mnistCUDNN
: 1513170315:0;python
: 1513170418:0;cd
: 1513170431:0;~./bashrc
: 1513170444:0;~/.bashrc
: 1513170455:0;sudo cat ~/.bashrc
: 1513170584:0;sudo vim ~/.bashrc
: 1513170653:0;sudo source ~/.bashrc
: 1513170672:0;source ~/.bashrc
: 1513170684:0;zsh
: 1513170783:0;python
: 1513170955:0;cd Desktop/iitd
: 1513170968:0;. venv/bin/activate
: 1513171025:0;python
: 1513171249:0;pip install tensorflow-gpu=0.11.0
: 1513171258:0;pip install tensorflow-gpu==0.11.0
: 1513171467:0;cd Downloads
: 1513171536:0;sudo dpkg -i libcudnn6_6.0.21-1+cuda8.0_amd64.deb
: 1513171581:0;sudo dpkg -i libcudnn6-dev_6.0.21-1+cuda8.0_amd64.deb
: 1513171614:0;sudo dpkg -i libcudnn6-doc_6.0.21-1+cuda8.0_amd64.deb
: 1513171637:0;cp -r /usr/src/cudnn_samples_v6/ $HOME
: 1513171649:0;cd  $HOME/cudnn_samples_v7/mnistCUDNN
: 1513171656:0;cd  $HOME/cudnn_samples_v6/mnistCUDNN
: 1513171674:0;make clean && make
: 1513171686:0;./mnistCUDNN
: 1513171711:0;cd ~
: 1513171717:0;clear
: 1513171989:0;python
: 1513172449:0;pip uninstall scrapy
: 1513172470:0;pip freeze
: 1513172510:0;pip uninstall selenium
: 1513172545:0;pip freeze
: 1513172900:0;vi .gitignore
: 1513172940:0;ga .
: 1513172957:0;gc -m"dataset done"
: 1513172987:0;gp
: 1513185379:0;cat ~/.zsh_history
