D:\Users\user>python -v
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
############################################################################################################################
D:\Users\user>python2 -v
'python2' is not recognized as an internal or external command,
operable program or batch file.
############################################################################################################################
D:\Users\user>where python
D:\Users\user\AppData\Local\Programs\Python\Python312\python.exe
D:\Users\user\AppData\Local\Microsoft\WindowsApps\python.exe
###########################################################################################################################
D:\Users\user>cd "D:\Users\user\AppData\Local\Programs\Python\Python312"
##################################################################################################################################################
D:\Users\user\AppData\Local\Programs\Python\Python312>virtualenv --python=D:\Users\user\AppData\Local\Programs\Python\Python312\python.exe BDDVirtualEnvPy3
created virtual environment CPython3.12.3.final.0-64 in 4703ms
  creator CPython3Windows(dest=D:\Users\user\AppData\Local\Programs\Python\Python312\BDDVirtualEnvPy3, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=D:\Users\user\AppData\Local\pypa\virtualenv)
    added seed packages: pip==24.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

D:\Users\user\AppData\Local\Programs\Python\Python312>cd BDDVirtualEnvPy3

D:\Users\user\AppData\Local\Programs\Python\Python312\BDDVirtualEnvPy3>dir
 Volume in drive D is Data
 Volume Serial Number is BABF-1589

 Directory of D:\Users\user\AppData\Local\Programs\Python\Python312\BDDVirtualEnvPy3

03-09-2024  11:38    <DIR>          .
03-09-2024  11:38    <DIR>          ..
03-09-2024  11:38                42 .gitignore
03-09-2024  11:38    <DIR>          Lib
03-09-2024  11:38               410 pyvenv.cfg
03-09-2024  11:38    <DIR>          Scripts
               2 File(s)            452 bytes
               4 Dir(s)  221,927,981,056 bytes free

D:\Users\user\AppData\Local\Programs\Python\Python312\BDDVirtualEnvPy3>cd Scripts

D:\Users\user\AppData\Local\Programs\Python\Python312\BDDVirtualEnvPy3\Scripts>dir
 Volume in drive D is Data
 Volume Serial Number is BABF-1589

 Directory of D:\Users\user\AppData\Local\Programs\Python\Python312\BDDVirtualEnvPy3\Scripts

03-09-2024  11:38    <DIR>          .
03-09-2024  11:38    <DIR>          ..
03-09-2024  11:38             2,287 activate
03-09-2024  11:38             1,498 activate.bat
03-09-2024  11:38             3,110 activate.fish
03-09-2024  11:38             2,794 activate.nu
03-09-2024  11:38             1,657 activate.ps1
03-09-2024  11:38             1,298 activate_this.py
03-09-2024  11:38               537 deactivate.bat
03-09-2024  11:38           108,449 pip-3.12.exe
03-09-2024  11:38           108,449 pip.exe
03-09-2024  11:38           108,449 pip3.12.exe
03-09-2024  11:38           108,449 pip3.exe
03-09-2024  11:38                24 pydoc.bat
03-09-2024  11:38           274,712 python.exe
03-09-2024  11:38           263,448 pythonw.exe
              14 File(s)        985,161 bytes
               2 Dir(s)  221,927,981,056 bytes free

D:\Users\user\AppData\Local\Programs\Python\Python312\BDDVirtualEnvPy3\Scripts>activate.bat

D:\Users\user\AppData\Local\Programs\Python\Python312\BDDVirtualEnvPy3\Scripts>()

(BDDVirtualEnvPy3) D:\Users\user\AppData\Local\Programs\Python\Python312\BDDVirtualEnvPy3\Scripts>pip install selenium
Collecting selenium
  Downloading selenium-4.24.0-py3-none-any.whl.metadata (7.1 kB)
Collecting urllib3<3,>=1.26 (from urllib3[socks]<3,>=1.26->selenium)
  Downloading urllib3-2.2.2-py3-none-any.whl.metadata (6.4 kB)
Collecting trio~=0.17 (from selenium)
  Downloading trio-0.26.2-py3-none-any.whl.metadata (8.6 kB)
Collecting trio-websocket~=0.9 (from selenium)
  Using cached trio_websocket-0.11.1-py3-none-any.whl.metadata (4.7 kB)
Collecting certifi>=2021.10.8 (from selenium)
  Downloading certifi-2024.8.30-py3-none-any.whl.metadata (2.2 kB)
Collecting typing_extensions~=4.9 (from selenium)
  Downloading typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Collecting websocket-client~=1.8 (from selenium)
  Downloading websocket_client-1.8.0-py3-none-any.whl.metadata (8.0 kB)
Collecting attrs>=23.2.0 (from trio~=0.17->selenium)
  Downloading attrs-24.2.0-py3-none-any.whl.metadata (11 kB)
Collecting sortedcontainers (from trio~=0.17->selenium)
  Using cached sortedcontainers-2.4.0-py2.py3-none-any.whl.metadata (10 kB)
Collecting idna (from trio~=0.17->selenium)
  Downloading idna-3.8-py3-none-any.whl.metadata (9.9 kB)
Collecting outcome (from trio~=0.17->selenium)
  Using cached outcome-1.3.0.post0-py2.py3-none-any.whl.metadata (2.6 kB)
Collecting sniffio>=1.3.0 (from trio~=0.17->selenium)
  Using cached sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting cffi>=1.14 (from trio~=0.17->selenium)
  Downloading cffi-1.17.0-cp312-cp312-win_amd64.whl.metadata (1.6 kB)
Collecting wsproto>=0.14 (from trio-websocket~=0.9->selenium)
  Using cached wsproto-1.2.0-py3-none-any.whl.metadata (5.6 kB)
Collecting pysocks!=1.5.7,<2.0,>=1.5.6 (from urllib3[socks]<3,>=1.26->selenium)
  Using cached PySocks-1.7.1-py3-none-any.whl.metadata (13 kB)
Collecting pycparser (from cffi>=1.14->trio~=0.17->selenium)
  Using cached pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Collecting h11<1,>=0.9.0 (from wsproto>=0.14->trio-websocket~=0.9->selenium)
  Using cached h11-0.14.0-py3-none-any.whl.metadata (8.2 kB)
Downloading selenium-4.24.0-py3-none-any.whl (9.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.6/9.6 MB 5.2 MB/s eta 0:00:00
Downloading certifi-2024.8.30-py3-none-any.whl (167 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 167.3/167.3 kB 1.7 MB/s eta 0:00:00
Downloading trio-0.26.2-py3-none-any.whl (475 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 476.0/476.0 kB 2.1 MB/s eta 0:00:00
Using cached trio_websocket-0.11.1-py3-none-any.whl (17 kB)
Downloading typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Downloading urllib3-2.2.2-py3-none-any.whl (121 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 121.4/121.4 kB 1.8 MB/s eta 0:00:00
Downloading websocket_client-1.8.0-py3-none-any.whl (58 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.8/58.8 kB 771.2 kB/s eta 0:00:00
Downloading attrs-24.2.0-py3-none-any.whl (63 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.0/63.0 kB 57.2 kB/s eta 0:00:00
Downloading cffi-1.17.0-cp312-cp312-win_amd64.whl (181 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 181.5/181.5 kB 1.6 MB/s eta 0:00:00
Using cached PySocks-1.7.1-py3-none-any.whl (16 kB)
Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Using cached wsproto-1.2.0-py3-none-any.whl (24 kB)
Downloading idna-3.8-py3-none-any.whl (66 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.9/66.9 kB 899.3 kB/s eta 0:00:00
Using cached outcome-1.3.0.post0-py2.py3-none-any.whl (10 kB)
Using cached sortedcontainers-2.4.0-py2.py3-none-any.whl (29 kB)
Using cached h11-0.14.0-py3-none-any.whl (58 kB)
Using cached pycparser-2.22-py3-none-any.whl (117 kB)
Installing collected packages: sortedcontainers, websocket-client, urllib3, typing_extensions, sniffio, pysocks, pycparser, idna, h11, certifi, attrs, wsproto, outcome, cffi, trio, trio-websocket, selenium
Successfully installed attrs-24.2.0 certifi-2024.8.30 cffi-1.17.0 h11-0.14.0 idna-3.8 outcome-1.3.0.post0 pycparser-2.22 pysocks-1.7.1 selenium-4.24.0 sniffio-1.3.1 sortedcontainers-2.4.0 trio-0.26.2 trio-websocket-0.11.1 typing_extensions-4.12.2 urllib3-2.2.2 websocket-client-1.8.0 wsproto-1.2.0

[notice] A new release of pip is available: 24.1 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip
################################################################################################################################################

Go to IDE
Select new Python Project 
Select existing environment , Existing Interpreter
Select System Interpreter  (python folder path)
Click on Create Project
##################################################################################################################################################

(BDDVirtualEnvPy3) D:\Users\user\AppData\Local\Programs\Python\Python312\BDDVirtualEnvPy3\Scripts>pip freeze
attrs==24.2.0
certifi==2024.8.30
cffi==1.17.0
h11==0.14.0
idna==3.8
outcome==1.3.0.post0
pycparser==2.22
PySocks==1.7.1
selenium==4.24.0
sniffio==1.3.1
sortedcontainers==2.4.0
trio==0.26.2
trio-websocket==0.11.1
typing_extensions==4.12.2
urllib3==2.2.2
websocket-client==1.8.0
wsproto==1.2.0
#################################################################################################################

(BDDVirtualEnvPy3) D:\Users\user\AppData\Local\Programs\Python\Python312\BDDVirtualEnvPy3\Scripts>pip install behave
Collecting behave
  Downloading behave-1.2.6-py2.py3-none-any.whl.metadata (6.4 kB)
Collecting parse>=1.8.2 (from behave)
  Downloading parse-1.20.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting parse-type>=0.4.2 (from behave)
  Downloading parse_type-0.6.3-py2.py3-none-any.whl.metadata (12 kB)
Collecting six>=1.11 (from behave)
  Downloading six-1.16.0-py2.py3-none-any.whl.metadata (1.8 kB)
Downloading behave-1.2.6-py2.py3-none-any.whl (136 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 136.8/136.8 kB 68.1 kB/s eta 0:00:00
Downloading parse-1.20.2-py2.py3-none-any.whl (20 kB)
Downloading parse_type-0.6.3-py2.py3-none-any.whl (27 kB)
Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: parse, six, parse-type, behave
Successfully installed behave-1.2.6 parse-1.20.2 parse-type-0.6.3 six-1.16.0

[notice] A new release of pip is available: 24.1 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip

(BDDVirtualEnvPy3) D:\Users\user\AppData\Local\Programs\Python\Python312\BDDVirtualEnvPy3\Scripts>pip freeze
attrs==24.2.0
behave==1.2.6
certifi==2024.8.30
cffi==1.17.0
h11==0.14.0
idna==3.8
outcome==1.3.0.post0
parse==1.20.2
parse_type==0.6.3
pycparser==2.22
PySocks==1.7.1
selenium==4.24.0
six==1.16.0
sniffio==1.3.1
sortedcontainers==2.4.0
trio==0.26.2
trio-websocket==0.11.1
typing_extensions==4.12.2
urllib3==2.2.2
websocket-client==1.8.0
wsproto==1.2.0
#############################################################################################################

BDD consist of
#Steps,Step StepDefinitions
Steps(Given, When, Then)-located in the features file
StepDefinitions-.py
Behave Handles Several Options for directory layout
Steps are required in main directory
There are multiple ways to layout the test
TestGroup-feature, Steps
#############################################################################################################
Test are run through the command Line or through a shell script
############################################################################################################



