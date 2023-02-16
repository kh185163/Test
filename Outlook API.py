# The code sets up the authentication parameters, sends a request to obtain an access token using client credentials flow,
#  extracts the access token from the response JSON, sets the authorization header with the access token, 
# and sends a GET request to retrieve information about the authenticated user's profile. Finally, it prints the JSON response returned by the API.


import requests

# Set up the authentication parameters
url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
client_id = '6109f1a5-1f8e-4467-a2dc-3726cb80373b'  # Replace with your registered Azure AD application's client ID
client_secret = ''  # Replace with your registered Azure AD application's client secret
scope = 'https://graph.microsoft.com/.default'
grant_type = 'client_credentials'

# Request an access token
response = requests.post(url, data={
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': scope,
    'grant_type': grant_type
})
access_token = response.json()['access_token']  # Extract the access token from the response JSON

# Retrieve information about the authenticated user
headers = {'Authorization': f'Bearer {access_token}'}  # Set the authorization header with the access token
response = requests.get('https://graph.microsoft.com/v1.0/me', headers=headers)  # Send a GET request to retrieve the user's profile
print(response.json())  # Print the JSON response returned by the API
