from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
import json, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = '\\'.join([ROOT_DIR, 'config.json'])

# read config file
with open(config_path) as config_file:
    config = json.load(config_file)
    config = config['share_point']

username = config['user']
password = config['password']
url = config['url']
site = config['site']
doc = config['doc_library']
relative_url = site + doc

ctx_auth = AuthenticationContext(url)
ctx_auth.acquire_token_for_user(username, password)   
ctx = ClientContext(url, ctx_auth)
response = File.open_binary(ctx,relative_url)
with open("data.csv", "wb") as local_file:
    local_file.write(response.content)


