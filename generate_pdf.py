#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fpdf import FPDF
import os

class TravelPDF(FPDF):
    def __init__(self):
        super().__init__()
        # Use a Unicode font that supports Chinese
        font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
        if not os.path.exists(font_path):
            font_path = "/System/Library/Fonts/PingFang.ttc"
        self.add_font("zh", "", font_path, uni=True)
        self.add_font("zh", "B", font_path, uni=True)

    def header(self):
        self.set_font("zh", "B", 10)
        self.set_text_color(200, 169, 87)
        self.cell(0, 8, "越心 YUEXIN \u00b7 弘越地產官方合作平臺", align="L")
        self.ln(4)
        self.set_draw_color(200, 169, 87)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(8)

    def footer(self):
        self.set_y(-15)
        self.set_font("zh", "", 7)
        self.set_text_color(140, 140, 140)
        self.cell(0, 10, f"\u00a9 2025 越心 Yu\u00e8X\u012bn \u00b7 讓你安心置產，看見越南  |  第 {self.page_no()} 頁", align="C")

    def section_title(self, title):
        self.set_font("zh", "B", 16)
        self.set_text_color(200, 169, 87)
        self.cell(0, 12, title, ln=True)
        self.ln(2)

    def section_subtitle(self, title):
        self.set_font("zh", "B", 11)
        self.set_text_color(200, 169, 87)
        self.cell(0, 8, title, ln=True)
        self.ln(1)

    def tour_card(self, name, tags, desc, days_content, highlight, price, price_note):
        # Card background
        x, y = self.get_x(), self.get_y()
        card_start_y = y

        # Tour name
        self.set_font("zh", "B", 13)
        self.set_text_color(238, 232, 216)
        self.cell(0, 9, name, ln=True)

        # Tags
        self.set_font("zh", "", 8)
        self.set_text_color(200, 169, 87)
        self.cell(0, 6, "  |  ".join(tags), ln=True)
        self.ln(2)

        # Description
        self.set_font("zh", "", 9)
        self.set_text_color(160, 160, 150)
        self.multi_cell(0, 5.5, desc)
        self.ln(3)

        # Days content
        for day_title, items in days_content:
            self.set_font("zh", "B", 9)
            self.set_text_color(200, 169, 87)
            self.cell(0, 6, day_title, ln=True)
            self.set_font("zh", "", 9)
            self.set_text_color(160, 160, 150)
            for item in items:
                self.cell(5)
                self.cell(0, 5.5, f"\u2014  {item}", ln=True)
            self.ln(2)

        # Highlight
        self.set_font("zh", "", 8)
        self.set_text_color(200, 169, 87)
        self.cell(0, 5.5, f"\u25b8 {highlight}", ln=True)
        self.ln(2)

        # Price
        self.set_font("zh", "B", 12)
        self.set_text_color(238, 232, 216)
        self.cell(0, 7, price, ln=True)
        self.set_font("zh", "", 8)
        self.set_text_color(140, 140, 140)
        self.cell(0, 5, price_note, ln=True)

        # Divider
        self.ln(6)
        self.set_draw_color(60, 70, 55)
        self.set_line_width(0.2)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(6)


pdf = TravelPDF()
pdf.set_auto_page_break(auto=True, margin=20)

# ═══ Page 1: Cover ═══
pdf.add_page()
pdf.ln(40)
pdf.set_font("zh", "B", 28)
pdf.set_text_color(200, 169, 87)
pdf.cell(0, 15, "旅遊 × 考察 配套行程", align="C", ln=True)
pdf.ln(4)
pdf.set_font("zh", "", 11)
pdf.set_text_color(160, 160, 150)
pdf.cell(0, 7, "來都來了，順便玩一趟", align="C", ln=True)
pdf.cell(0, 7, "Business First. Pleasure Follows.", align="C", ln=True)
pdf.ln(8)
pdf.set_font("zh", "", 10)
pdf.multi_cell(0, 6, "來越南辦理粉紅簿、簽合約或交屋之餘，\n順道安排 1\u20133 天的在地旅遊行程，\n讓每一趟越南之行，都不虛此行。", align="C")
pdf.ln(20)
pdf.set_draw_color(200, 169, 87)
pdf.set_line_width(0.5)
pdf.line(70, pdf.get_y(), 140, pdf.get_y())
pdf.ln(10)
pdf.set_font("zh", "", 9)
pdf.set_text_color(140, 140, 140)
pdf.cell(0, 6, "越心 YUEXIN  |  弘越地產官方合作平臺", align="C", ln=True)
pdf.cell(0, 6, "LINE / WeChat / Email: info@yuexin.vn", align="C", ln=True)

# ═══ 建案考察 ═══
pdf.add_page()
pdf.section_title("最新優質建案考察")
pdf.set_font("zh", "", 9)
pdf.set_text_color(160, 160, 150)
pdf.multi_cell(0, 5.5, "來越南辦理行政事務，順便看看有沒有值得入手的新項目。由弘越地產專業顧問帶隊，實地走訪最新優質建案，提供完整分析與投資建議。")
pdf.ln(6)

pdf.tour_card(
    "河內房產考察",
    ["2 天", "含交通", "含午餐"],
    "聚焦河內核心區域與新興發展區，帶你走訪 3\u20135 個精選建案，深入了解河內房市最新動態與投資機會。",
    [
        ("Day 1", [
            "河內房市趨勢簡報 × 投資方向分析",
            "核心區建案考察（2\u20133 個項目）",
            "樣品屋實地參觀 × 格局動線分析",
            "周邊生活機能 × 交通建設導覽",
            "午餐交流（投資 Q&A）",
        ]),
        ("Day 2", [
            "新興發展區建案考察（2 個項目）",
            "區域發展規劃介紹",
            "租金報酬率 × 增值潛力評估",
            "午餐後自由時間或續安排旅遊行程",
        ]),
    ],
    "含弘越地產專業顧問全程陪同、建案分析報告、專車接送",
    "價格待定 / 人",
    "需提前 7 天預約，2 人成行"
)

pdf.tour_card(
    "河內 + 海防房產考察",
    ["2 天", "含交通", "含午餐", "跨城市"],
    "同時考察河內與海防兩大城市，海防作為北越重要港口城市，近年房市快速發展，投資潛力備受關注。",
    [
        ("Day 1 \u2014 河內", [
            "河內精選建案考察（2\u20133 個項目）",
            "樣品屋參觀 × 投資分析",
            "午餐交流 × 河內市場趨勢簡報",
            "下午出發前往海防（車程約 2 小時）",
        ]),
        ("Day 2 \u2014 海防", [
            "海防城市發展規劃介紹",
            "海防精選建案考察（2\u20133 個項目）",
            "工業區 × 港口經濟帶導覽",
            "午餐後返回河內（或續留海防）",
        ]),
    ],
    "含弘越地產雙城顧問陪同、兩地建案報告、專車跨城接送",
    "價格待定 / 人",
    "需提前 7 天預約，2 人成行"
)

pdf.tour_card(
    "胡志明市優質建案考察",
    ["1\u20132 天", "含交通", "含午餐"],
    "走訪胡志明市核心區與周邊新興開發區的優質建案，實地參觀樣品房，了解周邊交通建設與發展潛力。",
    [
        ("Day 1", [
            "胡志明市房市趨勢簡報",
            "第一郡 / 第二郡（守添新區）建案考察",
            "樣品房實地參觀",
            "午餐交流（投資 Q&A）",
            "周邊交通建設導覽",
        ]),
        ("Day 2（選配）", [
            "平陽工業園區考察",
            "工業園區周邊發展帶導覽",
            "午餐後自由時間或續安排旅遊行程",
        ]),
    ],
    "含弘越地產顧問全程陪同、建案分析報告、市區專車接送",
    "價格待定 / 人",
    "需提前 7 天預約，2 人成行"
)

# ═══ 北越旅遊 ═══
pdf.add_page()
pdf.section_title("北越行程（河內出發）")
pdf.set_font("zh", "", 9)
pdf.set_text_color(160, 160, 150)
pdf.multi_cell(0, 5.5, "適合在河內辦理行政事務後，安排 1\u20132 天的周邊旅遊。")
pdf.ln(6)

pdf.tour_card(
    "\u2605 下龍灣郵輪之旅（人氣推薦）",
    ["2 天 1 夜", "含住宿", "含三餐"],
    "世界自然遺產，搭乘豪華郵輪穿梭於近兩千座石灰岩島嶼之間，船上享用海鮮料理，夜宿海上欣賞星空。",
    [
        ("Day 1", [
            "河內出發 \u2192 下龍灣碼頭（車程約 2.5 小時）",
            "登船 × 迎賓午餐 × 海上巡航",
            "驚訝洞（Sung Sot Cave）探索",
            "獨木舟 / 竹筏遊覽漁村",
            "甲板日落 × 海鮮晚宴",
        ]),
        ("Day 2", [
            "甲板日出 × 太極晨操",
            "提托島（Ti Top）登頂觀景",
            "船上早午餐 × 退房下船",
            "返回河內（約下午 4 點抵達）",
        ]),
    ],
    "含中文導遊、郵輪住宿、全程餐食、河內來回接送",
    "USD 189 / 人起",
    "依郵輪等級浮動，2 人成行"
)

pdf.tour_card(
    "寧平陸龍灣一日遊",
    ["1 日遊", "含午餐"],
    "被譽為「陸上下龍灣」的寧平，搭乘小木舟穿越喀斯特地形河谷，壯麗山水如詩如畫。",
    [
        ("行程安排", [
            "河內出發 \u2192 寧平（車程約 2 小時）",
            "長安風景區木舟遊覽（約 2.5 小時）",
            "穿越三座天然石灰岩洞穴",
            "在地風味午餐（山羊肉料理）",
            "華閭古都遺跡參觀",
            "Mua Cave 登頂俯瞰全景（500 階）",
            "傍晚返回河內",
        ]),
    ],
    "含中文導遊、午餐、門票、河內來回接送",
    "USD 65 / 人起",
    "2 人成行，4 人以上另有優惠"
)

pdf.tour_card(
    "沙巴梯田 × 少數民族之旅",
    ["2 天 1 夜", "含住宿", "含三餐"],
    "前法國殖民避暑勝地，海拔 1,600 公尺的山城，壯闊梯田與多元少數民族文化的交匯之地。",
    [
        ("Day 1", [
            "河內出發 \u2192 老街 \u2192 沙巴（車程約 5 小時）",
            "貓貓村（Cat Cat Village）苗族文化體驗",
            "梯田步道健行（約 2 小時）",
            "沙巴小鎮散步 × 在地晚餐",
        ]),
        ("Day 2", [
            "番西邦峰纜車（越南最高峰 3,143m）",
            "雲海觀景 × 山頂健行",
            "午餐後返回河內（約傍晚抵達）",
        ]),
    ],
    "含中文導遊、住宿、全程餐食、河內來回接送、纜車票",
    "USD 169 / 人起",
    "依住宿等級浮動，2 人成行"
)

pdf.tour_card(
    "河內市區文化一日遊",
    ["1 日遊", "含午餐"],
    "千年古都深度走訪——法式建築、老街巷弄、水上木偶戲，品嚐最道地的河內美食。",
    [
        ("行程安排", [
            "胡志明紀念堂 × 一柱寺",
            "文廟（越南最古老大學）",
            "還劍湖 × 玉山祠散步",
            "河內老街（三十六行街）漫遊",
            "在地美食午餐（河粉 / 烤肉米線）",
            "西湖周邊法式街區探索",
            "傍晚水上木偶戲觀賞",
        ]),
    ],
    "含中文導遊、午餐、門票、市區接送",
    "USD 55 / 人起",
    "2 人成行"
)

# ═══ 南越旅遊 ═══
pdf.add_page()
pdf.section_title("南越行程（胡志明市出發）")
pdf.set_font("zh", "", 9)
pdf.set_text_color(160, 160, 150)
pdf.multi_cell(0, 5.5, "適合在胡志明市辦理行政事務後，安排 1\u20133 天的周邊旅遊。")
pdf.ln(6)

pdf.tour_card(
    "胡志明市區文化一日遊",
    ["1 日遊", "含午餐"],
    "東方巴黎的法式風情與越戰歷史交織，走訪經典地標，品嚐南越特色美食。",
    [
        ("行程安排", [
            "統一宮（獨立宮）歷史導覽",
            "西貢聖母大教堂 × 中央郵局",
            "戰爭遺跡博物館",
            "在地午餐（越南河粉 / 碎米飯）",
            "濱城市場逛街購物",
            "咖啡公寓 × 西貢河畔漫步",
        ]),
    ],
    "含中文導遊、午餐、門票、市區接送",
    "USD 49 / 人起",
    "2 人成行"
)

pdf.tour_card(
    "\u2605 古芝地道歷史一日遊（人氣推薦）",
    ["1 日遊", "含午餐"],
    "親身走進越戰時期的地下城，三層地道構造含醫務室、廚房、會議室，體驗歷史的震撼。",
    [
        ("行程安排", [
            "胡志明市出發 \u2192 古芝（車程約 1.5 小時）",
            "越戰歷史影片導覽",
            "實際進入地下隧道體驗",
            "越戰時期陷阱與防禦設施展示",
            "在地午餐（木薯 / 越式料理）",
            "周邊果園或手工藝村參觀",
            "下午返回胡志明市",
        ]),
    ],
    "含中文導遊、午餐、門票、來回接送",
    "USD 55 / 人起",
    "2 人成行"
)

pdf.tour_card(
    "湄公河（美托）一日遊",
    ["1 日遊", "含午餐"],
    "乘船遊覽湄公河三角洲，探訪椰子糖工坊、水果島、蜂蜜農場，體驗南越水鄉風情。",
    [
        ("行程安排", [
            "胡志明市出發 \u2192 美托（車程約 1.5 小時）",
            "湄公河遊船巡航",
            "椰子糖工坊參觀 × 品嚐",
            "水果島午餐 × 熱帶水果品嚐",
            "竹筏穿越椰林水道",
            "蜂蜜茶品嚐 × 傳統音樂演奏",
            "下午返回胡志明市",
        ]),
    ],
    "含中文導遊、午餐、船票、來回接送",
    "USD 49 / 人起",
    "2 人成行"
)

pdf.tour_card(
    "頭頓海濱度假之旅",
    ["2 天 1 夜", "含住宿", "含三餐"],
    "胡志明市後花園，三面環海的度假勝地。登上亞洲最大基督像，享受悠閒海濱時光。",
    [
        ("Day 1", [
            "胡志明市出發 \u2192 頭頓（車程約 2 小時）",
            "前灘（Front Beach）海濱散步",
            "海鮮午餐",
            "耶穌山基督像（811 階登頂）",
            "燈塔觀景 × 日落",
            "海鮮晚宴 × 入住海景飯店",
        ]),
        ("Day 2", [
            "後灘（Back Beach）海邊早餐",
            "白宮（Villa Blanche）法式建築參觀",
            "海鮮市場自由採購",
            "午後返回胡志明市",
        ]),
    ],
    "含中文導遊、海景住宿、全程餐食、來回接送",
    "USD 139 / 人起",
    "依飯店等級浮動，2 人成行"
)

pdf.tour_card(
    "美奈沙丘 × 漁村之旅",
    ["2 天 1 夜", "含住宿", "含三餐"],
    "越南最獨特的沙漠海岸地貌——紅白沙丘、仙女溪、漁村，感受截然不同的越南面貌。",
    [
        ("Day 1", [
            "胡志明市出發 \u2192 美奈（車程約 4 小時）",
            "仙女溪（Fairy Stream）赤腳漫步",
            "美奈漁村 × 圓籃船拍照",
            "海鮮晚餐 × 入住度假村",
        ]),
        ("Day 2", [
            "清晨白沙丘日出 × 沙地吉普車",
            "紅沙丘滑沙體驗",
            "度假村早午餐 × 海邊放鬆",
            "午後返回胡志明市",
        ]),
    ],
    "含中文導遊、度假村住宿、全程餐食、來回接送、吉普車",
    "USD 159 / 人起",
    "依住宿等級浮動，2 人成行"
)

# ═══ 備註頁 ═══
pdf.add_page()
pdf.ln(10)
pdf.section_title("預約與注意事項")
pdf.ln(4)

notes = [
    ("搭配行政辦理更划算", "在辦理粉紅簿、交屋驗收或合約簽署時，同步預訂旅遊行程，即可享有 9 折優惠。"),
    ("預約方式", "請透過 LINE、微信或 Email 聯繫我們，提供出發日期、人數與想要的行程，專人為您安排。"),
    ("成行人數", "所有行程最低 2 人成行，4 人以上可享團體優惠，歡迎洽詢。"),
    ("取消政策", "出發前 7 天可免費取消；3\u20136 天前取消收取 50% 費用；3 天內取消恕不退費。"),
    ("費用包含", "除特別註明外，所有行程均含中文導遊、交通接送、門票及餐食。住宿行程含一晚住宿。"),
    ("費用不含", "個人消費、小費、旅遊保險、未列明之餐食及酒水飲料。"),
]

for title, desc in notes:
    pdf.set_font("zh", "B", 10)
    pdf.set_text_color(200, 169, 87)
    pdf.cell(0, 7, title, ln=True)
    pdf.set_font("zh", "", 9)
    pdf.set_text_color(160, 160, 150)
    pdf.multi_cell(0, 5.5, desc)
    pdf.ln(5)

pdf.ln(10)
pdf.set_draw_color(200, 169, 87)
pdf.set_line_width(0.5)
pdf.line(70, pdf.get_y(), 140, pdf.get_y())
pdf.ln(8)
pdf.set_font("zh", "B", 11)
pdf.set_text_color(200, 169, 87)
pdf.cell(0, 7, "聯絡我們", align="C", ln=True)
pdf.set_font("zh", "", 9)
pdf.set_text_color(160, 160, 150)
pdf.cell(0, 6, "LINE 官方帳號  |  WeChat: yuexin_vn  |  Email: info@yuexin.vn", align="C", ln=True)
pdf.cell(0, 6, "服務時間：09:00\u201321:00（含週末及假日）", align="C", ln=True)

# Save
output_path = os.path.expanduser("~/越心_旅遊考察行程.pdf")
pdf.output(output_path)
print(f"PDF saved to: {output_path}")
