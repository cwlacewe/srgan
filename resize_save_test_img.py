from PIL import Image


def resize_img(in_img_file, out_img_file, new_h, new_w):
    img = Image.open(in_img_file)
    new_img = img.resize((new_w, new_h), Image.ANTIALIAS)
    new_img.save(out_img_file)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('--in_img', type=str, default=None, help='Path to image to resize')
    parser.add_argument('--out_img', type=str, default=None, help='Path to save resulting image')
    parser.add_argument('--new_h', type=int, default=None, help='New height for image')
    parser.add_argument('--new_w', type=int, default=None, help='New width for image')
    args = parser.parse_args()
    resize_img(args.in_img, args.out_img, args.new_h, args.new_w)
