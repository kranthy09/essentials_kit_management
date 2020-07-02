# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetFormAPITestCase::test_case status'] = 200

snapshots['TestCase01GetFormAPITestCase::test_case body'] = {
    'closing_date': '2020-06-27 18:30:08.678809',
    'form_id': 1,
    'form_name': 'title0',
    'sections': [
    ]
}

snapshots['TestCase01GetFormAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '99',
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
