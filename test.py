import shutil

INPUT = "test.sspm"
OUTPUT = "out_maps/test_auto.sspm"

# 追加したいノーツ
note_data = bytes([
    0x2A, 0x0D, 0x00, 0x00,
    0x00, 0x00,
    0x02,
    0x02
])

with open(INPUT, "rb") as f:
    data = f.read()

# 最後に追加
data += note_data

with open(OUTPUT, "wb") as f:
    f.write(data)

print("生成完了")
