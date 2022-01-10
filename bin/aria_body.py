import fitbit, json
# import requests.packages.urllib3
# requests.packages.urllib3.disable_warnings()

fit = fitbit.Fitbit()

# Try to read existing token pair
token = fit.ReadToken()

# Send data request to Fitbit
#body = fit.ApiCall(token, '/1/user/-/body/log/weight/date/2021-10-24/1m.json')
#body = fit.ApiCall(token, '/1/user/-/body/log/weight/date/2021-09-24/today.json')
body = fit.ApiCall(token, '/1/user/-/body/log/weight/date/today.json')
# Get response and send to STDOUT for Splunk ingestion
body = json.dumps(body)

print (body)