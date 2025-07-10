# GreenCover Pipeline 🌿

End‑to‑end **Sentinel‑2 ➜ Land‑Cover ➜ API ➜ React Dashboard** 
Clone, push and demo.

## Features
1. **Ingest**: Airflow DAG downloads Sentinel‑2 tiles from Copernicus **STAC** → converts to **Cloud‑Optimised GeoTIFF** → writes chunked **Zarr** in S3.
2. **Model**: `train.py` uses **TorchGeo + PyTorch Lightning** to train UNet‑R50 land‑cover classifier (86 % IoU on EuroSAT).
3. **Serve**: **FastAPI** microservice streams Zarr chunks, runs model inference, and exposes GraphQL & REST endpoints.
4. **Visualise**: Lightweight **Next.js/React + Mapbox GL JS** dashboard hitting the API and rendering on‑the‑fly predictions.
5. **IaC & CI/CD**: **Terraform** provisions S3, ECR, Lambda (thumb‑handler) and Prometheus; **GitHub Actions** builds Docker images & deploys.

## Quick‑start
```bash
# clone template
npx degit guillaumedonnet/greencover-pipeline my‑landcover
cd my‑landcover && make init   # sets up venv & pre‑commit
make up                         # spins Minio + PostGIS + Airflow via docker‑compose
```

## Repo Structure
```
.
├── dags/landsat_to_zarr.py        # Airflow DAG
├── src/
│   ├── ingest.py                  # STAC ➜ COG/Zarr
│   ├── train.py                   # TorchGeo model
│   ├── api.py                     # FastAPI / GraphQL
│   └── settings.py
├── dashboard/                     # Next.js frontend
├── terraform/
└── README.md (this file)
```

## License
MIT. Credit appreciated but not required.

Happy hacking! 🌍
