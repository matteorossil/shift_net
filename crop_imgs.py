import os
import argparse
import cv2

parser = argparse.ArgumentParser(description='Read SAYCam videos')
parser.add_argument('--data', default='/vast/mr6744/SAYCAM_large_deblur', type=str, help='save directory')
parser.add_argument('--save-dir', default='/vast/mr6744/SAYCAM_deblur_new', type=str, help='save directory')

if __name__ == '__main__':

    args = parser.parse_args()

    class_list = os.listdir(args.data)[300:] ## remove after
    print(class_list)

    for class_ in class_list:

        dir_path = os.path.join(args.save_dir, class_)
        os.mkdir(dir_path)

        curr_dir_path = os.path.join(args.data, class_)

        imgs = os.listdir(curr_dir_path)

        for img in imgs:

            img_ = cv2.imread(os.path.join(curr_dir_path, img))
            img_ = cv2.flip(img_, -1)
            resized_frame = cv2.resize(img_, (341, 256), interpolation=cv2.INTER_CUBIC)
            cropped_frame = resized_frame[0:0 + 224, 58:58 + 224]
            cv2.imwrite(os.path.join(dir_path, img), cropped_frame[::-1, ::-1, :])
