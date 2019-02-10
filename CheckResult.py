#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys
import urlparse

domain = urlparse.urlparse(sys.argv[-1]).netloc.replace(':', '_')
if not os.listdir(domain):
    os.rmdir(domain)
    print("[!]目标 " + str(domain) + " 无文件，删除。")
