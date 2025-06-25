from fastapi import FastAPI
import xarray as xr

app = FastAPI()
da = xr.open_zarr("s3://greencover/zarr", chunks={"time":1})

@app.get("/ndvi/{x}/{y}/{time}")
def ndvi(x:int, y:int, time:int):
    red = da.sel(band="B04").isel(x=x,y=y,time=time)
    nir = da.sel(band="B08").isel(x=x,y=y,time=time)
    return {"ndvi": float((nir-red)/(nir+red))}
