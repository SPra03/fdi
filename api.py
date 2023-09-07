from fastapi import FastAPI
from fastapi.responses import FileResponse
from datapackage import Package, Resource
import pandas as pd
import requests
import tempfile
import shutil
import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from datapackage import Package

app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing) settings
origins = ["*"]  # You can specify specific origins instead of "*"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific HTTP methods here
    allow_headers=["*"],  # You can specify specific HTTP headers here
)

@app.post("/process_and_download/{dataset_name}")
async def process_and_download(dataset_name: str):   #,odc_key: str 
    # Create a data package
    package = Package()
    # Perform processing (replace this with your actual processing logic)
    package.infer(f"{dataset_name}/{dataset_name}.csv")
    package.infer(f"{dataset_name}/{dataset_name}_dictionary.csv")
    package.commit()
    
    # Define the filename for the resulting zip file
    file_name = f"{dataset_name}_data_package.zip"
    # Save the data package as a zip file
    package.save(file_name)

    # Move the zip file to the appropriate directory (optional)
    # shutil.move(file_name, "path_to_directory_where_you_want_to_store_the_zip")

    # Return the zip file as a response
    return FileResponse(file_name)