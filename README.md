# NIRO-SG2-SETTING
</br>
- ubuntu 18.04 </br>
- ROS melodic </br>
- Three Velodyne-LiDARs, Two Pointgrey-Cameras parsing & syncronization </br>
- FlyCapture2 Camera Selection 2.13.3.31 </br>
- SpinView 1.27.0.48 </br>
</br>
</br>
- set workspace </br>
`$ git clone https://github.com/JUYEON048/NIRO-SG2-SETTING.git` </br>
`$ cd niro-sg2-env/src/` </br>
`$ unzip pointgrey_camera_driver.zip` </br>
`$ unzip spinnaker_camera_driver.zip` </br>
`$ velodyne.zip` </br>
`$ cd .. ` </br>
`$ catkin_make` </br>
`$ source devel/setup.bash` </br>
</br>
</br>
- launch velodyne </br>
`$ roslaunch velodyne_pointcloud one_for_all.launch` </br>
</br>
- launch camera(ethernet) </br>
before this command, setting connection using FlyCapture2 application </br>
`$ roslaunch pointgrey_camera_driver camera.launch` </br>
</br>
- launch camera(USB) </br>
befor this command, setting connection using SpinView application </br>
`$ cd niro-sg2-env` </br>
`$ catkin_make` </br>
`$ sudo sh -c "echo 1000 > /sys/module/usbcore/parameters/usbfs_memory_mb"` </br>
`$ roslaunch spinnaker_sdk_camera_driver acquisition.launch` </br>

