#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name=None)
    builder.run()
