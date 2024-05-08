import os
import re

def replace_paths(folder_path):
    # 定义要替换的路径模式和对应的本地文件路径的字典
    path_mapping = {
        r"/nrsdk/development/depth-mesh/use-meshes-in-the-editor\b": "./UseMeshesintheEditor.html",
        r"/nrsdk/development/spatial-anchor/mapping-example-scene\b": "./MappingExampleScene.html",
        r"/nrsdk/development/spatial-anchor/tutorial-halloween-treasure-hunt/handle-the-situation-of-failed-anchor-saving\b": "./HandletheSituationofFailedAnchorSaving.html",
        r"/nrsdk/development/spatial-anchor/tutorial-halloween-treasure-hunt\b": "./Tutorial_HalloweenTreasureHunt.html",
        r"/nrsdk/development/spatial-anchor/tutorial-sharing-anchors/setting-up-photon\b": "./SettingUpPhoton.html",
        r"/nrsdk/development/spatial-anchor/tutorial-sharing-anchors/cloud-storage-firebase-optional\b": "./CloudStorage_Firebase(optional).html",
        r"/nrsdk/development/spatial-anchor/tutorial-sharing-anchors/cloud-storage-aliyun-oss-optional\b": "./CloudStorage_AliyunOSS(optional).html",
        r"/nrsdk/development/spatial-anchor/tutorial-sharing-anchors/implementing-cloud-save-and-load\b": "./ImplementingCloudSaveandLoad.html",
        r"/nrsdk/development/spatial-anchor/tutorial-sharing-anchors/sharing-anchors-with-photon\b": "./SharingAnchorswithPhoton.html",
        r"/nrsdk/development/spatial-anchor/tutorial-sharing-anchors\b": "./Tutorial_SharingAnchors.html",
        r"/nrsdk/development/depth-mesh/meshing-manager-overview\b": "./MeshingManagerOverview.html",
        r"/nrsdk/development/depth-mesh/tutorial-mesh-collision\b": "./Tutorial_MeshCollision.html",
        r"/nrsdk/development/depth-mesh\b": "./DepthMesh.html",
        r"/nrsdk/development/hand-tracking\b": "./HandTracking.html",
        r"/nrsdk/development/spatial-anchor\b": "./SpatialAnchor.html"
    }

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否以 .html 结尾
        if filename.endswith(".html"):
            file_path = os.path.join(folder_path, filename)

            # 读取文件内容
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            # 替换路径
            for old_path, new_path in path_mapping.items():
                content = re.sub(old_path, new_path, content)

            # 将替换后的内容写回文件
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)

            print(f"Processed: {filename}")


# 指定包含HTML文件的文件夹路径
folder_path = "/Users/xreal/Downloads/NRSDKOfflineHTML"

# 调用文件处理函数
replace_paths(folder_path)