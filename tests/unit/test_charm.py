#!/usr/bin/env python3

# Copyright 2024 Canonical Limited
# See LICENSE file for licensing details.

import logging

from ops import MaintenanceStatus
from scenario import Container, State

from constants import KYUUBI_CONTAINER_NAME

logger = logging.getLogger(__name__)


def test_start_kyuubi(kyuubi_context):
    state = State(
        config={},
        containers=[Container(name=KYUUBI_CONTAINER_NAME, can_connect=False)],
    )
    out = kyuubi_context.run("install", state)
    assert out.unit_status == MaintenanceStatus("Waiting for Pebble")
