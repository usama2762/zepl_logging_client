from zepl_logging import logging


def test_info():
	logger = logging.Logging()
	logger.base_config('de648d61bb480053bc96598a4a2227008d7c8216', notebook='test_NB', organization='pytest')
	assert logger.info('This is a info message')== "<Response [200]>"

def test_debug():
	logger = logging.Logging()
	logger.base_config('de648d61bb480053bc96598a4a2227008d7c8216', notebook='test_NB', organization='pytest')
	assert logger.debug('This is a debug message')== "<Response [200]>"

def test_warning():
	logger = logging.Logging()
	logger.base_config('de648d61bb480053bc96598a4a2227008d7c8216', notebook='test_NB', organization='pytest')
	assert logger.warning('This is a warning message')== "<Response [200]>"

def test_error():
	logger = logging.Logging()
	logger.base_config('de648d61bb480053bc96598a4a2227008d7c8216', notebook='test_NB', organization='pytest')
	assert logger.error('This is a error message')== "<Response [200]>"

def test_critical():
	logger = logging.Logging()
	logger.base_config('de648d61bb480053bc96598a4a2227008d7c8216', notebook='test_NB', organization='pytest')
	assert logger.critical('This is a critical message')== "<Response [200]>"