from ultralytics import YOLO


def Detect(source):
    model = YOLO(
        model="bdmod/bdmod.onnx",
        task="detect",
    )

    result = model.predict(
        source=source,
        conf=0.5,
        iou=0.4,
        imgsz=640,
        device="cpu",
    )

    img_result = result[0].plot(
        font_size=14,
        line_width=2,
        color_mode="instance",
    )
    return img_result
