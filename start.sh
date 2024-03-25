set -ue

export PYTHONUNBUFFERED=true

VIRTUAL=.data/venv

if [ ! -d $VIRTUAL ]; then
    python3 -m venv $VIRTUAL
fi

if [ ! -f $VIRTUAL/bin/pip ]; then
    curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | $VIRTUAL/bin/python
fi

$VIRTUAL/bin/pip install -r requirements.txt

$VIRTUAL/bin/python start.py
