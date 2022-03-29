# -*- coding: utf-8 -*-
import datetime
import os
import sys

def get_base_path():
    base_path = ""
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    return base_path

def get_exe_path(file):
    # file is the name of your exe file e.g nmap.exe
    base_path = get_base_path()
    exe_path = os.path.join(base_path, file)
    return exe_path


def avif2jpg(avif_ful_path, save_path='output.jpg'):
    try:
        avifdec = get_exe_path("avifdec.exe")
        #avifdec = "avifdec.exe"
        #cmd = '%s %s %s' % (avifdec, avif_ful_path, save_path)
        cmd = '%s "%s" "%s"' % (avifdec, avif_ful_path, save_path)
        print(cmd)
        os.system(cmd)
        if os.path.exists(save_path):
            print("处理文件 %s 成功" % avif_ful_path)
        else:
            print("处理文件 %s 失败" % avif_ful_path)
    except BaseException as e:
        print(e.args)


def handle_avif_file(file_path):
    fpath, fname = os.path.split(file_path)
    pre_file_name = fname.rsplit(".")[0]
    new_file_full_path = os.path.join(fpath, pre_file_name + ".jpg")
    avif2jpg(file_path, new_file_full_path)


def handle_dir(root_path):
    if os.path.isdir(root_path):
        dir_or_files = os.listdir(root_path)
        for file_name in dir_or_files:
            file_full_path = os.path.join(root_path, file_name)
            if os.path.isdir(file_full_path):
                continue
            if '.avif' in file_name.lower():
                handle_avif_file(file_full_path)
    else:
        fpath, fname = os.path.split(root_path)
        if '.avif' in fname.lower():
            handle_avif_file(root_path)


if __name__ == '__main__':
    print('#####\t version 1.0 20220329 \t#####')
    try:
        print('python info %s\n' % sys.version)
    except BaseException as e:
        pass
    while True:
        start_time = datetime.datetime.now()
        inputfile = input('请输入想要重命名处理文件夹路径（如：E:/input/）：')
        if inputfile.startswith('"'):
            inputfile = inputfile[1:-1]
        if inputfile.endswith('"'):
            inputfile = inputfile[0:-2]
        handle_dir(inputfile)
        end_time = datetime.datetime.now()
        print('\n\n用时' + str(end_time - start_time) + '秒')
        print('###\tFinish!\t###\n')
