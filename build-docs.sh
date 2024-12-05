#!/usr/bin/env bash
lazydocs \
    --output-path="./docs/docstrings" \
    --overview-file="README.md" \
    --src-base-url="https://github.com/souStypit/git-cicd/main/" \
    <folder with source code>

mkdocs build
