# Copyright 2018 Matthew Treinish
#
# This file is part of pyopnsense
#
# pyopnsense is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyopnsense is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyopnsense. If not, see <http://www.gnu.org/licenses/>.


import json

import mock

from pyopnsense import client
from pyopnsense import exceptions
from pyopnsense.tests import base


class TestOPNClient(base.TestCase):

    @mock.patch('requests.get')
    def test_success(self, request_mock):
        response_mock = mock.MagicMock()
        response_mock.status_code = 200
        response_mock.text = json.dumps({'a': 'body'})
        request_mock.return_value = response_mock
        opnclient = client.OPNClient('', '', '')
        resp = opnclient._get('fake_url')
        self.assertEqual({'a': 'body'}, resp)

    @mock.patch('requests.get')
    def test_failures(self, request_mock):
        response_mock = mock.MagicMock()
        response_mock.status_code = 401
        response_mock.text = json.dumps({'a': 'body'})
        request_mock.return_value = response_mock
        opnclient = client.OPNClient('', '', '')
        self.assertRaises(exceptions.APIException, opnclient._get, 'fake_url')
