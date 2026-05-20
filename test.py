import struct
import os

INPUT = "test.sspm"
OUTPUT = "out_maps/generated.sspm"

os.makedirs("out_maps", exist_ok=True)

with open(INPUT, "rb") as f:
    data = bytearray(f.read())

# =====================================
# ノーツ数変更
# =====================================

changed = 0

for i in range(len(data) - 4):

    if data[i:i+4] == b'\x01\x00\x00\x00':

        data[i:i+4] = b'\x0A\x00\x00\x00'

        changed += 1

        if changed == 2:
            break

print("ノーツ数変更:", changed)

# =====================================
# 元ノーツ位置
# 1000ms
# =====================================

base_time = b'\xE8\x03\x00\x00'

index = data.find(base_time)

if index == -1:
    print("ノーツが見つからない")
    exit()

print("ノーツ位置:", index)

# =====================================
# 追加ノーツ生成
# 左上固定
# =====================================

new_notes = bytearray()

for n in range(1, 10):

    time_ms = (n + 1) * 1000

    note = struct.pack(
        "<I B B B",
        time_ms,
        0,  # x
        0,  # y
        0   # type
    )

    new_notes.extend(note)

# =====================================
# 元ノーツ直後へ挿入
# =====================================

NOTE_SIZE = 7

insert_pos = index + NOTE_SIZE

data[insert_pos:insert_pos] = new_notes

# =====================================
# 保存
# =====================================

with open(OUTPUT, "wb") as f:
    f.write(data)

print("生成完了")
print(OUTPUT)