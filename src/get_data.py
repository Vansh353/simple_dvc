##read parameters
##process
##return the dataframe
import os
import yaml
import pandas as pd # type: ignore
import argparse

def read_params(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config

def get_data(config_path):
    config=read_params(config_path)
    print(config)   
    data_path=config["data_source"]["s3_source"]
    df=pd.read_csv(data_path,sep=",",encoding="utf-8")
    return df
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",default="params.yaml")
    args = parser.parse_args()
    data=get_data(config_path=args.config)
    
   

