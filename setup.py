#!/usr/bin/env python

from distutils.core import setup

setup(name='Openapi2jsonschema',
      version='1.0',
      description='OpenAPI to JSON Schemas converter',
      author='Yann Hamon',
      author_email='yann@mandragor.org',
      url='http://github.com/yannh/openapi2jsonschema',
      packages=['openapi2jsonschema'],
      entry_points={
            "console_scripts": [
                  "openapi2jsonschema=openapi2jsonschema.command:default",
            ],
      },
)