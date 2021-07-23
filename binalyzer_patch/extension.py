"""
    binalyzer_patch.extension
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    This module implements the Binalyzer patch extension.
"""
from binalyzer_core import BinalyzerExtension

class PatchExtension(BinalyzerExtension):
    def __init__(self, binalyzer=None):
        super(PatchExtension, self).__init__(binalyzer, "patch")

    def init_extension(self):
        super(PatchExtension, self).init_extension()
