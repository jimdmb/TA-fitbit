## ![Splunk Fit Icon](/../master/static/fiticon.png?raw=true "Splunk Fit Icon")&nbsp;&nbsp;Splunk Add-on for Fitbit v1.0

**Description:** Monitor IOT data from Fitbit devices to provide necessary data to analyze trends in health and activity performance over time in the **Splunk Fit** app.

**Authors:** Ramik Chopra and Justin Boucher. Copyright (C) 2016 Ramik Chopra and Justin Boucher.

*__NOTE:__ Uses heavily modified version of magnific0's Fitbit classes'. The magnific0 project is at [this link](https://github.com/magnific0/FitBit.py)*

## Supported Source types:
+ Fit:Activity
+ Fit:BodyFat _(Forthcoming. See ToDo)_
+ Fit:FoodLogging _(Includes Water Logs)_
+ Fit:HeartRate
+ Fit:Sleep
+ Fit:User

## Supported Devices:
+ Fitbit Charge
+ Fitbit ChargeHR
+ Fitbit Surge
+ Fitbit Aria

## Script Files
- /bin/fitbit.py - Python class for handling data and token requests
- /bin/access_generator.py - Command line utility for gaining initial access to your Fitbit account data
- /bin/CherryPy-4.0.0.egg - Egg file for token verification. Prevents install of requests in your Splunk Environment
- /bin/requests-2.0.0-py2.7.egg - Egg file for requests. Prevents install of requests in your Splunk Environment
- /bin/*&lt;endpoint type&gt;*.py - Worker files for ingesting different data sources from Fitbit

## Requirements
- Python Requests - Egg file provided
- CherryPy - Currently there is an issue loading this module dynamically. Please see the Issues tab for more information and a workaround.

#### ToDo
- Add advanced config to setup
- Add more Sleep information. Currently sleep functionality is configured for OAuth version 1, and Fitbit has not provided OAuth2 version stats as of yet. Basic stats are the only available stats right now.
- Add BodyFat information. Same problem as Sleep functionality right now. Additionally no Aria has been provided to test at this point.
- Fix CherryPy module issue

## Installation Instructions

### Preparation
Before using this TA, you must create a Fitbit app at [https://dev.fitbit.com](https://dev/fitbit.com) using the _Personal_ App type. This will provide you with all the necessary OAuth2 credentials required to gain access to your data. Additionally, the *Personal* will allow you to gain access to the intraday time series information used by this TA's Activity and Heart Rate monitoring. Please see the Fitbit Application documents on the Fitbit web site for information on completing this step.

### Install the TA in Splunk
Install the TA on your Splunk indexers via any Splunk provided means. Install from file is preferred, however any installation procedure can be followed. If you are unfamiliar with Splunk app installation see the following [Splunk Answers Post](https://answers.splunk.com/answers/51894/how-to-install-a-splunk-app.html). Then restart Splunk in order to continue installation.

Next, configure the setup of the TA by navigating to _http://**mysplunkserver**:8000/en-US/manager/search/apps/local_ and select the **"Setup App"** option for the TA. This screen provides the OAuth2 setup information required to obtain data from Fitbit.

_**Advanced Config:** $SPLUNK_HOME/etc/apps/Splunk_TA_fit/default/appconfig.conf contains additional advanced setup information. These settings can be copied to the /local/appconfig.conf file for further tweaking of the TA. All advanced information in the default/appconfig.conf file have been commented. This configuration information will eventually be added to the setup file._

#### Create Access Token:
Run the __access_generator.py__ from your terminal or command line located in the _$SPLUNK_HOME/etc/apps/Splunk_TA_fit/bin_ folder. This file creates the necessary access tokens and permissions in order for the Technology Addon to consume user data. This utility requires that you have already configured during the setup steps previously performed within your Splunk environment. Run the following commands in your terminal:

    cd $SPLUNK_HOME/etc/apps/Splunk_TA_fit/bin/
    chmod +x access_generator.py
    python access_generator.py

1. The __access_generator__ will provide a browser window with a code. Copy this code to your clipboard. See screenshot:
![Access Generator Code](/../master/static/CodeRef.png?raw=true "Access Generator Code")

2. At the prompt in the __access_generator__ utility, paste the code that you copied from the previous step:
![Access Generator Prompt](/../master/static/RunAccessGen.png?raw=true "Access Generator Prompt")

3. Once the code has been submitted then you should see the screenshot below:
![Access Generator Complete](/../master/static/Complete.png?raw=true "Access Generator Complete")

When the process above has been completed, you should see a file called __user_settings.txt__ has been created in the _$SPLUNK_HOME/etc/apps/Splunk_TA_fit/bin_ directory. This file contains all the required access and refresh tokens needed to access your Fitbit account information.

### Configure local/inputs.conf
The final installation step is to configure your __inputs.conf__ file that tells Splunk which data to request from your Fitbit account. To configure this, you must first create a __local__ folder in the _$SPLUNK_HOME/etc/apps/Splunk_TA_fit/_ directory. This __local__ directory is where you will make specific changes to your Splunk_TA_fit environment.

A sample __inputs.conf__ file has been provided in the _$SPLUNK_HOME/etc/apps/Splunk_TA_fit/default/_ directory. Please note that the scripts in the default file have been disabled and you will need to turn the _disabled=true_ setting to _false_ in each stanza. Please follow the guidance in the __default/inputs.conf__ file for more information.

Now restart Splunk and you should start receiving data within a few minutes!

---

*Fitbit is a registered trademark and service mark of Fitbit, Inc. Splunk Technology Add-on for Fitbit is designed for use with the Fitbit platform. This product is not put out by Fitbit, and Fitbit does not service or warrant the functionality of this product.* ![Fitbit Icon](/../master/static/FitbitLogo.png?raw=true "Fitbit Icon")