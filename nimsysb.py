#!/usr/bin/env python

# -*- coding: utf-8 -*-

from pprint import pprint
import argparse
import re
import traceback
import os
import logging
import logging.config
import logging.handlers
import subprocess

__version__ = '0.1'





class NimSYSB(object):
    """
    This library provides all the methods required to create a mksysb on a NIM server using a nas_filer object
    """

    def __init__(self, **kwargs):
        """Prepare to make a connection to the remote host
        Args:
            client (str): The NIM client we are creating the mksysb for
            nas_filer (str): The nas_filer object created to store the images.
            vfs (str): Virtual file system on the nas_filer.
        """
        allowed_params = ['nas_filer', 'nas_filer_dir', 'client' ]
        params = locals()
        for key, val in params['kwargs'].items():
            if key not in allowed_params:
                raise TypeError(
                    'Got an unexpected keyword argument {} to mehtod __init__'.format(key)
                )
            params[key] = val
        del params['kwargs']

        if ('nas_filer' not in params) or (params['nas_filer'] is None):
            raise ValueError("Missing the required parameter `nas_filer` when calling `__init__`")
        else:
            self.nas_filer = params['nas_filer']

        if ('nas_filer_dir' not in params) or (params['nas_filer_dir'] is None):
            raise ValueError("Missing the required parameter `nas_filer_dir` when calling `__init__`")
        else:
            self.nas_filer_dir = params['nas_filer_dir']

        if ('client' not in params) or (params['client'] is None):
            raise ValueError("Missing the required parameter `client` when calling `__init__`")
        else:
            self.client = params['client']

        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.NullHandler())

    def log_call(self,lvl,msg):
        self.logger.log(lvl, '===================+++{} Call+++======================='.format(__name__))
        self.logger.log(lvl, 'Message: {}'.format(msg))
        self.logger.log(lvl, '============================================================')

    def list_systems(self):
        """Helper function to list the defined standalone systems in NIM"""
        nim_clients = []
        cmd = 'lsnim -t standalone'
        for line in subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').split('\n'):
            line = line.strip().split(' ')
            nim_clients.append(line[0])
        return nim_clients

    def list_mksysb(self):
        """Helper function to list mksysb objects"""
        

    
def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--client',
                        action='store',
                        required=True,
                        dest='client',
                        help='Client name as stored on the NIM server')
    parser.add_argument('-n','--nas',
                        action='store',
                        required=True,
                        dest='nas_filer',
                        help='Specify the name of the nas_filer object in the NIM server, or master for other operations')
    parser.add_argument('--vfs',
                        action='store',
                        required=True,
                        dest='vfs',
                        help='The Virtual File System path on the NAS device')
    args = parser.parse_args()
    return args


#nimsysb = NimSYSB(nas_filer='netapp_8040', nas_filer_dir='/vol_advnim_mksysb')
#nimsysb.list_systems()
if __name__ == '__main__':
    args = getargs()
    NB = NimSYSB(nas_filer=args.nas_filer,nas_filer_dir=args.vfs,client=args.client)
    nim_clients = NB.list_systems()
    if nim_clients:
        pprint(nim_clients, depth=4)


