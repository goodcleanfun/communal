#!/usr/bin/env bash

set -e
set -x

ruff {{ name }} tests --fix
black {{ name }} tests --check
