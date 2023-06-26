#!/bin/bash

pkill -f allure
allure generate reports/allure-results -o reports/allure-report --clean && allure open reports/allure-report