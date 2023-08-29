#!/bin/bash

curl https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops > input.txt
cat input.txt | html2text > input.txt