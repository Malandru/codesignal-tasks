from collections import Counter

def frequencyAnalysis(encryptedText):
    return Counter(encryptedText).most_common(1).pop()[0]


encryptedText = "$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ"
print(frequencyAnalysis(encryptedText))