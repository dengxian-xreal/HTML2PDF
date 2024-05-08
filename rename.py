import os


def rename_files(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否以 .html 结尾
        if filename.endswith(".html"):
            # 去掉文件名中的空格
            new_filename = filename.replace(" ", "")

            # 去掉文件名中的 "_v2.2.0_NRSDK" 字符串
            new_filename = new_filename.replace("_v2.2.0_NRSDK", "")

            # 构建完整的文件路径
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)

            # 重命名文件
            os.rename(old_path, new_path)
            # print(f"Renamed: {filename} -> {new_filename}")
            print(f"{new_filename}")

# 指定包含HTML文件的文件夹路径
folder_path = "/Users/xreal/Downloads/NRSDKOfflineHTML"

# 调用文件重命名函数
rename_files(folder_path)