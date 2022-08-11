#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

from SSR import ssr_tool

def Main():
    """The main function."""

    print("SSR(Storage Space Reconstructor)")
    print('URL -> https://github.com/KimVegetable/StorageSpaceReconstructor\n')
    print('---------------------------------------------------------------------')
    print()
    sys.stdout.flush()

    tool = ssr_tool.StorageSpaceReconstructorTool()

    if not tool.ParseArguments(sys.argv[1:]):
        tool.ShowInfo()
        return False

    if tool.show_info:
        tool.ShowInfo()
        return True

    tool.ReconstructVirtualDisk()

    return True


if __name__ == '__main__':

    if not Main():
        sys.exit(1)
    else:
        sys.exit(0)
