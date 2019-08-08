#!/usr/bin/env python3

from rasa.core.channels.slack import SlackInput
from rasa.core.agent import Agent
from rasa.utils.endpoints import EndpointConfig

action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

agent = Agent.load(model_path='./models/20190716-155457.tar.gz',
                   action_endpoint=action_endpoint)
input_channel = SlackInput("xoxb-101095839045-681604410210-Gan6Q7z7tRXwAEoSbsvV5pjM")


if __name__ == '__main__':
  agent.handle_channels([input_channel], 5002)
