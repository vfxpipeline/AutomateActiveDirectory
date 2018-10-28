"""
Name: AD BOT - Execute commands on server
Author :  Rajiv Sharma
Developer Website : www.hqvfx.com
Developer Email   : rajiv@hqvfx.com
Date Started : 27 Oct 2018
Date Modified :
Description : Run Directory Service Commands to AD Server

Source Code Website : www.github.com/vfxpipeline
Watch Video Tutorials : www.youtube.com/vfxpipeline

Copyright (c) 2018, HQVFX(www.hqvfx.com) . All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.

    * Neither the name of HQVFX(www.hqvfx.com) nor the names of any
      other contributors to this software may be used to endorse or
      promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import argparse
import datetime
import rpyc
from rpyc.utils.server import ThreadedServer
import subprocess

date_time = datetime.datetime.now()


class MonitorService(rpyc.Service):
    def on_connect(self, connection):
        print('\nConnected on {}'.format(date_time))

    def on_disconnect(self, connection):
        print('Disconnected on {}\n'.format(date_time))

    def exposed_run_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True)
            print(output)
        except subprocess.CalledProcessError as Error:
            print(Error.returncode)
            print(Error.output)


def main():
    parser = argparse.ArgumentParser(description='Active Directory BOT')
    parser.add_argument('-port', type=int, help="Enter custom port number")
    args = parser.parse_args()
    port = args.port
    if not port:
        port = 19961
    t = ThreadedServer(MonitorService, port=port)
    t.start()


if __name__ == "__main__":
    main()
