from PIL import Image
from ultralytics import YOLO


def Detect(source):
    img = Image.open(source)

    model = YOLO(
        model="bdmod/bdmod.onnx",
        task="detect",
    )

    result = model.predict(
        source=img,
        conf=0.5,
        iou=0.3,
        device="cpu",
    )

    img_result = result[0].plot(
        font_size=18,
        line_width=3,
        color_mode="instance",
    )

    return img_result
