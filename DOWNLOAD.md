Dataset **Full Body TikTok Dancing** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/i/q/Qa/Ug2c7Sv9KTezoCvTGgCGS52mlVhjkWebADgroFLRNoYBbfPpi1m44FYCPHv1OUhHGxV5gerPYoAkZBaWODru66sIViJ2AfLzHtK7H2MlDLUhr264eEXPDgw7rT9E.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Full Body TikTok Dancing', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-tiktok-dancing-dataset/download?datasetVersionNumber=2)