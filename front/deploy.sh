#!/bin/bash

sh credentials.sh
npm run build
aws s3 sync ./dist s3://bd-2020-1-trabalho-final
