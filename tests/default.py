#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  default.py
#
#  Copyright 2018 Jelle Smet <development@smetj.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


from wishbone.actorconfig import ActorConfig
from wishbone_output_file import FileOut
from wishbone.event import Event
from gevent import sleep
import os


def test_module_init():

    actor_config = ActorConfig('FileOut', 100, 1, {}, "")
    d = FileOut(actor_config)
    d.start()
    assert d.name == "FileOut"


def test_module_write():

    actor_config = ActorConfig('FileOut', 100, 1, {}, "", disable_exception_handling=True)
    d = FileOut(actor_config, directory="/tmp")
    d.pool.queue.inbox.disableFallThrough()
    d.start()

    e = Event("hello")
    d.submit(e, "inbox")

    sleep(1)
    try:
        with open('/tmp/wishbone', 'r') as f:
            assert f.readlines() == ["hello"]
    except Exception as err:
        assert False, err
    else:
        assert True
    finally:
        try:
            os.unlink("/tmp/wishbone")
        except Exception:
            pass


def test_module_write_append():

    with open("/tmp/wishbone", "w") as f:
        f.write("hello")

    actor_config = ActorConfig('FileOut', 100, 1, {}, "", disable_exception_handling=True)
    d = FileOut(actor_config, directory="/tmp")
    d.pool.queue.inbox.disableFallThrough()
    d.start()

    e = Event("hello")
    d.submit(e, "inbox")

    sleep(1)
    try:
        with open('/tmp/wishbone', 'r') as f:
            assert f.readlines() == ["hellohello"]
    except Exception as err:
        assert False, err
    else:
        assert True
    finally:
        try:
            os.unlink("/tmp/wishbone")
        except Exception:
            pass


def test_module_write_overwrite():

    with open("/tmp/wishbone", "w") as f:
        f.write("hello")

    actor_config = ActorConfig('FileOut', 100, 1, {}, "", disable_exception_handling=True)
    d = FileOut(actor_config, directory="/tmp", overwrite=True)
    d.pool.queue.inbox.disableFallThrough()
    d.start()

    e = Event("cheers")
    d.submit(e, "inbox")

    sleep(1)
    try:
        with open('/tmp/wishbone', 'r') as f:
            assert f.readlines() == ["cheers"]
    except Exception as err:
        assert False, err
    else:
        assert True
    finally:
        try:
            os.unlink("/tmp/wishbone")
        except Exception:
            pass
