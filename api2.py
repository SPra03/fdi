from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from datapackage import Package
import shutil

app = FastAPI()

# Directory where datasets are stored
dataset_directory = "datasets"  # Update this with your dataset directory

@app.get("/get_dataset")
async def get_dataset(dataset_name: str):
    try:
        # Construct the path to the dataset file
        dataset_file_path = f"{dataset_directory}/{dataset_name}/{dataset_name}.csv"

        # Check if the file exists
        package = Package()
        resource = package.get_resource(dataset_file_path)
        if not resource:
            raise HTTPException(status_code=404, detail="Dataset not found")

        # Return the dataset file as a response
        return FileResponse(dataset_file_path, media_type="text/csv", filename=f"{dataset_name}.csv")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/process_and_download")
async def process_and_download(dataset_name: str):
    try:
        # Create a data package
        package = Package()

        # Perform processing (replace this with your actual processing logic)
        package.infer(f"{dataset_directory}/{dataset_name}/{dataset_name}.csv")
        package.infer(f"{dataset_directory}/{dataset_name}/{dataset_name}_dictionary.csv")
        package.commit()

        # Define the filename for the resulting zip file
        file_name = f"{dataset_name}_data_package.zip"

        # Save the data package as a zip file
        package.save(file_name)

        # Return the zip file as a response
        return FileResponse(file_name)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# https://odc-sci.org/php/odc-file-download.php?cid=97&type=doi&key=227dee630fd45daff6932eeaba4f669dccbb6649c7385ab5d8e832e43ce18912&doi=odc-sci_851
# sci_851
