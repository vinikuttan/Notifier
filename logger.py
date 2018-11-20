import logging
import os

from sms_exceptions import BadArgumentError, NotFoundError

error_log = None
info_log = None


def initialize_logger():
    """initializing logger objects """
    # create log files
    file_ = File()
    file_.create(['error.log', 'info.log'])

    # log intialize
    elogger = logging.getLogger('error_log')
    elogger.setLevel(logging.DEBUG)

    error_handler = logging.FileHandler('error.log')
    elogger.addHandler(error_handler)

    ilogger = logging.getLogger('info_log')
    ilogger.setLevel(logging.DEBUG)

    info_handler = logging.FileHandler('info.log')
    ilogger.addHandler(info_handler)
    return elogger, ilogger


class File(object):
    def __init__(self, directory=None):
        """ intializing """
        if directory and os.path.isdir(directory):
            self.dir_ = directory
        else:
            self.dir_ = os.getcwd()

    def create(self, filename_list=None):
        """ doc """
        if not filename_list:
            raise NotFoundError("No list of filenames provided to create")

        if not isinstance(filename_list, list):
            raise BadArgumentError("filename_list should be of <list> type")

        for file_ in filename_list:
            open(self.dir_ + os.sep + file_, 'w').close()

    def remove(self, remove_files):
        """ doc """
        if not isinstance(remove_files, list):
            raise BadArgumentError("removable file names should be of <list> type")

        for file_ in remove_files:
            located_file = os.path.isfile(self.dir_ + os.sep + file_)
            if located_file and file_ in self.filename_list:
                os.remove(located_file)
                self.filename_list.pop(file_)
