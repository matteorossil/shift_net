import os
import argparse
import shutil

parser = argparse.ArgumentParser(description='Read SAYCam videos')
parser.add_argument('--data', default='/vast/mr6744/SAYCAM', type=str, help='save directory')
parser.add_argument('--save-dir', default='/vast/mr6744/SAYCAM_blur', type=str, help='save directory')

if __name__ == '__main__':

    args = parser.parse_args()

    class_list = os.listdir(args.data)
    print(class_list)

    class_counter = 0

    for class_ in class_list:

        img_counter = 0

        curr_dir_name = os.path.join(args.save_dir, 'class_{:04d}'.format(class_counter))
        os.mkdir(curr_dir_name)

        dir_path = os.path.join(args.data, class_)

        imgs = os.listdir(dir_path)

        for img in imgs:


            if (img_counter - 2) % 5 == 0:
                image_path = os.path.join(dir_path, img)
                #print(image_path)
                image_dest_path = os.path.join(curr_dir_name, img)
                #print(image_dest_path)
                shutil.copy(image_path, image_dest_path)

            img_counter += 1

        
        class_counter += 1

