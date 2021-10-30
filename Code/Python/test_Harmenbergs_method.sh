#!/bin/bash

# Install requirements for Harmenberg test, if not already installed
if [ ! -e requirements_Harmenberg.out ]; then
    pip freeze --user > requirements_user.txt # Store original setup
    pip install --user -r requirements_Harmenberg.txt > requirements_Harmenberg.out
fi

# Descend to the point in the HARK toolkit where the tests are executed
pushd .
cd src/econ-ark/HARK/ConsumptionSaving/tests

# Execute only the test of Harmenberg's method
pytest --log-cli-level=DEBUG test_IndShockConsumerType.py -k test_Harmenbergs_method

# Return to original point
popd 

# Restore original setup
pip install --user -r requirements_user.txt
