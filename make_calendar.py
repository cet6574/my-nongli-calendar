import re
import urllib.request

URL = "https://yangh9.github.io/ChinaCalendar/cal_lunar.ics"
OUT = "lunar_short.ics"

data = urllib.request.urlopen(URL).read().decode("utf-8")

def clean(match):
    s = match.group(1)
    # 提取『』内的农历日期,去掉空格和"2026年"这类年份
    m = re.search(r"『([^』]*)』", s)
    if m:
        text = m.group(1)                      # 如 "腊月 初二 2026年"
        text = re.sub(r"\d{4}年", "", text)     # 去掉年份
        text = text.replace(" ", "")           # 去掉空格
        return "SUMMARY:" + text               # 如 "腊月初二"
    return "SUMMARY:" + s

data = re.sub(r"^SUMMARY:(.+)$", clean, data, flags=re.MULTILINE)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(data)

print("done")
