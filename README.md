# ReplicantAutomation
The test cases are written in Python. There are two types of automation

a) Web Automation which automates a React based client
b) Web Socket automation which automates and tests the backend


Web Automation
Step 1
The solution is developed in Pycharm using Python 3.8. It is desirable to run the automation with python 3.8 as the selected intertprter.

Step 2
The solution can run on Windows, Mac and Ubuntu. Inorder to setup the required python libraries run
a) pipreqs WebAutomation
b) pipreqs WebSocketAutomation

Step 3
The Solution is uses Selenium and Beautiful soup. The Firefox and Chrome Drivers for Mac, Ubuntu and Windows are under /ReplicantAutomation/Automation/WebAutomation/Drivers/webdrivers.

The automation can use chrome  or firefox and requires same version of the browsers to be installed on the Mac, Windows or Ubuntu

Step 4
To execute the automation please run the below command

export PYTHONPATH=.
/usr/bin/python3.8 mainWebTestRunner.py --MITM True --POST_DATA False --HEADLESS False

Web Socket Automation
Step 1
The solution is developed in Pycharm using Python 3.8. It is desirable to run the automation with python 3.8 as the selected intertprter.

Step 2
The solution can run on Windows, Mac and Ubuntu. Inorder to setup the required python libraries run
pipreqs WebSocketAutomation

Step 3
run this from command line

export PYTHONPATH=.
/usr/bin/python3.8 mainWebSocketRunner.py --MITM False --POST_DATA False --URL TEST
