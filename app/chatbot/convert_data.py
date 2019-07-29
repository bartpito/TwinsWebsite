#!/usr/bin/env python3

from rasa.nlu.training_data import load_data
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file',)
parser.add_argument('output_file')

args = parser.parse_args()

with open(args.output_file, 'w') as f:
  f.write(load_data(args.input_file).as_markdown())




