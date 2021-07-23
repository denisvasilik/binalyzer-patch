"""
    binalyzer_patch.cli
    ~~~~~~~~~~~~~~~~~~~

    Patch extension for the *binalyzer* command.
"""
import click
import io

from binalyzer import (
    Binalyzer,
    ExpandedFile,
    BasedIntParamType,
)


@click.command()
@click.option('--input-file', '-i', required=True, type=ExpandedFile("rb"), help='The binary file to patch.')
@click.option('--patch-file', '-p', required=True, type=ExpandedFile("rb"), help='The patch file.')
@click.option('--output-file', '-o', required=True, type=ExpandedFile("w"), help='The patched binary file.')
def patch(input_file, patch_file, output_file):
    """Patch a binary file using a patch file.
    """
