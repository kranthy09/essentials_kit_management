# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetListOfFormsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetListOfFormsAPITestCase::test_case body'] = [
    {
        'closing_date': '2020-06-26',
        'cost_incurred': 1674,
        'form_id': 1,
        'form_name': 'title0',
        'form_state': 'DONE',
        'next_delivery_date': '2020-06-26',
        'pending_items': -2,
        'total_cost_estimate': 2090,
        'total_items': 25
    }
]

snapshots['TestCase01GetListOfFormsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '219',
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

snapshots['TestCase01GetListOfFormsAPITestCase::test_case form_id'] = 1

snapshots['TestCase01GetListOfFormsAPITestCase::test_case form_name'] = 'title0'

snapshots['TestCase01GetListOfFormsAPITestCase::test_case form_state'] = 'DONE'

snapshots['TestCase01GetListOfFormsAPITestCase::test_case closing_date'] = GenericRepr('datetime.datetime(2020, 6, 26, 16, 40, 16, 490151)')

snapshots['TestCase01GetListOfFormsAPITestCase::test_case next_delivery_date'] = GenericRepr('datetime.datetime(2020, 6, 26, 16, 40, 16, 490175)')

snapshots['TestCase01GetListOfFormsAPITestCase::test_case total_items'] = 21

snapshots['TestCase01GetListOfFormsAPITestCase::test_case total_cost_estimate'] = 1535

snapshots['TestCase01GetListOfFormsAPITestCase::test_case pending_items'] = 2

snapshots['TestCase01GetListOfFormsAPITestCase::test_case cost_incurred'] = 1696
