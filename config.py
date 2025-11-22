# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = 'lajoyazyh'

# The repository to add this issue to
REPO_OWNER = 'lajoyazyh'
REPO_NAME = 'ArXivDaily_lajoya'

# Set new submission url of subject
NEW_SUB_URL = 'https://arxiv.org/list/cs/new'

# Keywords to search
KEYWORD_LIST = ["Human-Computer Interaction", "Machine Learning", "Artificial Intelligence", "Cryptography and Security", "Computer Vision and Pattern Recognition", "HCI"]
# Keywords to exclude
KEYWORD_EX_LIST = [""]
# Note that the 'Keywords' above are actually searched in the abstract instead of the real keyword section. 
