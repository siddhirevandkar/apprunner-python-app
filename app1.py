from flask import Flask, jsonify, request, render_template
from pprint import pprint
import boto3
from botocore.exceptions import ClientError
import os

def index(request):
  pprint("This is Python Application displaying Hello World!")
