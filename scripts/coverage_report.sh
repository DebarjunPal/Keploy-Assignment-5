#!/bin/bash
# Generate code coverage report using gcov/lcov
cd ../orgChartApi/build
lcov --capture --directory . --output-file coverage.info
lcov --remove coverage.info '/usr/*' --output-file coverage.info
lcov --list coverage.info
