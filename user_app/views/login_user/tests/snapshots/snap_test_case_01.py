# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01LoginUserAPITestCase::test_case status'] = 201

snapshots['TestCase01LoginUserAPITestCase::test_case body'] = {
    'access_token': 'token',
    'expires_in': '10000',
    'refresh_token': 'refresh_token',
    'user_id': 1
}

snapshots['TestCase01LoginUserAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '96',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}

snapshots['TestCase01LoginUserAPITestCase::test_case username'] = 'jasper'

snapshots['TestCase01LoginUserAPITestCase::test_case user_id'] = 1

snapshots['TestCase01LoginUserAPITestCase::test_case access_token'] = 'token'

snapshots['TestCase01LoginUserAPITestCase::test_case refresh_token'] = 'refresh_token'

snapshots['TestCase01LoginUserAPITestCase::test_case expires_in'] = '10000'
