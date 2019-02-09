#!/usr/bin/python

import whois

import subprocess

domain_answer = whois.whois('95.210.48.0')

#print(domain_answer.country)

print(domain_answer)