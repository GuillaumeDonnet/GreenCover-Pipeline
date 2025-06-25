import pytorch_lightning as pl
from torchgeo.datamodules import EuroSATDataModule
from torchgeo.models import UNet

dm = EuroSATDataModule("data/", batch_size=32)
model = UNet(in_channels=13, classes=10)
trainer = pl.Trainer(max_epochs=20)
if __name__ == "__main__":
    trainer.fit(model, dm)
