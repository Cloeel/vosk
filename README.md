# vosk
実行方法\n
1.oggファイルをwavファイルに変換\n
　コマンド：ffmpeg -i <input_file_path> -ar 16000 -ac 1 -f s16le <output_file_path> \n
2.voskのプログラムを実行\n
　コマンド：python3 vosk_moji.py <audio_file_path>\n
3.実行した後のファイルはtextfilesに格納。\n
4.textfilesの中から任意の文字起こし結果へ移動。
