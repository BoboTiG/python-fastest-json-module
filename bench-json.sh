#!/bin/bash
#
# Run Python JSON benchmarks to find the fastest module that can be used as a drop-in replacement of the `json` standard one.
#
set -eu

VENV='venv-bench-json'
PYTHON="${VENV}/bin/python"

# Python module name to install from PyPi
LIBS='fast_json orjson python-rapidjson pysimdjson simplejson ujson'
# Python module to import
MODS='fast_json orjson rapidjson simdjson simplejson ujson'

cleanup() {
    deactivate 2>/dev/null || true
    [ -d "${VENV}" ] && rm -rf "${VENV}"
}

main() {
    cleanup

    python3 -m venv "${VENV}"
    source "${VENV}/bin/activate"

    ${PYTHON} -m pip install -U pip wheel >/dev/null
    ${PYTHON} -m pip install -U ${LIBS} >/dev/null || exit 1

    echo -n 'Run from '
    date '+%Y-%m-%d %Hh%M'
    echo

    ${PYTHON} -V
    ${PYTHON} -m pip freeze | while read line; do echo "    ${line}"; done
    echo

    ${PYTHON} 'bench-json.py' ${MODS}
    cleanup
}

main || cleanup
