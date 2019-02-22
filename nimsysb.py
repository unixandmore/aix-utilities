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
            host (str): Hostname or IP address of the remote AIX system, if hostname is used it must be in DNS or /etc/hosts
            username (str): Defaults to root
            sshkey (str): Full path to the key being used to allow remote access to the AIX system
        """
        allowed_params = ['nas_filer', 'nas_filer_dir' ]
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


        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.NullHandler())

    def log_call(self,lvl,msg):
        self.logger.log(lvl, '===================+++{} Call+++======================='.format(__name__))
        self.logger.log(lvl, 'Message: {}'.format(msg))
        self.logger.log(lvl, '============================================================')

    def list_systems(self):
        """Helper function to list the defined standalone systems in NIM"""
        cmd = 'lsnim -t standalone'
        process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            output = process.stdout.readline().decode('utf-8').strip()
            if output:
                print('{}'.format(output.strip()))
    
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
                            dest='server',
                            help='Specify the name of the nas_filer object in the NIM server, or master for other operations')
        parser.add_argument('--vfs',
                            action='store',
                            required=True,
                            dest='vfs',
                            help='The Virtual File System path on the NAS device')
        args = parser.parse_args()
        return args


nimsysb = NimSYSB(nas_filer='netapp_8040', nas_filer_dir='/vol_advnim_mksysb')
nimsysb.list_systems()
if __name__ == '__main__':
    args = getargs()

