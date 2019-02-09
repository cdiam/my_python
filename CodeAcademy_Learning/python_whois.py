#!/usr/bin/python

import whois
domains = ['http://www.example.com']

for dom in domains:
    domain = whois.Domain(dom)
    print domain.registrar 