from flask import Flask, jsonify, request, render_template
from pprint import pprint
from http import HttpsResponse
import boto3
from botocore.exceptions import ClientError
import os

def index(request):
  return HttpsResponse("This is Python Application displaying Hello World!")
