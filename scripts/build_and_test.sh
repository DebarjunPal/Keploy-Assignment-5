#!/bin/bash
# Build orgChartApi with tests and run them
cd ../orgChartApi
mkdir -p build && cd build
cmake .. -DENABLE_TESTS=ON
make
ctest --output-on-failure
