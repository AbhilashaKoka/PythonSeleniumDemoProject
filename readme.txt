##############################################################################################################
Local Setup for Python3-Install python Locally
Below are the steps to create a Virtual Environment to isolate installation environment for development
########################################################################################################
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
Test are run through the command Line or through a shell script-By running cmd on features folder
single run
(BDDVirtualEnvPy3) PS D:\Users\akoka\IdeaProjects\PythonSeleniumDemoProject\examples\features> behave login.feature

DevTools listening on ws://127.0.0.1:62505/devtools/browser/0d81a0bb-db84-40d3-8781-6a2aa1e7278b
Feature: Checking TestBox Functionality # login.feature:1

  Scenario: Verify Textbox login with valid values                              # login.feature:4
    Given User is on Landing Page                                               # steps/loginsteps.py:9
    When User enter details username, email, current address, permanent address # steps/loginsteps.py:20
    And Click on Submit                                                         # steps/loginsteps.py:31
    Then user should able to verify the detail on output area                   # steps/loginsteps.py:36

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
4 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m14.171s
############################################################################################################
(BDDVirtualEnvPy3) PS D:\Users\akoka\IdeaProjects\PythonSeleniumDemoProject\examples\features> behave --help
usage: behave [options] [ [DIR|FILE|FILE:LINE] ]+

Run a number of feature tests with behave.

positional arguments:
  paths                 Feature directory, file or file location (FILE:LINE).

options:
  -h, --help            show this help message and exit
  -c, --no-color        Disable the use of ANSI color escapes.
  --color               Use ANSI color escapes. This is the default behaviour. This switch is used to override a configuration file setting.
  -d, --dry-run         Invokes formatters without executing the steps.
  -D NAME=VALUE, --define NAME=VALUE
                        Define user-specific data for the config.userdata dictionary. Example: -D foo=bar to store it in config.userdata["foo"].
  -e PATTERN, --exclude PATTERN
                        Don't run feature files matching regular expression PATTERN.
  -i PATTERN, --include PATTERN
                        Only run feature files matching regular expression PATTERN.
  --no-junit            Don't output JUnit-compatible reports.
  --junit               Output JUnit-compatible reports. When junit is enabled, all stdout and stderr will be redirected and dumped to the junit
                        report, regardless of the "--capture" and "--no-capture" options.
  --junit-directory PATH
                        Directory in which to store JUnit reports.
  -f FORMAT, --format FORMAT
                        Specify a formatter. If none is specified the default formatter is used. Pass "--format help" to get a list of available
                        formatters.
  --steps-catalog       Show a catalog of all available step definitions. SAME AS: --format=steps.catalog --dry-run --no-summary -q
  -k, --no-skipped      Don't print skipped steps (due to tags).
  --show-skipped        Print skipped steps. This is the default behaviour. This switch is used to override a configuration file setting.
  --no-snippets         Don't print snippets for unimplemented steps.
  --snippets            Print snippets for unimplemented steps. This is the default behaviour. This switch is used to override a configuration file
                        setting.
  -m, --no-multiline    Don't print multiline strings and tables under steps.
  --multiline           Print multiline strings and tables under steps. This is the default behaviour. This switch is used to override a
                        configuration file setting.
  -n NAME, --name NAME  Only execute the feature elements which match part of the given name. If this option is given more than once, it will match
                        against all the given names.
  --no-capture          Don't capture stdout (any stdout output will be printed immediately.)
  --capture             Capture stdout (any stdout output will be printed if there is a failure.) This is the default behaviour. This switch is used
                        to override a configuration file setting.
  --no-capture-stderr   Don't capture stderr (any stderr output will be printed immediately.)
  --capture-stderr      Capture stderr (any stderr output will be printed if there is a failure.) This is the default behaviour. This switch is used
                        to override a configuration file setting.
  --no-logcapture       Don't capture logging. Logging configuration will be left intact.
  --logcapture          Capture logging. All logging during a step will be captured and displayed in the event of a failure. This is the default
                        behaviour. This switch is used to override a configuration file setting.
  --logging-level LOGGING_LEVEL
                        Specify a level to capture logging at. The default is INFO - capturing everything.
  --logging-format LOGGING_FORMAT
                        Specify custom format to print statements. Uses the same format as used by standard logging handlers. The default is
                        "%(levelname)s:%(name)s:%(message)s".
  --logging-datefmt LOGGING_DATEFMT
                        Specify custom date/time format to print statements. Uses the same format as used by standard logging handlers.
  --logging-filter LOGGING_FILTER
                        Specify which statements to filter in/out. By default, everything is captured. If the output is too verbose, use this option
                        to filter out needless output. Example: --logging-filter=foo will capture statements issued ONLY to foo or foo.what.ever.sub
                        but not foobar or other logger. Specify multiple loggers with comma: filter=foo,bar,baz. If any logger name is prefixed with
                        a minus, eg filter=-foo, it will be excluded rather than included.
  --logging-clear-handlers
                        Clear all other logging handlers.
  --no-summary          Don't display the summary at the end of the run.
  --summary             Display the summary at the end of the run.
  -o FILE, --outfile FILE
                        Write to specified file instead of stdout.
  -q, --quiet           Alias for --no-snippets --no-source.
  -s, --no-source       Don't print the file and line of the step definition with the steps.
  --show-source         Print the file and line of the step definition with the steps. This is the default behaviour. This switch is used to
                        override a configuration file setting.
  --stage STAGE         Defines the current test stage. The test stage name is used as name prefix for the environment file and the steps directory
                        (instead of default path names).
  --stop                Stop running tests at the first failure.
  -t TAG_EXPRESSION, --tags TAG_EXPRESSION
                        Only execute features or scenarios with tags matching TAG_EXPRESSION. Pass "--tags-help" for more information.
  -T, --no-timings      Don't print the time taken for each step.
  --show-timings        Print the time taken, in seconds, of each step after the step has completed. This is the default behaviour. This switch is
                        used to override a configuration file setting.
  -v, --verbose         Show the files and features loaded.
  -w, --wip             Only run scenarios tagged with "wip". Additionally: use the "plain" formatter, do not capture stdout or logging output and
                        stop at the first failure.
  -x, --expand          Expand scenario outline tables in output.
  --lang LANG           Use keywords for a language other than English.
  --lang-list           List the languages available for --lang.
  --lang-help LANG      List the translations accepted for one language.
  --tags-help           Show help for tag expressions.
  --version             Show version.
##############################################################################################################
Unit Test
#############################################################################################################
(BDDVirtualEnvPy3) PS D:\Users\User\IdeaProjects\PythonSeleniumDemoProject\examples\DemoPythonScript> python -m unittest unit1.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
(BDDVirtualEnvPy3) PS D:\Users\User\IdeaProjects\PythonSeleniumDemoProject\examples\DemoPythonScript> python -m unittest -v unit1.py
test_isupper (unit1.TestStringMethods.test_isupper) ... ok
test_split (unit1.TestStringMethods.test_split) ... ok
test_upper (unit1.TestStringMethods.test_upper) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
(BDDVirtualEnvPy3) PS D:\Users\User\IdeaProjects\PythonSeleniumDemoProject\examples\DemoPythonScript>
######################################################################################################################################
(BDDVirtualEnvPy3) PS D:\Users\User\IdeaProjects\PythonSeleniumDemoProject\examples\DemoPythonScript> python -m unittest -h
usage: python.exe -m unittest [-h] [-v] [-q] [--locals] [--durations N] [-f] [-c] [-b] [-k TESTNAMEPATTERNS] [tests ...]

positional arguments:
  tests                a list of any number of test modules, classes and test methods.

options:
  -h, --help           show this help message and exit
  -v, --verbose        Verbose output
  -q, --quiet          Quiet output
  --locals             Show local variables in tracebacks
  --durations N        Show the N slowest test cases (N=0 for all)
  -f, --failfast       Stop on first fail or error
  -c, --catch          Catch Ctrl-C and display results so far
  -b, --buffer         Buffer stdout and stderr during tests
  -k TESTNAMEPATTERNS  Only run tests which match the given substring

Examples:
  python.exe -m unittest test_module               - run tests from test_module
  python.exe -m unittest module.TestClass          - run tests from module.TestClass
  python.exe -m unittest module.Class.test_method  - run specified test method
  python.exe -m unittest path/to/test_file.py      - run tests from test_file.py

usage: python.exe -m unittest discover [-h] [-v] [-q] [--locals] [--durations N] [-f] [-c] [-b] [-k TESTNAMEPATTERNS] [-s START] [-p PATTERN]
                                       [-t TOP]

options:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose output
  -q, --quiet           Quiet output
  --locals              Show local variables in tracebacks
  --durations N         Show the N slowest test cases (N=0 for all)
  -f, --failfast        Stop on first fail or error
  -c, --catch           Catch Ctrl-C and display results so far
  -b, --buffer          Buffer stdout and stderr during tests
  -k TESTNAMEPATTERNS   Only run tests which match the given substring
  -s START, --start-directory START
                        Directory to start discovery ('.' default)
  -p PATTERN, --pattern PATTERN
                        Pattern to match tests ('test*.py' default)
  -t TOP, --top-level-directory TOP
                        Top level directory of project (defaults to start directory)

For test discovery all test modules must be importable from the top level directory of the project.
(BDDVirtualEnvPy3) PS D:\Users\User\IdeaProjects\PythonSeleniumDemoProject\examples\DemoPythonScript>
###############################################################################################################





