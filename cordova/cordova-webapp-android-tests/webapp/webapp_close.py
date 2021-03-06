#!/usr/bin/env python
#
# Copyright (c) 2015 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Lin, Wanming <wanming.lin@intel.com>

import unittest
import os, sys, commands
import comm
import time

class TestWebAppFunctions(unittest.TestCase):
    def test_close(self):
        comm.setUp()
        app_name = "helloworld"
        pkg_name = "com.example." + app_name.lower()
        if not comm.check_app_installed(pkg_name, self):
            comm.app_install(app_name, pkg_name, self)
        # Find whether the app have launched
        cmd_acti = "adb -s " + comm.device + " shell ps | grep %s" % pkg_name
        launched = commands.getstatusoutput(cmd_acti)
        if launched[0] != 0:
            print "Close app ---------------->%s App haven't launched, need to launch it!" % app_name
            cmd_start = "adb -s " + comm.device + " shell am start -n %s/.%s" % (pkg_name, app_name)
            comm.app_launch(cmd_start, self)
            time.sleep(1)
        cmd_close = "adb -s " + comm.device + " shell am force-stop %s" % pkg_name
        comm.app_stop(cmd_close, self)

if __name__ == '__main__':  
    unittest.main()
