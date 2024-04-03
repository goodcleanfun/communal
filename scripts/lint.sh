#!/usr/bin/env bash

set -e
set -x

ruff check communal tests --fix
black communal tests --check
