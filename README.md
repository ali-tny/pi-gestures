Hand gesture control for raspi's omxplayer
==========================================
Attempting a system of gesture control for movies using the raspberry pi's
native multimedia app, omxplayer (which is, by the way, easily controllable via
ssh out-the-box).

Installation - OpenCV
---------------------
Note that this uses OpenCV (version 3.2.0). It's not installable simply via pip,
and doesn't show up in `pip freeze` hence its absence from `requirements.txt`. 
Unfortunately it can be a pain in the ass to install. I did the following:

1. Made sure I was in the project virtualenv (folder name `venv`)
2. Downloaded the [OpenCV source](http://sourceforge.net/projects/opencvlibrary)
and unzipped in the project directory.
3. Installed by compiling from source via
[instructions](http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html).
After running `cmake` you can check it's looking at the right python interpreter
(which should be in your venv folder)
4. Copied `opencv-3.2.0/release/lib/cv2.so` to `venv/lib/python2.7/site-packages/`

You can check it's installed correctly by opening the python interpreter and
trying `import cv2`.

