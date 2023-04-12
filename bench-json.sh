#!/bin/bash
#
# Run Python JSON benchmarks to find the fastest module that can be used as a drop-in replacement of the `json` standard one.
#
set -eu

VENV='venv-bench-json'
PYTHON="${VENV}/bin/python"

# Python module to import
MODULES='fast_json orjson rapidjson simdjson simplejson ujson'

cleanup() {
    deactivate 2>/dev/null || true
    [ -d "${VENV}" ] && rm -rf "${VENV}"
}

main() {
    cleanup

    python3 -m venv "${VENV}"
    source "${VENV}/bin/activate"

    ${PYTHON} -m pip install -U pip wheel >/dev/null || exit 1
    ${PYTHON} -m pip install -r requirements.txt >/dev/null || exit 1

    echo -n 'Run at '
    date '+%Y-%m-%d %Hh%M'
    echo

    ${PYTHON} -V
    ${PYTHON} 'bench-json.py' ${MODULES}
    cleanup
}

main || cleanup
