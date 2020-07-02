# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetListOfFormsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetListOfFormsAPITestCase::test_case body'] = [
    {
        'closing_date': '2020-07-02',
        'cost_incurred': 0,
        'form_id': 1,
        'form_name': 'aDROJA',
        'form_state': 'CLOSED',
        'next_delivery_date': '2020-07-02',
        'pending_items': 0,
        'total_cost_estimate': 0,
        'total_items': 0
    }
]

snapshots['TestCase01GetListOfFormsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '213',
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

snapshots['TestCase01GetListOfFormsAPITestCase::test_case form_name'] = 'aDROJA'

snapshots['TestCase01GetListOfFormsAPITestCase::test_case form_state'] = 'CLOSED'

snapshots['TestCase01GetListOfFormsAPITestCase::test_case closing_date'] = GenericRepr('datetime.datetime(2020, 7, 2, 11, 22, 0, 936937)')

snapshots['TestCase01GetListOfFormsAPITestCase::test_case next_delivery_date'] = GenericRepr('datetime.datetime(2020, 7, 2, 11, 22, 0, 936963)')

snapshots['TestCase01GetListOfFormsAPITestCase::test_case total_items'] = 21

snapshots['TestCase01GetListOfFormsAPITestCase::test_case total_cost_estimate'] = 1535

snapshots['TestCase01GetListOfFormsAPITestCase::test_case pending_items'] = 2

snapshots['TestCase01GetListOfFormsAPITestCase::test_case cost_incurred'] = 1696
