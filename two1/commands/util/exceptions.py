import click


class Two1Error(click.ClickException):
    """ A generic Two1Error """

    def __init__(self, msg="", json={}):
        self._msg = msg
        self._json = json
        super(Two1Error, self).__init__(self._msg)

    def __str__(self):
        return self._msg

    def show(self, file=None):
        """ Prints the error message to standard out or to a file

            Two1Error overwrites the show function because ClickException.show
            prefixes "Error:" to the error message which causes some undesireable
            UX effects.
        """
        click.echo(str(self.format_message()), file=file)


class UnloggedException(Two1Error):
    """ An error used to exit out of a commnad and not log the exception """


class MiningDisabledError(UnloggedException):
    """ A error indicating that the mining limit has been reached """


class UpdateRequiredError(UnloggedException):
    """ Error during a request os made and the client is out of date """


class FileDecodeError(Exception):
    """ Error when a config file cannot be decoded """


class ServerRequestError(click.ClickException):
    """ Error during a request to a server """

    def __init__(self, msg="", response=None, status_code=None, data=None):
        super(ServerRequestError, self).__init__(msg)
        if response:
            self.status_code = response.status_code
            try:
                self.data = response.json()
            except ValueError:
                self.data = {"error": "Request Error"}
        else:
            self.status_code = status_code
            self.data = data


class ServerConnectionError(click.ClickException):
    """Error during a connection to a server"""

    def __init__(self, msg=""):
        super(ServerConnectionError, self).__init__(msg)


class BitcoinComputerNeededError(ServerRequestError):
    """ Error during a request made on a protected api """
