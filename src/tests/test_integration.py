# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#config_loader.py
from fileinput import filename
import yaml
import argparse


#Default location of config file
# default_file_path='config.yaml'
test_config_file='./test_config.yaml'

class _Config:
    
    def __init__(self):
        

        args=self.read_command_line()
        #print("command line args is", args.filename)
        if args.filename is not None:
            self.load_yaml(args.filename)
        else:
            #self.load_yaml(default_file_path)
            self.load_yaml(test_config_file)    

    
   #load config yaml     
    def load_yaml(self,file_path):
        with open(file_path, "r") as f:
            self.config = yaml.safe_load(f)


    #Read command line argument         

    def read_command_line(self):
        # Create the parser
        parser = argparse.ArgumentParser()
        # Add an argument to get an alternate config file
        parser.add_argument('--filename', type=str)
        # Parse the argument
        args = parser.parse_args()
        
        return args

    def __getattr__(self, name):
        try:
            return self.config[name]
        except KeyError:
            return getattr(self.args, name)


config = _Config()