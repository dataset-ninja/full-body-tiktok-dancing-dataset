# https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-tiktok-dancing-dataset

import os, glob
import numpy as np
import supervisely as sly
from supervisely.io.fs import get_file_name_with_ext
from cv2 import connectedComponents
from tqdm import tqdm


def convert_and_upload_supervisely_project(api, workspace_id):

    project_name = "Full Body TikTok Dancing"
    dataset_path = "/Users/almaz/Downloads/archive_tiktok/segmentation_full_body_tik_tok_2615_img/segmentation_full_body_tik_tok_2615_img"
    ds_name = "ds"
    batch_size = 30
    images_folder_name = "images"
    masks_folder_name = "masks"


    def create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        mask_name = get_file_name_with_ext(image_path)
        mask_path = os.path.join(masks_path, mask_name)
        ann_np = sly.imaging.image.read(mask_path)[:, :, 0]

        obj_mask = ann_np == 255
        ret, curr_mask = connectedComponents(obj_mask.astype("uint8"), connectivity=8)
        for i in range(1, ret):
            obj_mask = curr_mask == i
            curr_bitmap = sly.Bitmap(obj_mask)
            curr_label = sly.Label(curr_bitmap, obj_class_dancing)
            labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


    obj_class_dancing = sly.ObjClass("dancing person", sly.Bitmap)
    obj_class_collection = sly.ObjClassCollection([obj_class_dancing])

    project_info = api.project.create(workspace_id, project_name)
    meta = sly.ProjectMeta(obj_classes=obj_class_collection)
    api.project.update_meta(project_info.id, meta.to_json())

    dataset = api.dataset.create(project_info.id, ds_name, change_name_if_conflict=True)

    images_path = os.path.join(dataset_path, images_folder_name)
    masks_path = os.path.join(dataset_path, masks_folder_name)
    images_names = os.listdir(images_path)

    progress = tqdm(desc=f"Create dataset {ds_name}", total=len(images_names))

    for img_names_batch in sly.batched(images_names, batch_size=batch_size):
        images_pathes_batch = [os.path.join(images_path, image_path) for image_path in img_names_batch]

        anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        api.annotation.upload_anns(img_ids, anns_batch)

        progress.update(len(img_names_batch))

    return project_info