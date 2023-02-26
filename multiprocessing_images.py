import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    'photo-1677040628614-53936ff66632.jpg',
    'photo-1676595670250-626d402700e0.jpg',
    'photo-1676737830610-2cebe4843eca.jpg',
    'photo-1676920410907-8d5f8dd4b5ba.jpg',
    'photo-1653219305693-28ad4baf623a.jpg',
    'photo-1676868720246-d608555dd3ba.jpg',
    'photo-1676625196031-b8b0d11c9172.jpg',
    'photo-1676798635656-b78321e08eb5.jpg',
    'photo-1676846631735-e10bf09d49d8.jpg',
    'photo-1676798385570-8fabdbf995ec.jpg',
    'photo-1676765374032-57d90e318b8f.jpg',
    'photo-1676744625189-48f9f6ad077f.jpg',
    'photo-1676845578082-2e08e7c359b4.jpg',
    'photo-1627209876750-9db65322c4ed.jpg'
]

set_size = (1000, 1000)


def image_processor(img_name: str) -> None:
    """
    Process the given image and saves it in the processed_image folder.

    :param img_name: name of the image
    :return: None
    """
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(10))
    img.thumbnail(set_size)
    img.save(f'processed_images/{img_name}')
    print(f'Processed the image: {img_name}')


if __name__ == '__main__':
    start_time = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(image_processor, img_names)

    end_time = time.perf_counter()
    print(f'Completed the process in {round(end_time - start_time, 2)} seconds')
