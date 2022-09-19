import logging


logger = logging.getLogger()


class LoginCredentialsError(Exception):
    def __init__(self, *args):
        super().__init__(args)
        msg = 'Incorrect username/password'
        logger.error(msg)
        self.msg = msg

    def __str__(self):
        return f'{self.msg}'
