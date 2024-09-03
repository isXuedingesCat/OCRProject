OCR_CONFIG = {
    # text detector
    "det_algorithm": "DB",
    "det_model_dir": "/home/shijia/pycode/OCRProject/ocrcore/infer/ocr_det/inference.onnx",
    "det_limit_side_len": 960,
    "det_limit_type": "max",
    "det_box_type": "quad",

    # DB params
    "det_db_thresh":0.3,
    "det_db_box_thresh":0.6,
    "det_db_unclip_ratio":1.5,
    "max_batch_size":10,
    "use_dilation":False,
    "det_db_score_mode":"fast",

    # EAST parmas
    "det_east_score_thresh":0.8,
    "det_east_cover_thresh":0.1,
    "det_east_nms_thresh":0.2,

    # SAST parmas
    "det_sast_score_thresh":0.5,
    "det_sast_nms_thresh":0.2,

    # PSE parmas
    "det_pse_thresh": 0,
    "det_pse_box_thresh": 0.85,
    "det_pse_min_area": 16,
    "det_pse_scale": 1,

    # FCE parmas
    "scales":[8,16,32],
    "alpha":1.0,
    "beta":1.0,
    "fourier_degree":5,

    # params for text recognizer
    "rec_algorithm":"SVTR_LCNet",
    "rec_model_dir":"/home/shijia/pycode/OCRProject/ocrcore/infer/ocr_rec/inference.onnx",
    "rec_image_inverse":True,
    "rec_image_shape":[3,48,320],
    "rec_batch_num":6,
    "max_text_length":25,
    "rec_char_dict_path":"/home/shijia/pycode/OCRProject/ocrcore/infer/ocr_rec/ppocr_keys_v1.txtt",
    "use_space_char":True,
    "vis_font_path":"/home/shijia/pycode/OCRProject/ocrcore/infer/ocr_rec/simfang.ttf",
    "drop_score":0.5,

    # params for e2e
    "e2e_algorithm":"PGNet",
    "e2e_model_dir":"",
    "e2e_limit_side_len":768,
    "e2e_limit_type":"max",

    # PGNet parmas
    "e2e_pgnet_score_thresh":0.5,
    "e2e_char_dict_path":"./ppocr/utils/ic15_dict.txt",
    "e2e_pgnet_valid_set":"totaltext",
    "e2e_pgnet_mode":"fast",

    # params for text classifier
    "use_angle_cls":False,
    "cls_model_dir":"/home/shijia/pycode/OCRProject/ocrcore/infer/ocr_cls/inference.onnx",
    "cls_image_shape":[3,48,192],
    "label_list":["0", "180"],
    "cls_batch_num":6,
    "cls_thresh":0.9,

    # extended function
    "return_word_box":False,
    "save_log_path":"./log_output/"

}