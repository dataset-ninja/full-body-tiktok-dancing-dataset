Dataset **Full Body TikTok Dancing** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzkwMl9GdWxsIEJvZHkgVGlrVG9rIERhbmNpbmcvZnVsbC1ib2R5LXRpa3Rvay1kYW5jaW5nLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogImhPMWZOVUNTZjI4TTBWRVkzN2kydEtyazVCd01lYnNLMDR3UkM4ci9tdmc9In0=)

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

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-tiktok-dancing-dataset/download?datasetVersionNumber=2).