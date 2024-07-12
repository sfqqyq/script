"""
计算两张图片的相似度
使用感知hash的方式进行图片相似度计算

"""

from PIL import Image
import imagehash

# 打开并加载图片
image1 = Image.open('files/1.png')
image2 = Image.open('files/3.png')

# 计算感知哈希
hash1 = imagehash.average_hash(image1)
hash2 = imagehash.average_hash(image2)

# 打印哈希值
print("Hash 1:", hash1)
print("Hash 2:", hash2)


# 计算汉明距离
similarity = 1.0 - (hash1 - hash2) / max(len(hash1), len(hash2))

# 打印相似度
print("Similarity:", similarity)
