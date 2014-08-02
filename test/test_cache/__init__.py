# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2013 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.

import hashlib
from default import Test
from pybossa.cache import get_key_to_hash, get_hash_key


class TestCache(Test):
    def test_00_get_key_to_hash_with_args(self):
        """Test CACHE get_key_to_hash with args works."""
        expected = ':1:a'
        key_to_hash = get_key_to_hash(1, 'a')
        err_msg = "Different key_to_hash %s != %s" % (key_to_hash, expected)
        assert key_to_hash == expected, err_msg

    def test_01_get_key_to_hash_with_kwargs(self):
        """Test CACHE get_key_to_hash with kwargs works."""
        expected = ':1:a'
        key_to_hash = get_key_to_hash(page=1, vowel='a')
        err_msg = "Different key_to_hash %s != %s" % (key_to_hash, expected)
        assert key_to_hash == expected, err_msg

    def test_02_get_key_to_hash_with_args_and_kwargs(self):
        """Test CACHE get_key_to_hash with args and kwargs works."""
        expected = ':1:a'
        key_to_hash = get_key_to_hash(1, vowel='a')
        err_msg = "Different key_to_hash %s != %s" % (key_to_hash, expected)
        assert key_to_hash == expected, err_msg

    def test_03_get_hash_key(self):
        """Test CACHE get_hash_key works."""
        prefix = 'prefix'
        key_to_hash = get_key_to_hash(1, vowel=u'ñ')
        tmp = key_to_hash.encode('utf-8')
        expected = prefix + ":" + hashlib.md5(tmp).hexdigest()
        key = get_hash_key(prefix, key_to_hash)
        err_msg = "The expected key is different %s != %s" % (expected, key)
        assert expected == key, err_msg
