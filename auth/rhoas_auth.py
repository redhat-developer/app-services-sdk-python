from keycloak import KeycloakOpenID
from os import environ

from auth.constants import DEFAULT_AUTH_URL, DEFAULT_CLIENT_ID, REALM_NAME;

def get_access_token(offline_token):
    try:
        if offline_token is None:
            offline_token = environ.get('OFFLINE_TOKEN')
    except KeyError:
        print("Offline token not found in environment variables")
        return None
    
    # Configure keycloak_openid client 
    keycloak_openid = KeycloakOpenID(server_url=DEFAULT_AUTH_URL,
                                 client_id=DEFAULT_CLIENT_ID,
                                 realm_name=REALM_NAME,
                                 )
    # Refresh token
    token = keycloak_openid.refresh_token(offline_token)
    return token
