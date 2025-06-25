import stackstac, pystac_client, xarray as xr, zarr, s3fs

def stac_to_zarr():
    catalog = pystac_client.Client.open("https://earth-search.aws.element84.com/v1")
    items = catalog.search(collections=["sentinel-s2-l2a"], bbox=[5, 43, 8, 46], datetime="2024-06-01/2024-06-30").items()
    da = stackstac.stack(items, resolution=10)
    da.to_dataset(name="reflectance").coarsen(time=1).mean().to_zarr("s3://greencover/zarr", mode="w")
