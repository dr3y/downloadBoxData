# Import two classes from the boxsdk module - Client and OAuth2
from boxsdk import Client, OAuth2
from boxsdk.network.default_network import DefaultNetwork
from pprint import pformat


class LoggingNetwork(DefaultNetwork):
    def request(self, method, url, access_token, **kwargs):
        """ Base class override. Pretty-prints outgoing requests and incoming responses. """
        #print "\x1b[36m{} {} {}\x1b[0m".format(method, url, pformat(kwargs))
        response = super(LoggingNetwork, self).request(
            method, url, access_token, **kwargs
        )
        if response.ok:
            #print '\x1b[32m{}\x1b[0m'.format(response.content)
            pass
        else:
            pass
            #print '\x1b[31m{}\n{}\n{}\x1b[0m'.format(
                #response.status_code,
                #response.headers,
                #pformat(response.content),
            #)
        return response

def getFilesFromFolder(folderid="75058858589",frompath="",topath=""):
    """gets all the files from a folder and puts them into
    the corresponding path"""
    # Define client ID, client secret, and developer token.
    CLIENT_ID = None
    CLIENT_SECRET = None
    ACCESS_TOKEN = None
    # Read app info from text file
    with open('app.cfg', 'r') as app_cfg:
        CLIENT_ID = app_cfg.readline().strip()
        CLIENT_SECRET = app_cfg.readline().strip()
        ACCESS_TOKEN = app_cfg.readline().strip()
    # Create OAuth2 object. It's already authenticated, thanks to the developer token.
    oauth2 = OAuth2(CLIENT_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN)
    print("got authentication")
    #print(oauth2)
    # Create the authenticated client
    client = Client(oauth2)#, LoggingNetwork())
    print("made client")
    for item in client.folder(folder_id=folderid).get_items(limit=1000):
        path = 'anyFileName.xlsx'
        with open(path, 'wb') as f:
            client.file(file_id).download_to(f)

if __name__ == '__main__':
    getFilesFromFolder()
