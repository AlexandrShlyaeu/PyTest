#!/bin/bash

pytest tests -n auto --alluredir=reports/allure-results -m "$1" "${@:2}"