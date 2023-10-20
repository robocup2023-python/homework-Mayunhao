import threading
import os

def changename(path,filename):
    #path="C:/Users/18210/Desktop/故乡吉他谱/
    i=0
    files = os.listdir(path)
    for file in files:
        filepath=os.path.join(path,file)
        newname=filename+"许巍"+str(i)+".jpg"
        newpath=os.path.join(path,newname)
        print(newpath)
        os.rename(filepath,newpath)
        i+=1
if __name__ == '__main__':
    source_dir= "E:\许巍歌曲"

    file_list = os.listdir(source_dir)
    # 4.遍历文件列表实现拷贝
    for file_name in file_list:
        # copy_file(file_name, source_dir, dest_dir)
        # 5.使用多线程实现多任务拷贝
        path = os.path.join(source_dir, file_name)
        print(path)
        sub_thread = threading.Thread(target=changename,
                                      args=(path,file_name))
        sub_thread.start()
