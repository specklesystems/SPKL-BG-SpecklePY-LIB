# This class is intended to work in conjunction with the specklepy class, not replace it!
from specklepy.api.client import SpeckleClient

# Können wir besser machen (?) - class Client(SpeckleClient) mit super().__init__()
class Client(SpeckleClient):

    def __init__(self,
                speckle_server: str,
                speckle_token: str) -> None:

        '''
        Access the SpeckleClient object for a given server using an authorization token.

        Args:
            speckle_server (str): Server url for the desired stream.
            speckle_token (str): Personal access token. For more information refer to https://speckle.guide/dev/tokens.html

        Returns:
            specklepy.api.client.SpeckleClient: SpeckleClient object is returned.
        '''
        super().__init__(host=speckle_server)
        self.authenticate_with_token(speckle_token)
        self.speckle_server = speckle_server
        self.speckle_token = speckle_token
    