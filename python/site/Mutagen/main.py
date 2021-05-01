import glob
import os
from mutagen.easyid3 import EasyID3

# ID3を編集する関数
def editId3(file):
    tags = EasyID3(file)            # 音声ファイルをEasyID3オブジェクトに変換し、編集可能にする
    tags['artist'] = '旺文社'                       # アーティスト名を変更
    tags['album'] = '英検準1級　でる順パス単'        # アルバム名を変更
    tags['albumartist'] = '旺文社'                  # アルバムのアーティスト名を変更
    tags.save()

# 指定されたディレクトリ内のファイル情報を取得する関数
def bundle_resize(dir):
    path_list = glob.glob(dir + '/*.mp3')       # 指定されたディレクトリ内の全てのファイルを取得
    # print(path_list)

    # ファイルのフルパスからファイル名と拡張子を抽出
    for i in path_list:
        # print(i)
        # file = os.path.basename(i)          # 拡張子ありファイル名を取得
        # print(file)
        # print(type(file))
        editId3(i)
    return

# ファイルを探してリサイズする関数を実行
bundle_resize('/home/telur4/Music/p1q_all')