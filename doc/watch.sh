#!/bin/bash


while inotifywait -e create,delete,move,modify ./report/chap/*.md ; do ./generatedocs.sh; done