#!/usr/bin/env bash

set -e
set -x

ruff communal tests --fix
black communal tests --check
